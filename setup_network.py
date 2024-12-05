from network_device_config import NetworkManager

def main():
    # Initialize network manager
    network = NetworkManager()
    
    # Create project
    project_name = "Enterprise_Network_Group17"
    if not network.create_project(project_name):
        return
    
    # Add devices with proper spacing
    devices = [
        ("Router", 1, -200, 0),
        ("Switch", 1, 0, 0),
        ("Switch", 2, 200, 0)
    ]
    
    for device_type, number, x, y in devices:
        node = network.add_device(device_type, number, x, y)
        if node:
            print(f"Created {node.name}")
            network.configure_device(node)

if __name__ == "__main__":
    main()
