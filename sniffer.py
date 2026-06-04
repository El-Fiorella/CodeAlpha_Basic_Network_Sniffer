from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        
        # Determine the protocol name
        protocol_name = "Unknown"
        if packet.haslayer(TCP):
            protocol_name = "TCP"
        elif packet.haslayer(UDP):
            protocol_name = "UDP"
        elif packet.haslayer(ICMP):
            protocol_name = "ICMP"
            
        print(f"\n[+] New Packet: {src_ip} -> {dst_ip} | Protocol: {protocol_name}")
        
        # Check for and display payload data
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = packet.lastlayer().payload
            if len(payload) > 0:
                print(f"    Payload (Preview): {bytes(payload)[:50]}")
            else:
                print("    Payload: [Empty]")

def main():
    print("=" * 60)
    print(" 📡 Starting Basic Python Network Sniffer... ")
    print(" Press Ctrl+C to stop capturing. ")
    print("=" * 60)
    
    # Capture packets continuously without storing them heavily in memory
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()