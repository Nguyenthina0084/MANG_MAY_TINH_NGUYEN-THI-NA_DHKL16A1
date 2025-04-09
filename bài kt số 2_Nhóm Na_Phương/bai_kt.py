import pyshark

# Đường dẫn tới file .pcapng bạn đã lưu
cap = pyshark.FileCapture('bai_kt.pcapng')

for pkt in cap:
    print("------ GÓI TIN ------")
    try:
        # Lớp 2 - Ethernet
        print("MAC nguồn:", pkt.eth.src)
        print("MAC đích:", pkt.eth.dst)

        # Lớp 3 - IP
        print("IP nguồn:", pkt.ip.src)
        print("IP đích:", pkt.ip.dst)

    except AttributeError:
        print("Gói tin không phải Ethernet/IP")
