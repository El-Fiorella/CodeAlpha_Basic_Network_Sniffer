# CodeAlpha_Basic_Network_Sniffer 


## 📡 Project Overview
This project is a lightweight Network Sniffer built in Python using the Scapy library. The tool intercepts network packets in real-time, decodes their headers, and extracts critical packet information to analyze how data flows across a network.

## 🚀 Features
- **Real-Time Capture:** Hooks into the network interface to intercept live traffic.
- **Protocol Analysis:** Identifies and parses Layer 3 (IP) and Layer 4 protocols (TCP, UDP, ICMP).
- **Addressing:** Extracts and displays source and destination IP addresses.
- **Payload Inspection:** Extracts and displays raw application-layer data payloads where available.

## 🛠️ Requirements & Installation
This tool is designed to run natively on a Windows host machine using Python 3.

1. **Install Python 3:** Ensure Python 3.x is installed on your system.
   
2. **Install Npcap Driver:** Download and install [Npcap](https://npcap.com/). During installation, ensure you check the box for **"Install Npcap in WinPcap API-compatible Mode"** so Scapy can interact with your network interface.
   
3. **Install Scapy:** Open PowerShell as an Administrator and install the library via pip:
   ```powershell
   pip install scapy


## 🛠️ Run Process Step by step

1. **Open Windows PowerShell or Command Prompt:**  Run as Administrator.
   
2. **Navigate to the directory where your script is saved:**
   ```powershell
   cd $home\Downloads
   
3. **Execute the sniffer script:**
    ```powershell
   python sniffer.py

4. **Test and verify:** Open a separate terminal window and generate network traffic (e.g., run ping 8.8.8.8).




