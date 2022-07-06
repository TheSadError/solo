from colorama import *
import os
from time import *
import optparse
import random
import sys
import core.pscan as pscan
import core.oscan as oscan
import core.swordlist as swordlist
import datetime

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

def start(us,ps,os,wr,md):
    if(ps == "true"):
        pscan.portscan(us,md)
    if(os == "true"):
        oscan.oscan(us)
    if(wr == "start" or wr == "true"):
        swordlist.create()
        
if __name__ == "__main__":
    e = datetime.datetime.now()
    parser = optparse.OptionParser(Fore.BLUE+f"""
{Fore.BLUE} _______  _______  ___      _______ 
{Fore.BLUE}|       ||       ||   |    |       |
{Fore.BLUE}|  _____||   _   ||   |    |   _   |
{Fore.RED}| |_____ |  | |  ||   |    |  | |  |
{Fore.RED}|_____  ||  |_|  ||   |___ |  |_|  |
{Fore.GREEN} ____|  ||       ||       ||       |
{Fore.GREEN}|_______||_______||_______||_______|

                        {Fore.RED} Coded By @thesaderror 
                        {Fore.GREEN} Github: TheSadError

{Fore.BLUE}Usage (Port Scan)  : python3 solo.py --p true --u example.com
                --> slow mode full scan: python3 solo.py --p true --m slow --u example.com
                --> fast mode vuln port : python3 solo.py --p true --m fast --u example.com
{Fore.BLUE}Usage (OSINT Scan) : python3 solo.py --o true --u username
{Fore.BLUE}Usage (Create Wordlist) : python3 solo.py --w start 

    """)
    parser.add_option("--p","--port",dest = "port",type="string",help = "Port scanning parameter")
    parser.add_option("--u","--U",dest = "url",type="string",help = "Target URL , Username Usage : --u TheSadError , --u thesaderror.com")
    parser.add_option("--o","--osint",dest = "osint",type="string",help = "Osint Option Usage : --o true")
    parser.add_option("--w","--word",dest = "wordlist",type="string",help = "Create big wordlist option : --w start")
    parser.add_option("--m","--mode",dest = "mode",type="string",help = "Full scan mode : --m fast , --m slow (fast = fast scan for port scan and slow == full port scan 65535)")
    (options,args) = parser.parse_args()
    port = options.port
    url = options.url
    osint = options.osint
    wordlist = options.wordlist
    mode = options.mode
    print("Starting solo scanner 2.3 ( https://github.com/TheSadError/solo ) at %s" % e)
    if(url == None and port == None and osint == None and wordlist == None ):
        print(parser.usage)
        exit(0)
    start(url,port,osint,wordlist,mode)
