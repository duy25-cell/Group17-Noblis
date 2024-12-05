from gns3fy import Gns3Connector, Project, Node, Link
import telnetlib
import time
import random

class DeviceConfigurator:
    def __init__(self):
        self.ip_ranges = {
            'network': ('10.0.0.1', '10.0.255.254'),
            'hosts': ('192.168.0.1', '192.168.255.254')
        }
        
    def generate_hostname(self, device_type, number):
        return f"{device_type}{number}"
    
    def generate_ip(self, range_type):
        start, end = self.ip_ranges[range_type]
        start_parts = list(map(int, start.split('.')))
        end_parts = list(map(int, end.split('.')))
        
        ip_parts = []
        for i in range(4):
            if i == 3:  # Last octet
                value = random.randint(1, 254)  # Avoid 0 and 255
            else:
                value = random.randint(start_parts[i], end_parts[i])
            ip_parts.append(str(value))
            
        return '.'.join(ip_parts)

    def get_initial_config_commands(self, hostname):
        return [
            "no",  # Skip initial setup
            "enable",
            "configure terminal",
            f"hostname {hostname}",
            "enable algorithm-type sha256 secret group17enablesecret",
            "username group17admin algorithm-type sha256 secret group17adminpassword",
            "line console 0",
            "login local",
            "exec-timeout 15",
            "logging synchronous",
            "do write",
            "end"
        ]

class NetworkManager:
    def __init__(self, server_url="http://localhost:3080"):
        self.server = Gns3Connector(server_url)
        self.project = None
        self.nodes = {}
        self.configurator = DeviceConfigurator()

    def create_project(self, project_name):
        try:
            projects = self.server.projects
            self.project = next((p for p in projects if p.name == project_name), None)
            
            if not self.project:
                self.project = Project(name=project_name, connector=self.server)
                self.project.create()
            else:
                self.project.open()
            return True
        except Exception as e:
            print(f"Project creation failed: {e}")
            return False

    def add_device(self, device_type, number, x=0, y=0):
        hostname = self.configurator.generate_hostname(device_type, number)
        template = f"cisco_{device_type.lower()}"
        
        try:
            node = Node(
                project_id=self.project.project_id,
                connector=self.server,
                name=hostname,
                template=template,
                x=x,
                y=y
            )
            node.create()
            self.nodes[hostname] = node
            return node
        except Exception as e:
            print(f"Device creation failed: {e}")
            return None

    def configure_device(self, node):
        try:
            # Wait for device to boot
            time.sleep(45)
            
            console = telnetlib.Telnet(node.console_host, node.console_port)
            commands = self.configurator.get_initial_config_commands(node.name)
            
            for cmd in commands:
                console.write(f"{cmd}\n".encode())
                time.sleep(1)
            
            console.close()
            return True
        except Exception as e:
            print(f"Configuration failed for {node.name}: {e}")
            return False
