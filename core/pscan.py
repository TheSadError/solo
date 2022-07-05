import socket
from colorama import *


def portscan(url):
    print(f"""
--> Starting Port Scanning...
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
