import requests
import json
from os import system
print("")

def get_info():
   
                        system("setterm -foreground blue")
                        system("bash check")
                        print("")
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
print(" \033[1;33mDesea continuar usando el programa \033[1;37msi/no")
volver = input(" \033[1;37m>>> ")

if volver == "si":                                                                      
         system("python AIO_CC.py")
else:                        
         exit()
