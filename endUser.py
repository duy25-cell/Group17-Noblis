#!/usr/bin/env python3
import os
import time
import subprocess
from pathlib import Path
from scapy.all import *
from scapy.layers.inet import IP, ICMP

# Configuration
INTERFACE = 'eth0'                   # Confirm with 'ip a'
TARGET_IP = '8.8.8.8'                # Using single reliable target
PCAP_DIR = '/tmp/kali_traffic'       # Using /tmp for guaranteed permissions
SIMULATION_DURATION = 30             # Seconds to capture

def setup_environment():
    """Ensure directory exists with proper permissions"""
    Path(PCAP_DIR).mkdir(exist_ok=True)
    os.chmod(PCAP_DIR, 0o777)

def generate_traffic():
    """Generate simple ICMP traffic"""
    print("Generating ICMP traffic to", TARGET_IP)
    try:
        for _ in range(30):
            send(IP(dst=TARGET_IP)/ICMP())
            time.sleep(0.5)
    except Exception as e:
        print(f"Traffic generation error: {e}")

def capture_traffic():
    """Reliable packet capture using tcpdump"""
    pcap_file = f"{PCAP_DIR}/capture_{int(time.time())}.pcap"
    
    print(f"Starting capture on {INTERFACE} for {SIMULATION_DURATION}s...")
    
    try:
        # Start traffic generation in background process
        traffic_proc = subprocess.Popen(
            ['python3', '-c', 
             'from scapy.all import send, IP, ICMP; '
             'from time import sleep; '
             'for _ in range(30): send(IP(dst="8.8.8.8")/ICMP()); sleep(0.5)'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        # Run capture
        subprocess.run([
            'sudo', 'tcpdump',
            '-i', INTERFACE,
            '-w', pcap_file,
            '-G', str(SIMULATION_DURATION),
            '-W', '1',
            'icmp'
        ], check=True)
        
        traffic_proc.terminate()
        return pcap_file
        
    except subprocess.CalledProcessError as e:
        print(f"Capture failed: {e}")
        return None

def main():
    setup_environment()
    pcap_file = capture_traffic()
    
    if pcap_file and os.path.exists(pcap_file):
        print(f"\nSUCCESS: Capture saved to {pcap_file}")
        print(f"File size: {os.path.getsize(pcap_file)} bytes")
    else:
        print("\nFAILED: No packets captured")

if __name__ == "__main__":
    main()