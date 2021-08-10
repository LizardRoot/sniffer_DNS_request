import scapy.all as scapy

def sniff(interface):
	scapy.sniff(iface = interface, store = False, prn = packet_detail)

def packet_detail(packet):
	if packet.haslayer(scapy.DNSRR):
		print(packet[scapy.DNSQR].qname)

sniff('enx3c18a011e9bc')