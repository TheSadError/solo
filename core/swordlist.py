from colorama import *
from time import *
import itertools 
import string    
import time      

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


def gen(st,et,nm):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '1'+'2'+'3'+'4'+'5'+'6'+'7'+'8'+'9'+'0'+'@'+'£'+'!'+'<'+'>'+'.'+'*'+'-'+'+'+'?'+'{'+'}'+'['+']'+'='+'|'
    attempts = 0
    f = open(nm,'a')
    for password_length in range(st, et):
        for guess in itertools.product(chars,repeat=password_length): 
            attempts += 1
            guess = ''.join(guess)
            f.write(guess) 
            f.write("\n")
            print(guess, attempts)      
    f.close()
def create(option):

    st = 6
    et = 15
    nm = "wordlist-output.txt"
    start_time = time.time()
    gen(st,et,nm)
    end_time = time.time()
    print(end_time-start_time)
