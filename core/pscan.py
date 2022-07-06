import socket
from colorama import *


def portscan(url,md):
    if md == "slow":
        print(f"""
    --> Starting Port Scanning...
        Mode : Slow Scan (Full Scan)
        """)
        url = socket.gethostbyname(url)
        print(Fore.BLUE+"\tPort  \tSTATE  \tVersion")
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((url,port))
            if result ==0:
                version = socket.getservbyport(port, "tcp")
                print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
            s.close()
    else:
        print(f"""
    --> Starting Port Scanning...
        Mode : Fast Scan (Spesific Ports)
        """)
        url = socket.gethostbyname(url)
        print(Fore.BLUE+"\tPort  \tSTATE  \tVersion")
        lst = [20,21,22,25,53,69,80,8080,8443,137,139,443,445]
        for port in lst: 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((url,port))
            if result ==0:
                version = socket.getservbyport(port, "tcp")
                print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
            s.close()
