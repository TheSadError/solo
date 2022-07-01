from colorama import *
import os
from time import *
import optparse
import random
import sys
import pscan
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

def start(us,ps):
    if(ps == "True"):
        pscan.portscan(us)

if __name__ == "__main__":
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

{Fore.BLUE}Usage : python3 solo.py --p True --u example.com

    """)
    parser.add_option("--p",dest = "port",type="string",help = "Port scanning parameter")
    parser.add_option("--u",dest = "url",type="string",help = "Target URL")
    (options,args) = parser.parse_args()
    port = options.port
    url = options.url
    if(port == None and url == None):
        print(parser.usage)
        exit(0)
    start(url,port)