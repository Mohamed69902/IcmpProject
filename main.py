from scapy.all import IP
from scapy.all import ICMP
from scapy.all import sr1

while True:
    try:
        src_ip = input("Enter IP Source: ")
        dst_ip = input("Enter Destination IP: ")

        ip_head = IP(src=src_ip,dst=dst_ip)
        icmp = ICMP(id=1000)
        full_packet = ip_head / icmp
        packet_send = sr1(full_packet)
        if packet_send:
            print(packet_send.show())
        retry = input("Do you want to continue?(y/n)")
        if retry == "y":
            continue
        else:
            print("Bye !!")
            break
    except Exception:
        print("Please enter a valid address. ")
        continue