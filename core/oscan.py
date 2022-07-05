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
    "https://www.crunchyroll.com/user/",
    "https://support.t-mobile.com/people/",
    "https://about.me/",
    "https://independent.academia.edu/",
    "https://airbit.com/",
    "https://www.alik.cz/u/",
    "https://allmylinks.com/",
    "https://anilist.co/user/",
    "https://developer.apple.com/forums/profile/",
    "https://discussions.apple.com/profile/",
    "https://www.artstation.com/",
    "https://asciinema.org/~",
    "https://ask.fedoraproject.org/u/",
    "https://ask.fm/",
    "https://audiojungle.net/user/",
    "https://www.autofrage.net/nutzer/",
    "https://www.avizo.cz/",
    "https://www.bazar.cz/",
    "https://bezuzyteczna.pl/uzytkownicy/",
    "https://binarysearch.io/@/",
    "https://forum.dangerousthings.com/u/",
    "https://bitbucket.org/",
    "https://bitcoinforum.com/profile/",
    "https://gitlab.com/",
    "https://www.goodreads.com/",
    "https://plugins.gradle.org/u/",
    "https://www.grailed.com/",
    "http://en.gravatar.com/",
    "https://forums.gunsandammo.com/profile/",
    "https://www.gutefrage.net/nutzer/",
    "https://hackaday.io/",
    "https://hackerearth.com/@",
    "https://news.ycombinator.com/user?id="
]
domainlst = [
    ".cf",
    ".github.io",
    ".com",
    ".cf",
    ".tl",
    ".ml",
    ".tr",
    ".en",
    ".az",
    ".org",
    ".net",
    ".live",
    ".pol",
    ".wix.com",
    ".blogspot.com",
    ".dev",
    ".xyz",
    ".download",
    ".itch.io",
]
def oscan(us):
    print(f"""
--> OSINT SCAN

    Username : {us}
    Websites : {len(urllst)} 
    """)
    print(Fore.BLUE+"""
    --> Normal Scan! Mode : Normal Web
    """)
    for i in range(0,len(urllst)):
        req = requests.get(urllst[i]+us)
        if(req.status_code == 200):
            try : 
                print(Fore.GREEN+f"{[i]} User Found! URL : {urllst[i]}{us}")
            except:
                print("[-] WARNING : Please connect Internet! ")
        else:
            print(Fore.RED+f"{[i]} User Not Found! URL : {urllst[i]}{us}")
    print(" ")
