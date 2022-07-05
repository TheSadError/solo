from colorama import *
import os
from time import *
import optparse
import random
import sys
import core.pscan as pscan
import core.oscan as oscan
import core.swordlist as swordlist
import core.dork as dork
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

def start(us,ps,os,wr,dr):
    if(ps == "true"):
        pscan.portscan(us)
    if(os == "true"):
        oscan.oscan(us)
    if(wr == "start"):
        swordlist.create(wr)
    dork.ls(dr)
        
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
{Fore.BLUE}Usage (OSINT Scan) : python3 solo.py --o true --u username

    """)
    parser.add_option("--p","--port",dest = "port",type="string",help = "Port scanning parameter")
    parser.add_option("--u","--U",dest = "url",type="string",help = "Target URL , Username Usage : --u TheSadError , --u thesaderror.com")
    parser.add_option("--o","--osint",dest = "osint",type="string",help = "Osint Option Usage : --o true")
    parser.add_option("--w","--word",dest = "wordlist",type="string",help = "Create big wordlist option : --w start")
    parser.add_option("--d","--dork",dest = "dork",type="int",help = "List vulnerable websites list for hack easly by google dorking : --d number of websites to list ")
    (options,args) = parser.parse_args()
    port = options.port
    url = options.url
    osint = options.osint
    wordlist = options.wordlist
    dork = options.dork
    print("Starting solo scanner 2.3 ( https://github.com/TheSadError/solo ) at %s" % e)
    if(url == None and port == None and osint == None and wordlist == None and dork == None):
        print(parser.usage)
        exit(0)
    start(url,port,osint,wordlist,dork)
