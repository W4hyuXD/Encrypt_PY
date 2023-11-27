# © Created By Pahrul
# Author WahyuuXD
# github : WahyuuXD
# my instagram : why.404_
# my facebook : w4hyu.404


# <!-- Import Module --->
import os, sys, requests, fbthon, random, json, webbrowser
from fbthon import CreateAccount
from fake_email import Email
from pytube import YouTube as yutub
from os import system as _
import os, sys, requests, bs4, re, time, datetime, urllib, random, json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bs
from rich import print as cetak
from rich.panel import Panel as panel
from rich.console import Console
from rich.panel import Panel
from time import sleep as s
import requests, sys, os, time, random
from gtts import gTTS
os.system("clear")

# <!-- Text Berjalan --->

#def mengetik(s):
#    for c in s + '\n':
#        sys.stdout.write(c)
#        sys.stdout.flush()
        # kecepatan mengetik
#        time.sleep(0.1)
#mengetik("")
#mengetik("")
#mengetik("          Hello User!\n          Udah Follow Instagram Mimin Belum Nih?\n          Kalo Belum Follow Dulu Yah^_^\n\n          MyInsta: why.404_\n          Terimakasih.")
# <!-- open browser --->
#webbrowser.open("https://www.instagram.com/why.404_")
#time.sleep(2)
#os.system("clear")

# <!-- Module --->
mail = Email().Mail()
x = (mail["mail"])

try:
        import fbthon, pytube, fake_email, rich
except ImportError:
        os.system('pip install fbthon')
        os.system("pip install pytube")
        os.system("pip install fake-email")
        os.system('pip install rich')
        
# <!-- Banner --->
def logo():
	cetak(panel(f"""[bold purple] 
    [bold white]Multi[bold purple]
    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
       ██║   ██║   ██║██║   ██║██║     ███████╗
       ██║   ██║   ██║██║   ██║██║     ╚════██║
       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                [bold white]© Created 2023
""",width=90,padding=(0,8),title=f"[bold white]>>> Version 1.0 <<<",subtitle=f"[bold white]>>> Multi Tools <<<",style=f"bold red"))


# <!-- Menu --->
def masuk():
	os.system("clear")
	logo()
	cetak(panel(f"[bold white][[bold red]01[bold white]] Bot Share [bold purple]     (ASFU) [bold white]      [[bold red]02[bold white]] Download Video YouTube [bold green]ON\n[bold white][[bold red]03[bold white]] Bot Share V2    [bold green] ON         [bold white][[bold red]04[bold white]] Bot Share V3[bold green]           ON\n[bold white][[bold red]05[bold white]] Profile Guardian [bold green]ON         [bold white][[bold red]06[bold white]] Bot Komen FB[bold green]           ON\n[bold white][[bold red]07[bold white]] Bot Chat Simi [bold green]   ON[bold white]         [[bold red]08[bold white]] Follow Facebook[bold red]        OFF\n[bold white][[bold red]09[bold white]] Crack Facebook[bold red]   OFF[bold white]        [[bold red]10[bold white]] Create Facebook Acc[bold green]    ON",width=90,title=f"[bold white]>>> Menu <<<",style=f"bold red"))
	cetak(panel(f"[bold white]                Ketik tools Untuk Masuk Ke Tools Lainnya",width=90,title=f"[bold white]>>> Info <<<",style=f"bold red"))
	tanya = input ("\n\033[1;87m[×] Pilih : ")
	if tanya =="":
		exit()
	elif tanya =="1" or tanya =="01":
		tools_1()
	elif tanya =="2" or tanya =="02":
		download()
	elif tanya =="3" or tanya =="03":
		tools_3()
	elif tanya =="4" or tanya =="04":
		tools_4()
	elif tanya =="5" or tanya =="05":
		guard()
	elif tanya =="6" or tanya =="06":
		tools_6()
	elif tanya =="7" or tanya =="07":
		bot()
	elif tanya =="8" or tanya =="08":
		tools_8()
	elif tanya =="9" or tanya =="09":
		tools_9()
	elif tanya =="10" or tanya =="10":
		tools_10()
	elif tanya =="tools":
		tools()
	else:
		exit()
		
		
# <!-- Menu Tambahan --->
def tools():
	os.system("clear")
	logo()
	cetak(panel(f"[bold white][[bold red]01[bold white]] Lacak Nomor Telepon [bold white]                  [[bold red]02[bold white]] Lacak IP Address ",width=90,style=f"bold red"))
	tanya = input ("\033[1;97m\n[×] Pilih : ")
	if tanya =="":
		exit()
	elif tanya =="1" or tanya =="01":
		tools_5()
	elif tanya =="2" or tanya =="02":
		tools_2()
	else:
		exit()
		

# <!-- YT Downloader --->
def download():
	link = input ("\n\033[1;87m- Url Vidio : ")
	yt = yutub(link)
	print("\n- Judul Vidio : ",yt.title)
	print("- ID Vidio :",yt.video_id)
	print("- Durasi Vidio : ",yt.length)
	print("- Viewer Vidio :",yt.views)
	print("- Rating Vidio :",yt.rating)
	print("- Batasan Usia : ",yt.age_restricted)
	print("\n1. Download Vidio Resolusi Tinggi")
	print("2. Download Vidio Resolusi Rendah")
	tanya = input ("\n- Pilih : ")
	if tanya =="":
		exit()
	elif tanya == "1" or tanya =="01":
		print(_("pytube {} -t /sdcard --itag=22".format(link)))
	elif tanya =="02" or tanya =="02":
		print(_("pytube {} -t /sdcard --itag=18".format(link)))
	else:
		exit()
		

# <!-- Profile Guardian --->
def guard():
	cookie = input ("\n- Masukkan Cookie Akun : ")
	token = input ("- Masukan Token Akun : ")
	open('cookie.txt','w').write(cookie)
	open('token.txt','w').write(token)
	print("\n1. Akktifkan Profile Guardian ")
	print("2. Nonaktifkan Profile Guardian")
	print("0. Log Out ")
	
	tanya = input ("\n- Pilih : ")
	if tanya == "":
		print ("\n- Ngetik Yang Bener Dong Bangsat !!!")
		exit()
	elif tanya =="1" or tanya =="01":
		scrap1(True)
	elif tanya =="2" or tanya =="02":
		scrap1(False)
	elif tanya =="0" or tanya =="00":
		exit()
	else:
		print ("\n- Ngetik Yang Bener Dong Bangsat !!!")
		exit()
		

		
	
# <!-- Get ID Facebook --->
def get_id():
	token = open("token.txt","r").read()
	cok = open("cookie.txt","r").read()
	cookie = {"cookie":cok}
	id = requests.get("https://graph.facebook.com/me/?access_token=%s"%(token),cookies={"cookie":cok}).json()["id"]	    
	return (id)
	

def scrap1(stat):
	token = open("token.txt","r").read()
	cok = open("cookie.txt","r").read()
	cookie = {"cookie":cok}
	id   = get_id()
	
	
	
	var  = {
            '0': {
                'is_shielded'        : stat,
                'session_id'         : '9b78191c-84fd-4ab6-b0aa-19b39f04a6bc',
                'actor_id'           : str(id),
                'client_mutation_id' : 'b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0'}}
	
	data = {
            'variables'                : json.dumps(var),
            'method'                   : 'post',
            'doc_id'                   : '1477043292367183',
            'query_name'               : 'IsShieldedSetMutation',
            'strip_defaults'           : 'true',
            'strip_nulls'              : 'true',
            'locale'                   : 'en_US',
            'client_country_code'      : 'US',
            'fb_api_req_friendly_name' : 'IsShieldedSetMutation',
            'fb_api_caller_class'      : 'IsShieldedSetMutation'}
            
	
	head = {
            'Content-Type'  : 'application/x-www-form-urlencoded',
            'Authorization' : 'OAuth %s'%token}
     
	url  = 'https://graph.facebook.com/graphql'
	req  = requests.post(url, data=data, headers=head, cookies=cookie)
	if '"is_shielded":true' in req.text:
		print("\n- Berhasil Mengaktifkan Profile Guard")
		exit()
	elif '"is_shielded":false' in req.text:
		print("\n- Berhasil Menonaktifkan Profile Guard")
		exit()
		
		
# <!-- unliShare --->
def tools_1():
	os.system("pkg update -y && pkg upgrade -y")
	os.system("pkg i -y python python3 play-audio")
	os.system("pkg install git")
	os.system("pip install requests")
	os.system("git clone https://github.com/WahyuuXD/unliShare")
	os.chdir("unliShare")
	os.system("git pull")
	os.system("python3 run.py")
	
# <!-- Lacak IP (Menu Tambahan) --->
def tools_2():
	target = input ("\n\033[1;97m- Masukkan IP Target : ")
	data = requests.get (f"http://ip-api.com/json/{target}").json()
	print("\n- Country :",data["country"])
	print("- CountryCode :",data["countryCode"])
	print("- Region :",data["region"])
	print("- RegionName :",data["regionName"])
	print("- City : ",data["city"])
	print("- Lat :",data["lat"])
	print("- Lon :",data["lon"])
	print("- TimeZone :",data["timezone"])
	print("- ISP :",data["isp"])
	print("- AS :",data["as"])
	print("- Query :",data["query"])
	print("")
	
# <!-- Simple Share --->
def tools_3():
	os.system("pkg update -y && pkg upgrade -y")
	os.system("pkg install python")
	os.system("pkg install git")
	os.system("pip install requests")
	os.system("git clone https://github.com/WahyuuXD/SSF")
	os.chdir("SSF")
	os.system("git pull")
	os.system("python main.py")
	
# <!-- Share V2 --->
def tools_4():
	os.system("pkg update -y && pkg upgrade -y")
	os.system("pkg install python")
	os.system("pkg install git")
	os.system("pip install requests")
	os.system("git clone https://github.com/WahyuuXD/ShareV3")
	os.chdir("SSF")
	os.system("git pull")
	os.system("python run.py")
	
# <!-- Lacak Nomor (Menu Tambahan) --->
def tools_5():
	number =  input ("\n\033[1;97m- Masukkan Nomor Telepon : ")
	output = requests.get(f'http://phone-number-api.com/json/?number={number}').text
	data = json.loads(output)
	print("\n- Query :",data["query"])
	print("- NumberCountryCode :",data["numberCountryCode"])
	print("- FormatE164 :",data["formatE164"])
	print("- FormatNational :",data["formatNational"])
	print("- FormatInternational :",data["formatInternational"])
	print("- dialFromCountryCode :",data["dialFromCountryCode"])
	print("- Carrier :",data["carrier"])
	print("- Continent :",data["continent"])
	print("- ContinentCode :",data["continentCode"])
	print("- Country :",data["country"])
	print("- CountryName :",data["countryName"])
	print("- Lat :",data["lat"])
	print("- Lon :",data["lon"])
	print("- TimeZone :",data["timezone"])
	print("- Currency :",data["currency"])
	print("")
	
	
	
	
# <!-- Komen FB --->
def tools_6():
	os.system("pkg update -y && pkg upgrade -y")
	os.system("pkg install python")
	os.system("pkg install git")
	os.system("pip install requests")
	os.system("git clone https://github.com/WahyuuXD/Comments")
	os.chdir("Comments")
	os.system("git pull")
	os.system("python run.py")
	

	
# <!-- Encrypt --->
def tools_8():
    os.system('clear')
    print("")
    print("")
    print("")
    print("Maaf Fitur Ini Belum Tersedia (Dalam Masa Pengembangan)")
    print("Tunggu Update Selanjutnya Dari Kami")
    print("")
    print("")
    print("Untuk Update Selanjutnya Bisa Cek Di Sosial Media Saya")
    print("Facebook : Wahyuu (w4hyu.404)")
    print("Instagran: why.404_")
    print("Github   : WahyuuXD")
    print("Jangan Lupa Follow Yah:) Enjoy(^_^)")
    print("")
    print("Saya WahyuDin Ambia, Terimakasih :)")
    exit()
# 	os.system("pkg update && pkg upgrade")
# 	os.system("pkg install python2")
# 	os.system("pkg install git")
# 	os.system("pip install requests")
# 	os.system("git clone https://github.com/P4HRUL/PYENC")
# 	os.chdir("PYENC")
# 	os.system("git pull")
# 	os.system("python2 PYENC.py")
	
# <!-- Crack Facebook (MBF) --->
def tools_9():
    os.system("clear")
    print("")
    print("")
    print("Maaf Fitur Ini Belum Tersedia (Dalam Tahap Pengembangan)")
    print("Tunggu Update Selanjutnya Dari Kami")
    print("")
    print("")
    print("Untuk Update Selanjutnya Bisa Cek Di Akun Media Sosial Saya")
    print("Facebook : w4hyu.404")
    print("Instagram: why.404_")
    print("Github   : WahyuuXD")
    print("Jangan Lupa Follow Yah :). Enjoy (^_^)")
    print("")
    print("Saya WahyuDin Ambia, Terimakasih :)")
    exit()
#    os.system("pkg update -y && pkg upgrade -y")
#    os.system("pkg install python")
#    os.system("pkg install git")
#    os.system("pip install requests")
#	os.system("git clone https://github.com/WhyuXD/fb")
#	os.chdir("fb")
#	os.system("git pull")
#	os.system("python run.py")
	

# <!-- Create Facebook Account --->
def tools_10():
	firstname = input ("\n- Nama Depan : ")
	lastname = input ("- Nama Belakang : ")
	email = (x)
	ultah = "01/01/2000"
	gender = input ("- Jenis Kelamin ( Male/Female ) : ")
	password = input ("- Password : ")
	print("")
	new_account = CreateAccount(firstname = firstname, lastname = lastname, email = email, gender = gender, date_of_birth = ultah, password = password)
	
	while True:
		mess=Email(mail["session"]).inbox()
		if mess:
			c =mess['topic'].split(' ')[0].replace("FB-","")
			break
		
	kode = (c)
	konfir = new_account.confirm_account(kode)
	 
	if konfir:
		print ("\033[1;97m- STATUS : \033[1;92mBERHASIL\033[1;97m")
		print ("\033[1;97m- Nama Akun : %s %s" % (firstname,lastname))
		print ("\033[1;97m- ID : %s" % (new_account.get_cookie_dict()['c_user']))
		print ("\033[1;97m- Email : %s" % (email))
		print ("\033[1;97m- Jenis Kelamin : %s" % (gender))
		print ("\033[1;97m- TTL : %s" % (ultah))
		print ("\033[1;97m- Password : %s" % (password))
		ip = requests.get("https://api.ipify.org").text
		print ("\033[1;97m- IP :\033[1;92m",ip)
		print ("\033[1;97m- Cookie Akun : %s" % (new_account.get_cookie_str()))
		print ("\033[1;97m- Token Akun : %s" % (new_account.get_token()))
		exit()
	else:
		print("\033[1;97m- STATUS : \0331;91mGAGAL !")
		exit()
		
def proccess():
    for i in list("\|/-"):
        print(f"\r\033[0;97m[\033[0;92m{i}\033[0;97m] Simi is typing...",end="")
        time.sleep(0.5)

def bot():
        os.system('clear')
        while True:
                print(f"\n")
                pesan = input(f'     \033[1;90mKetik Pesan\r \033[1;91m>\033[1;92m ')
                print('\033[4A');Console().print(Panel('[white]'+pesan, style='yellow'), justify='right')
                if pesan in ["stop","Stop"]:exit()
                print(f"\n");proccess()
                simi = requests.get(f'https://api.simsimi.net/v2/?text={pesan}&lc=id&cf=false')
                balasan_simi = simi.json().get('success')
                tts = gTTS(balasan_simi)
                tts.save('hello.mp3')
                print('\033[3A');Console().print(Panel('[white]'+balasan_simi, style='purple'), justify='left')
                os.system("play-audio hello.mp3")
                
      
      
      
      
      
      
masuk()
		
		
		
		
		


