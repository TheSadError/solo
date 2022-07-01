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
urllst = [
    "https://github.com/",
    "https://www.behance.net/",
    "https://www.instagram.com/",
    "https://forums.adobe.com/people/",
    "https://angel.co/u/",
    "http://blackplanet.com/",
    "https://www.canva.com/",
    "https://www.codementor.io/@",
    "https://evewho.com/pilot/",
    "http://www.fanpop.com/",
    "https://fotolog.com/",
    "https://foursquare.com/",
    "https://www.furaffinity.net/user/",
    "https://gpodder.net/user/",
    "https://www.investing.com/traders",
    "https://www.khanacademy.org/profile/",
    "https://kiwifarms.net/members/?username=",
    "https://forum.redsun.tf/members/?username=",
    "https://creativemarket.com/users/",
    "http://pedsovet.su/index/8-0-",
    "https://radioskot.ru/index/8-0-",
    "https://coderwall.com/",
    "https://tamtam.chat/",
    "https://www.zomato.com/pl/",
    "https://mixer.com/",
    "https://world.kano.me/",
    "https://yandex.ru/collections/user/",
    "https://www.paypal.com/paypalme/",
    "https://imageshack.us/user/",
    "https://www.crunchyroll.com/user/",
    "https://support.t-mobile.com/people/"
    ]
def oscan(us):
    print(Fore.RED+"""
    Normal Scan! Mode : Normal Web
    """)
    for i in range(0,len(urllst)):
        req = requests.get(urllst[i]+us)
        if(req.status_code == 200):
            print(Fore.GREEN+f"User Found ! URL : {urllst[i]}{us}")
        else:
            print(Fore.RED+f"User Not Found! URL : {urllst[i]}{us}")
    
    print(Fore.RED+"""
    Normal Scan! Mode : Dorking (DataBases)
    """)
