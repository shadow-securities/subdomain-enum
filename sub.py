
cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m' 

        

if __name__=="__main__":
    print(cyan+"""
    
 .d8888. db    db d8888b.   d88888b d8b   db db    db .88b  d88. 
88'  YP 88    88 88  `8D   88'     888o  88 88    88 88'YbdP`88 
`8bo.   88    88 88oooY'   88ooooo 88V8o 88 88    88 88  88  88 
  `Y8b. 88    88 88~~~b.   88~~~~~ 88 V8o88 88    88 88  88  88 
db   8D 88b  d88 88   8D   88.     88  V888 88b  d88 88  88  88 
`8888Y' ~Y8888P' Y8888P'   Y88888P VP   V8P ~Y8888P' YP  YP  YP 
                                                                
                                                                
    """)
    print(Y+" Created By : JAYASURYAPAL G")
    print(Y+" Github profile: https://github.com/shadow-securities")


import requests
import json
R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 
def fuzz():
    dom=input("Enter Domain >> ")
    url="https://sonar.omnisint.io/subdomains/"+dom
    r=requests.get(url)
    print(C+"Enumerating Subdomains ^-^ .....")
    for i in r.json():
        print(i)
    print(G+"Subdomain Enumeration Success")
    
if __name__=="__main__":
    fuzz()
