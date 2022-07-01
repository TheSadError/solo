import requests
import socket
from colorama import *
from time import *

def progress(percent=0, width=40):
    left = width * percent // 100
    right = width - left
    tags = "█" * left
    spaces = " " * right
    percents = f"{percent:.0f}%"
    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)

def load():
    for i in range(101):
        progress(i)
        sleep(0.01)
urllst = ["https://github.com/","https://www.behance.net/","https://www.instagram.com/","https://forums.adobe.com/people/","https://angel.co/u/","http://blackplanet.com/","https://www.canva.com/","https://www.codementor.io/@","https://evewho.com/pilot/","http://www.fanpop.com/"]

def oscan(us):
    for i in range(0,len(urllst)):
        req = requests.get(urllst[i]+us)
        if(req.status_code == 200):
            try : 
                print(Fore.GREEN+f"User Found ! {urllst[i]}{us}")
            except:
                print(Fore.RED+"Some Error Occured!")

oscan("TheSadError")