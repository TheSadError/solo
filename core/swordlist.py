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
class options : 
    name = "name"
    username = "username"
    birthyear = 0
    momname = "mom"
    fathername = "father"
    hobby = "luckynumber"
    wordlistl = "wr"
    pet = "pet"
    
def create(option):
    options.name = input(Fore.BLUE+"[+] Input victim name : ")
    options.username = input(Fore.BLUE+"[+] Input victim username : ")
    options.birthyear = input(Fore.BLUE+"[+] Input victim birth year : ")
    options.momname = input(Fore.BLUE+"[+] Input victim mom name: ")
    options.fathername = input(Fore.BLUE+"[+] Input victim father name : ")
    options.hobby = input(Fore.BLUE+"[+] Input victim hobby: ")
    options.pet = input(Fore.BLUE+"[+] Input victim pet name : ")
    options.wordlistl = input(Fore.GREEN+"[!] Input wordlist length : ")
