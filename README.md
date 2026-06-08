# CodeAlpha_Basic_Network_Sniffer 


## 📡 Project Overview
[cite_start]This project is a lightweight Network Sniffer built in Python using the Scapy library as part of the CodeAlpha Cybersecurity Internship[cite: 1, 22]. [cite_start]The tool intercepts network packets in real-time, decodes their headers, and extracts critical packet information to analyze how data flows across a network.

## 🚀 Features
- [cite_start]**Real-Time Capture:** Hooks into the network interface to intercept live traffic[cite: 23].
- [cite_start]**Protocol Analysis:** Identifies and parses Layer 3 (IP) and Layer 4 protocols (TCP, UDP, ICMP)[cite: 24, 26].
- [cite_start]**Addressing:** Extracts and displays source and destination IP addresses[cite: 26].
- [cite_start]**Payload Inspection:** Extracts and displays raw application-layer data payloads where available[cite: 26].

## 🛠️ Requirements & Installation
This tool is designed to run natively on a Windows host machine using Python 3.

1. **Install Python 3:** Ensure Python 3.x is installed on your system.
2. **Install Npcap Driver:** Download and install [Npcap](https://npcap.com/). During installation, ensure you check the box for **"Install Npcap in WinPcap API-compatible Mode"** so Scapy can interact with your network interface.
3. **Install Scapy:** Open PowerShell as an Administrator and install the library via pip:
   ```powershell
   pip install scapy

## 🛠️ Run Process step by step

1. **Open Windows PowerShell or Command Prompt:**  Run as Administrator.
2. **Navigate to the directory where your script is saved:**  ```cd $home\Downloads``` 
4. **Execute the sniffer script:** ```python sniffer.py```
5. **Test and verify:** Open a separate terminal window and generate network traffic (e.g., run ping 8.8.8.8).


