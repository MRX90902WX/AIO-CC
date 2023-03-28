import requests
import json
from os import system
print("")
system("clear")

def get_info():
                        print("  \033[1;34m__________  _______ _____________ _________")
                        print(" / ___/ ___/ / ___/ // / __/ ___/ //_/ __/ _ \ ")
                        print("/ /__/ /__  / /__/ _  / _// /__/ ,< / _// , _/")
                        print("\___/\___/  \___/_//_/___/\___/_/|_/___/_/|_|")
                        print("\033[1;37m----------------------------------------------")
                        print(" \033[1;34mAUTHOR  : \033[1;37mDEMO")
                        print(" \033[1;34mVERSION : \033[1;37m1.9")
                        print(" \033[1;34mSCRIPT  : \033[1;37mCREDIT CARD CHECKER")
                        print("\033[1;37m----------------------------------------------")
                        ccbin = input( "\033[1;34m[\033[1;37m?\033[1;34m]\033[1;37m Bins o CC: ")
                        print("")
                        r = requests.get("https://bin-checker.net/api/" + ccbin)                                                             
                        json = r.json()
                        print("\033[1;34m[\033[1;37m+\033[1;34m] \033[1;34mCC o Bin : \033[1;37m" + str(ccbin))
                        print("\033[1;34m[\033[1;37m+\033[1;34m] \033[1;34mMARCA    :\033[1;37m", json["scheme"])
                        print("\033[1;34m[\033[1;37m+\033[1;34m] \033[1;34mTIPO     :\033[1;37m", json["type"])
                        print("\033[1;34m[\033[1;37m+\033[1;34m] \033[1;34mNIVEL    :\033[1;37m", json["level"])
                        country = json["country"]
                        pais = country["name"]
                        codigo = country["code"]
                        print("\033[1;34m[\033[1;37m+\033[1;34m] \033[1;34mPAIS     :\033[1;37m", pais)
                        print("\033[1;34m[\033[1;37m+\033[1;34m] \033[1;34mCODIGO   :\033[1;37m", codigo)
                        bank = json["bank"]
                        nombre = bank["name"]
                        sitioweb = bank["website"]
                        numero = bank["phone"]
                        print("\033[1;34m[\033[1;37m+\033[1;34m] \033[1;34mBANCO    :\033[1;37m", nombre)
                        print("\033[1;34m[\033[1;37m+\033[1;34m] \033[1;34mPAGE WEB :\033[1;37m", sitioweb)
                        print("\033[1;34m[\033[1;37m+\033[1;34m] \033[1;34mN° BANCO :\033[1;37m", numero)
                        todo = str("CC: " + str(ccbin +
                                " \nMARCA: " + json["scheme"] +
                                " \nTIPO: " + json["type"] +
                                " \nNIVEL: " + json["level"] +
                                " \nNOMBRE PAIS: " + pais +
                                " \nCODIGO PAIS: " + codigo +
                                " \nNOMBRE BANCO: " + nombre +
                                " \nSITIO WEB BANCO: " + sitioweb +
                                " \nNUMERO BANCO: " + numero +
                                " \nººººººººººººººººººººººººººººººººººº"))
                        print( " ºººººººººººººººººººººººººººººººººº")      

get_info()

print("")
volver = input(" \033[1;34m[\033[1;37m☆\033[1;34m]\033[1;37mContinuar info de un bin \033[1;34msi/no: \033[1;37m")

if volver == "si":
         system("python.info.py")
else:
         exit()
