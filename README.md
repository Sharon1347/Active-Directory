# Active Directory Home Lab (Red & Blue Team Lab)

This project showcases a hands-on Active Directory lab environment designed for practicing both offensive (Red Team) and defensive (Blue Team) cybersecurity techniques.

I set up a realistic virtual environment with multiple machines to simulate a real-world enterprise network, performed attack simulations, and monitored the network activity using security tools.

---

## 📌 Lab Diagram

Below is a visual overview of the lab setup showing how the machines are connected.

![Lab Diagram](screenshots/ACTIVE%20DIRECTORY%20(Home%20Lab).drawio.png)

---

## 💻 Machines & Tools Used

| Machine              | Purpose/Role                  | OS/Tool Version   |
|----------------------|-------------------------------|-------------------|
| **Windows Server 2025** | Domain Controller (Active Directory) | Windows Server 2025 |
| **Windows 11**          | Target Workstation (Joined to Domain) | Windows 11 |
| **Kali Linux**          | Attacker Machine (Penetration Testing) | Kali Linux 2025 |
| **Ubuntu (Splunk Server)** | Security Monitoring (SIEM) | Ubuntu 22.04 + Splunk |
| **Sysmon**              | Advanced Logging & Monitoring | Sysmon v14+ |
| **Atomic Red Team**     | Attack Simulation Framework   | Latest |

---

## ⚙️ Lab Workflow & Tasks Performed

### ✅ 1. Domain Controller (Windows Server 2025)
- Installed Active Directory Domain Services (ADDS).
- Configured the domain: `MYDFIR.LOCAL`.
- Promoted the machine to a Domain Controller.
- Set up DNS and other required services.

### ✅ 2. Domain Join (Windows 11 Workstation)
- Configured network settings to point to the Domain Controller’s DNS.
- Joined Windows 11 machine to the domain `MYDFIR.LOCAL`.
- Verified successful domain join using PowerShell commands:
  - `whoami`
  - `nltest /dsgetdc:mydfir.local`
- Synced time using:
  - `w32tm /resync`
- Rebooted the machine to apply changes.

### ✅ 3. Installed Splunk (on Ubuntu)
- Installed Splunk for log analysis and monitoring.
- Configured Splunk to collect logs from Windows machines.
- Added Sysmon logs to Splunk for deeper visibility.

### ✅ 4. Installed Sysmon (on Windows Machines)
- Deployed Sysmon for detailed event logging on Windows.
- Forwarded Sysmon logs to Splunk.

### ✅ 5. Attack Simulation (on Kali Linux)
- Attempted brute-force attacks on the Windows 11 machine using `xfreerdp` and custom Python scripts.
- Verified successful authentication via brute-force on RDP.
- Captured logs of these attacks in Splunk.

### ✅ 6. Security Detection (on Splunk)
- Reviewed and analyzed the logs from Sysmon and Splunk.
- Verified that Splunk successfully detected the attack activities.

---

## 📸 Screenshots (Proof of Work)

| Screenshot Description                     | File Path |
|--------------------------------------------|-----------|
| **Domain Join Verification**               | screenshots/tsmith.PNG |
| **Time Resync Success**                    | screenshots/resync.PNG |
| **Initial Trust Failure Screenshot**       | https://github.com/Sharon1347/Active-Directory/blob/9c20f6a9f8f801c8744d21c0c5aaa722e6a32be0/screenshots/TRUST-failure.PNG|
| **Successful Direct RDP Connection**       | screenshots/xfreedrp-direct%20connection.PNG |
| **RDP Brute-Force Success (Python Script)** | screenshots/RDP-SUCCESS.PNG |

---

## 🔥 Key Cybersecurity Skills Practiced:
- Active Directory Setup & Management.
- Domain Joining & Network Configuration.
- Brute-force Attack Techniques (Red Teaming).
- Logging & Security Monitoring with Splunk & Sysmon.
- Detection & Response Workflows (Blue Teaming).
- Using Security Tools like Atomic Red Team for Simulation.

---

## 📝 Notes:
- The entire lab was run in a virtualized environment for educational purposes.
- Screenshots and documentation were carefully captured for transparency and reproducibility.
- All machines were isolated in a private network.

---

## ✅ Conclusion:
This project demonstrates a full Active Directory environment build with integrated offensive and defensive cybersecurity practices. It highlights:
- My ability to deploy enterprise-grade security tools.
- My skills in both attacking and defending systems.
- My experience in documenting and explaining technical projects clearly.

---

