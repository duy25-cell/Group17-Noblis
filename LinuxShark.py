# Packet capture script for Linux systems

import os
import subprocess

def install_tshark():   # Attempts to install tshark

    try:
        print("Updating packages...")
        subprocess.run(["sudo", "apt-get", "update"], check=True)

        print("Installing Wireshark...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "wireshark"], check=True)

        print("Installing tshark...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "tshark"], check=True)
        print("tshark installation successful!")

    except:
        print("An error has occurred during installation.")


def capture_traffic(capture_duration=60, interface="any"):  # Attempts to capture network traffic on chosen interface for chosen duration

    output_file = "/tmp/output.pcap"  # Save file in /tmp, I was having permission errors, will fix later

    try:
        print(f"Starting capture on interface '{interface}' for {capture_duration} seconds...")
        print(f"Saving output to '{output_file}'.")

        subprocess.run(["sudo", "tshark", "-i", interface, "-a", f"duration:{capture_duration}", "-w", output_file], check=True)   # Runs the tshark capture command
        print("Capture completed successfully.")

        change_file_ownership(output_file)   # Fixes ownership of the file

    except:
        print("Error during capture.")


def change_file_ownership(file_path):   # Attempts to fix created file ownership

    try:
        user_id = os.getuid()
        group_id = os.getgid()

        os.chown(file_path, user_id, group_id)
        print(f"Changed ownership of '{file_path}' to user ID {user_id}.")

    except:
        print(f"An error has occured while changing the file ownership.")


if __name__ == "__main__":
    capture_duration_seconds = 30  # Duration of the capture in seconds
    capture_interface = "lo"      # Interface to capture traffic on

    install_tshark()
    capture_traffic(capture_duration_seconds, capture_interface)
