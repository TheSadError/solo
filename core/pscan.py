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
        port = 20
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 21
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 22
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 139
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 137
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 445
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 53
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 443
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 80
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 23
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 8080
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 25
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 8443
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
        port = 69
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,port))
        if result ==0:
            version = socket.getservbyport(port, "tcp")
            print(Fore.GREEN+f"\t{port}  \topen  \t{version}")
        s.close()
