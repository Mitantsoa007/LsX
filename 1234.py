import os
import time
import random
import string
import requests
import sys
import subprocess
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

# Insère ici ton SID de compte Twilio
account_sid = "AC720ff1e111cfdf12170972cdf5161f19"

# Insère ici ton token d'authentification Twilio
auth_token = "4bdde3c7aefe37555d6fcf706b3c297f"

# Insère ici ton numéro Twilio
twilio_number = "+261389116928"

# Insère ici ton numéro WhatsApp
whatsapp_number = "+261345514003"

# Crée un client Twilio
client = Client(account_sid, auth_token)

def generate_approval_key():
    # Génère une clé d'approbation aléatoire
    return ''.join(random.choices(string.ascii_letters + string.digits, k=30))

def send_whatsapp_message(message):
    # Envoie un message WhatsApp
    try:
        message = client.messages.create(
            body=message,
            from_='whatsapp:' + twilio_number,
            to='whatsapp:' + whatsapp_number
        )
        print("Message sent successfully!")
    except Exception as e:
        print("An error occurred while sending the message:", e)

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
    
    lp = input(f'{oo
