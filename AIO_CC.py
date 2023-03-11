import random
import os
import requests
import json


num = int()
cantidad = int()
threads = int()
class Aio():
	global num
	global cantidad
	global threads

	def bin_gen():
		print("""
\033[1;32m ____ _____ _   _    _____ ______ _   _ 
\033[1;32m|  _ \_   _| \ | |  / ____|  ____| \ | |
\033[1;32m| |_) || | |  \| | | |  __| |__  |  \| |
\033[1;32m|  _ < | | | . ` | | | |_ |  __| | . ` |
\033[1;32m| |_) || |_| |\  | | |__| | |____| |\  |
\033[1;32m|____/_____|_| \_|  \_____|______|_| \_|
                                        
			""")
		aumentando = 1
		cantidad = int(input("Cuantas BIN'S te gustaria generar: "))
		while aumentando <= cantidad:
			generador = str(random.randint(2,6)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) +  str(random.randint(0,9)) + str(random.randint(0,9))
			bingen = generador + "xxxxxxxxxx"
			print(bingen)
			aumentando += 1
			print(bingen, file=open("BINSGen.txt", "a+"))

		print("\033[1;33mDesea continuar usando el programa \033[1;37msi/no")
		volver = input("\033[1;37m>>> ").lower()
		if volver == "si":
			return Aio.modules()
		else:
			print("\033[1;37mCerrando . . .")


	def cc_gen_random():
		print("""
\033[1;32m  _____ _____    _____ ______ _   _  
\033[1;32m / ____/ ____|  / ____|  ____| \ | | 
\033[1;32m| |   | |      | |  __| |__  |  \| | 
\033[1;32m| |   | |      | | |_ |  __| | . ` | 
\033[1;32m| |___| |____  | |__| | |____| |\  |
\033[1;32m \_____\_____|  \_____|______|_| \_| 
                                                           

			""")
		aumentando = 1
		cantidad = int(input("Cuantas CC'S te gustaria generar: "))
		while aumentando <= cantidad:
			generador = str(random.randint(2,6)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) +  str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#
			cvv = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			dia = str(random.randint(0,30))
			mes = str(random.randint(1,12))
			año = str(20) + str(random.randint(21,30))
			fecha_exp = dia + "/" + mes + "/" + año
			save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"

			separar, separar1, separar2, separar3, separar4, separar5 = generador[0], generador[1], generador[3], generador[4], generador[5], generador[6]
			separadores_dos = separar + separar1
			separadores_tres = separar + separar1 + separar2 
			separadores_cuatro = separar + separar1 + separar2 + separar3
			separadores_cinco = separar + separar1 + separar2 + separar3 + separar4
			separadores_seis = separar + separar1 + separar2 + separar3 + separar4 + separar5
			entero_dos = int(separadores_dos)
			entero_tres = int(separadores_tres)
			entero_cuatro = int(separadores_cuatro)
			entero_cinco =  int(separadores_cinco)
			entero_seis =+ int(separadores_seis)

			if separadores_dos == "34" or separadores_dos == "37":
				generador += str(random.randint(0,9))
				aumentando += 1
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)
			###############################################################
			elif separadores_dos == "62":
				a = random.randint(1, 4)
				if a == 1:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)
				elif a == 2:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)	
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)
			################################################################
			elif entero_tres >= 300 and entero_tres <= 305:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				aumentando += 1
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)
			################################################################
			elif separadores_cuatro == "5610" or entero_seis >= 560221 and entero_seis <= 560225: 
				#CC NO FUNCIONAL
				print("") 
			###############################################################
			elif separadores_cuatro == "2014" or separadores_cuatro == "2149":
				#CC NO FUNCIONAL
				print("") 
			################################################################
			elif separadores_tres == "309"  or separadores_dos == "36" or entero_dos >= 38 and entero_dos <= 39:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				aumentando += 1
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)
			################################################################
			elif separadores_dos == "54" or separadores_dos == "55":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				aumentando += 1
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)
			#################################################################
			elif separadores_cuatro == "6011" or entero_seis >= 622126 and entero_seis <= 622925 or entero_tres >= 644 and entero_tres <= 649 or separadores_dos == "65":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				aumentando += 1
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)
			#################################################################
			elif separadores_tres == "636":
				a = random.randint(1, 4)
				if a == 1:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)	
				elif a == 2:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)	
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)		
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)		
			#################################################################
			elif entero_tres >= 637 and entero_tres <= 639:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				aumentando += 1
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)
			#################################################################
			elif entero_cuatro >= 3528 and entero_cuatro <= 3589:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				aumentando += 1
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)
			#################################################################
			elif separadores_cuatro == "6304" or separadores_cuatro == "6706" or separadores_cuatro == "6771" or separadores_cuatro == "6709":
				#CC NO FUNCIONAL
				print("") 
			#################################################################
			elif entero_seis >= 500000 and entero_seis <= 509999 or entero_seis >= 560000 and entero_seis <= 699999:
				a = random.randint(1,8)
				if a == 1:
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)
				elif a == 2:
					generador += str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)		
				elif a == 4:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
						
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)	
				elif a == 5:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)
				elif a == 6:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)
				elif a == 7:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					aumentando += 1
					save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
					print(save, file=open("CCSRandom.txt", "a+"))
					print(save)
			##################################################################
			elif separadores_cuatro == "5019":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				aumentando += 1
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)
			###################################################################
			elif entero_seis >= 222100 and entero_seis <= 272099:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				aumentando += 1
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)
			###################################################################
			elif entero_dos >= 51 and entero_dos <= 55:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				aumentando += 1
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)
			#####################################################################
			elif separadores_cuatro == "6334" or separadores_cuatro == "6767":
				#CC NO FUNCIONAL
				print("") 
			#####################################################################
			elif separadores_cuatro == "4903" or separadores_cuatro == "4905" or separadores_cuatro == "4911" or separadores_cuatro == "4936" or separadores_seis == "564182" or separadores_seis == "633110" or separadores_cuatro == "6333" or separadores_cuatro == "6759":
				#CC NO FUNCIONAL
				print("") 
			#####################################################################
			elif separar == "4" or separadores_cuatro == "4026" or separadores_seis == "417500" or separadores_cuatro == "4405" or separadores_cuatro == "4508" or separadores_cuatro == "4508" or separadores_cuatro == "4844" or separadores_cuatro == "4913" or separadores_cuatro == "4917":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				aumentando += 1
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)
			#####################################################################
			else:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				aumentando += 1
				save = "\n" + "CC: " + generador + "\n" + "CVV: " + cvv + "\n" + fecha_exp + "\n" + "ººººººººººººººººººººººººººººººººººº"
				print(save, file=open("CCSRandom.txt", "a+"))
				print(save)

		print("\033[1;33mDesea continuar usando el programa \033[1;37msi/no")
		volver = input("\033[1;37m>>> ").lower()
		if volver == "si":
			return Aio.modules()
		else:
			print("\033[1;37mCerrando . . .")
			#####################################################################
##########################################################################################################################################
##########################################################################################################################################	
	def cc_gen_country():
		print("""
\033[1;32m  _____ _____      _____ ____  _    _ _   _ _______ _______     __
\033[1;32m / ____/ ____|    / ____/ __ \| |  | | \ | |__   __|  __ \ \   / /
\033[1;32m| |   | |        | |   | |  | | |  | |  \| |  | |  | |__) \ \_/ / 
\033[1;32m| |   | |        | |   | |  | | |  | | . ` |  | |  |  _  / \   /  
\033[1;32m| |___| |____    | |___| |__| | |__| | |\  |  | |  | | \ \  | |   
\033[1;32m \_____\_____\    \_____\____/ \____/|_| \_|  |_|  |_|  \_\ |_|   

				                                                                                    
\033[m1) United States                \033[m31) Mexico                \033[m61) Moldova
\033[m2) Japan                        \033[m32) Finland               \033[m62) Nicaragua
\033[m3) Italy                        \033[m33) China                 \033[m63) Malta
\033[m4) Korea                        \033[m34) Chile                 \033[m64) Trinidad And Tobago
\033[m5) France                       \033[m35) South Africa          \033[m65) Soudi Arabia
\033[m6) Germany                      \033[m36) Slovakia              \033[m66) Croatia
\033[m7) Taiwan                       \033[m37) Hungary               \033[m67) Cyprus
\033[m8) Russian Federation           \033[m38) Ireland               \033[m68) Pakistan
\033[m9) United Kingdom               \033[m39) Egypt                 \033[m69) United Arab Emirates
\033[m10) Netherlands                 \033[m40) Thailand              \033[m70) Kazakhstan
\033[m11) Czech Republic              \033[m41) Ukraine               \033[m71) Kuwait
\033[m12) Turkey                      \033[m42) Serbia                \033[m72) Venezuela
\033[m13) Austria                     \033[m43) Hong Kong             \033[m73) Georgia
\033[m14) Switzerland                 \033[m44) Greece                \033[m74) Montenegro
\033[m15) Spain                       \033[m45) Portugal              \033[m75) El Salvador
\033[m16) Canada                      \033[m46) Latvia                \033[m76) Luxembourg
\033[m17) Sweden                      \033[m47) Singapore             \033[m77) Curacao
\033[m18) Israel                      \033[m48) Iceland               \033[m78) Puerto Rico
\033[m19) Iran                        \033[m49) Malaysia              \033[m79) Costa Rica
\033[m20) Poland                      \033[m50) Colombia              \033[m80) Belarus
\033[m21) India                       \033[m51) Tunisia               \033[m81) Albania
\033[m22) Norway                      \033[m52) Estonia               \033[m82) Liechtenstein
\033[m23) Romania                     \033[m53) Dominican Republic    \033[m83) Bosnia And Herzegovia
\033[m24) Viet Nam                    \033[m54) Sloveania             \033[m84) Paraguay
\033[m25) Belgium                     \033[m55) Ecuador               \033[m85) Philippines
\033[m26) Brazil                      \033[m56) Lithuania             \033[m86) Faroe Islands
\033[m27) Bulgaria                    \033[m57) Palestinian           \033[m87) Guatemala
\033[m28) Indonesia                   \033[m58) New Zealand           \033[m88) Nepal
\033[m29) Denmark                     \033[m59) Bangladeh             \033[m89) Peru
\033[m30) Argentina                   \033[m60) Panama                \033[m90) Uruguay
							""")
		num = int(input("Escoge un pais: "))
		cantidad = int(input("Cuantas CC'S te gustaria generar: "))

		countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
		             "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
		             "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
		             "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
		             "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
		             "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
		             "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
		             "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
		             "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
		             "-"]
		country0 = countries[num-1]
		aumentando = 1

		while aumentando <= cantidad:
			generador = str(random.randint(2,6)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) +  str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

			separar, separar1, separar2, separar3, separar4, separar5 = generador[0], generador[1], generador[3], generador[4], generador[5], generador[6]
			separadores_dos = separar + separar1
			separadores_tres = separar + separar1 + separar2 
			separadores_cuatro = separar + separar1 + separar2 + separar3
			separadores_cinco = separar + separar1 + separar2 + separar3 + separar4
			separadores_seis = separar + separar1 + separar2 + separar3 + separar4 + separar5
			entero_dos = int(separadores_dos)
			entero_tres = int(separadores_tres)
			entero_cuatro = int(separadores_cuatro)
			entero_cinco =  int(separadores_cinco)
			entero_seis =+ int(separadores_seis)

			cvv = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			dia = str(random.randint(0,30))
			mes = str(random.randint(1,12))
			año = str(20) + str(random.randint(21,30))
			fecha_exp = dia + "/" + mes + "/" + año


			if separadores_dos == "34" or separadores_dos == "37":
				generador += str(random.randint(0,9))
			###############################################################
			elif separadores_dos == "62":
				a = random.randint(1, 4)
				if a == 1:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 2:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))	
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif entero_tres >= 300 and entero_tres <= 305:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif separadores_cuatro == "5610" or entero_seis >= 560221 and entero_seis <= 560225: 
				#CC NO FUNCIONAL
				print("\nLoading") 
			###############################################################
			elif separadores_cuatro == "2014" or separadores_cuatro == "2149":
				#CC NO FUNCIONAL
				print("\nLoading") 
			################################################################
			elif separadores_tres == "309"  or separadores_dos == "36" or entero_dos >= 38 and entero_dos <= 39:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif separadores_dos == "54" or separadores_dos == "55":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_cuatro == "6011" or entero_seis >= 622126 and entero_seis <= 622925 or entero_tres >= 644 and entero_tres <= 649 or separadores_dos == "65":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_tres == "636":
				a = random.randint(1, 4)
				if a == 1:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))		
			#################################################################
			elif entero_tres >= 637 and entero_tres <= 639:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif entero_cuatro >= 3528 and entero_cuatro <= 3589:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_cuatro == "6304" or separadores_cuatro == "6706" or separadores_cuatro == "6771" or separadores_cuatro == "6709":
				#CC NO FUNCIONAL
				print("\nLoading") 
			#################################################################
			elif entero_seis >= 500000 and entero_seis <= 509999 or entero_seis >= 560000 and entero_seis <= 699999:
				a = random.randint(1,8)
				if a == 1:
					cd = 1
				elif a == 2:
					generador += str(random.randint(0,9))
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9))	
				elif a == 4:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 5:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 6:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 7:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			##################################################################
			elif separadores_cuatro == "5019":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			###################################################################
			elif entero_seis >= 222100 and entero_seis <= 272099:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			###################################################################
			elif entero_dos >= 51 and entero_dos <= 55:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#####################################################################
			elif separadores_cuatro == "6334" or separadores_cuatro == "6767":
				#CC NO FUNCIONAL
				print("\nLoading") 
			#####################################################################
			elif separadores_cuatro == "4903" or separadores_cuatro == "4905" or separadores_cuatro == "4911" or separadores_cuatro == "4936" or separadores_seis == "564182" or separadores_seis == "633110" or separadores_cuatro == "6333" or separadores_cuatro == "6759":
				#CC NO FUNCIONAL
				print("\nLoading") 
			#####################################################################
			elif separar == "4" or separadores_cuatro == "4026" or separadores_seis == "417500" or separadores_cuatro == "4405" or separadores_cuatro == "4508" or separadores_cuatro == "4508" or separadores_cuatro == "4844" or separadores_cuatro == "4913" or separadores_cuatro == "4917":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			##########################################################
			else:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

			r = requests.get("https://bin-checker.net/api/" + generador)
			json = r.json()
			country = json["country"]
			codigo = country["code"]

			if codigo == country0:
				print("CC: " + str(generador))
				print("CVV: " + str(cvv))
				print("EXP: " + str(fecha_exp))
				print("MARCA: ", json["scheme"])
				print("TIPO: ", json["type"])
				print("NIVEL: ", json["level"])
				country = json["country"]
				pais = country["name"]
				codigo = country["code"]
				print("NOMBRE PAIS: ", pais)
				print("CODIGO PAIS: ", codigo)
				bank = json["bank"]
				nombre = bank["name"]
				sitioweb = bank["website"]
				numero = bank["phone"]
				print("NOMBRE BANCO: ", nombre)
				print("SITIO WEB BANCO: ", sitioweb)
				print("NUMERO BANCO: ", numero)
				todo = str("CC: " + str(generador +
					"\nCVV: " + str(cvv) +
					"\nEXP: " + str(fecha_exp) +
					"\nMARCA: " + json["scheme"] + 
					"\nTIPO: " + json["type"] + 
					"\nNIVEL: " + json["level"] + 
					"\nNOMBRE PAIS: " + pais + 
					"\nCODIGO PAIS: " + codigo + 
					"\nNOMBRE BANCO: " + nombre + 
					"\nSITIO WEB BANCO: " + sitioweb + 
					"\nNUMERO BANCO: " + numero + 
					"\nººººººººººººººººººººººººººººººººººº"))
				print(todo, file=open("CCGenCountry.txt", "a+"))
				print("ººººººººººººººººººººººººººººººººººº")
				aumentando += 1

		print("\033[1;33mDesea continuar usando el programa \033[1;37msi/no")
		volver = input("\033[1;37m>>> ").lower()
		if volver == "si":
			return Aio.modules()
		else:
			print("\033[1;37mCerrando . . .")

	def cc_gen_cardmarca():
		print("""
\033[1;32m  _____ _____    ____  _____            _   _ _____  
\033[1;32m / ____/ ____|  |  _ \|  __ \     /\   | \ | |  __ \ 
\033[1;32m| |   | |       | |_) | |__) |   /  \  |  \| | |  | |
\033[1;32m| |   | |       |  _ <|  _  /   / /\ \ | . ` | |  | |
\033[1;32m| |___| |____   | |_) | | \ \  / ____ \| |\  | |__| |
\033[1;32m \_____\_____|  |____/|_|  \_\/_/    \_\_| \_|_____/ 
                                                                       

\033[m1) VISA                         \033[m11) LOCAL BRAND     \033[m21) UNIONPAY                        
\033[m2) MASTERCARD                   \033[m12) GLOBAL BC       \033[m22) CARNET
\033[m3) AMERICAN EXPRESS             \033[m13) ELO             \033[m23) EFTPOS                 
\033[m4) DISCOVER                     \033[m14) RUPAY           \033[m24) GE CAPITAL
\033[m5) DINERS CLUB INTERNATIONAL    \033[m15) MAESTRO         
\033[m6) CIRRUS                       \033[m16) NSPK MIR        
\033[m7) PRIVATE LABEL                \033[m17) VISA/DANKORT    
\033[m8) MASTERCARD                   \033[m18) NEWDAY          
\033[m9) JCB                          \033[m19) DANKORT         
\033[m10) CHINA UNION PAY             \033[m20) DUE             
			""")

		types_card = ["VISA", "MASTERCARD", "AMERICAN EXPRESS", "DISCOVER", 
		"DINERS CLUB INTERNATIONAL", "CIRRUS", "PRIVATE LABEL", "MASTERCARD", 
		"JCB", "CHINA UNION PAY", "LOCAL BRAND", "GLOBAL BC", "ELO", "RUPAY", 
		"MAESTRO", "NSPK MIR", "VISA/DANKORT", "NEWDAY", "DANKORT", "DUET" "UNIONPAY",
		"CARNET", "EFTPOS","GE CAPITAL", "-"]

		num = int(input("Escoge una marca: "))
		cantidad = int(input("Cuantas CC'S te gustaria generar: "))
		brand_card = types_card[num-1]
		aumentando = 1

		while aumentando <= cantidad:
			generador = str(random.randint(2,6)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) +  str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

			separar, separar1, separar2, separar3, separar4, separar5 = generador[0], generador[1], generador[3], generador[4], generador[5], generador[6]
			separadores_dos = separar + separar1
			separadores_tres = separar + separar1 + separar2 
			separadores_cuatro = separar + separar1 + separar2 + separar3
			separadores_cinco = separar + separar1 + separar2 + separar3 + separar4
			separadores_seis = separar + separar1 + separar2 + separar3 + separar4 + separar5
			entero_dos = int(separadores_dos)
			entero_tres = int(separadores_tres)
			entero_cuatro = int(separadores_cuatro)
			entero_cinco =  int(separadores_cinco)
			entero_seis =+ int(separadores_seis)

			cvv = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			dia = str(random.randint(0,30))
			mes = str(random.randint(1,12))
			año = str(20) + str(random.randint(21,30))
			fecha_exp = dia + "/" + mes + "/" + año

			if separadores_dos == "34" or separadores_dos == "37":
				generador += str(random.randint(0,9))
			###############################################################
			elif separadores_dos == "62":
				a = random.randint(1, 4)
				if a == 1:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 2:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif entero_tres >= 300 and entero_tres <= 305:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif separadores_cuatro == "5610" or entero_seis >= 560221 and entero_seis <= 560225: 
				#CC NO FUNCIONAL
				print("\nLoading") 
			###############################################################
			elif separadores_cuatro == "2014" or separadores_cuatro == "2149":
				#CC NO FUNCIONAL
				print("\nLoading") 
			################################################################
			elif separadores_tres == "309"  or separadores_dos == "36" or entero_dos >= 38 and entero_dos <= 39:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif separadores_dos == "54" or separadores_dos == "55":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_cuatro == "6011" or entero_seis >= 622126 and entero_seis <= 622925 or entero_tres >= 644 and entero_tres <= 649 or separadores_dos == "65":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_tres == "636":
				a = random.randint(1, 4)
				if a == 1:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 2:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))		
			#################################################################
			elif entero_tres >= 637 and entero_tres <= 639:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif entero_cuatro >= 3528 and entero_cuatro <= 3589:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_cuatro == "6304" or separadores_cuatro == "6706" or separadores_cuatro == "6771" or separadores_cuatro == "6709":
				#CC NO FUNCIONAL
				print("\nLoading") 
			#################################################################
			elif entero_seis >= 500000 and entero_seis <= 509999 or entero_seis >= 560000 and entero_seis <= 699999:
				a = random.randint(1,8)
				if a == 1:
					cd = 1
				elif a == 2:
					generador += str(random.randint(0,9))
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9))	
				elif a == 4:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 5:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 6:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 7:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			##################################################################
			elif separadores_cuatro == "5019":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			###################################################################
			elif entero_seis >= 222100 and entero_seis <= 272099:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			###################################################################
			elif entero_dos >= 51 and entero_dos <= 55:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#####################################################################
			elif separadores_cuatro == "6334" or separadores_cuatro == "6767":
				print("\nLoading") 
			#####################################################################
			elif separadores_cuatro == "4903" or separadores_cuatro == "4905" or separadores_cuatro == "4911" or separadores_cuatro == "4936" or separadores_seis == "564182" or separadores_seis == "633110" or separadores_cuatro == "6333" or separadores_cuatro == "6759":
				print("\nLoading") 
			#####################################################################
			elif separar == "4" or separadores_cuatro == "4026" or separadores_seis == "417500" or separadores_cuatro == "4405" or separadores_cuatro == "4508" or separadores_cuatro == "4508" or separadores_cuatro == "4844" or separadores_cuatro == "4913" or separadores_cuatro == "4917":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			##########################################################
			else:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

			r = requests.get("https://bin-checker.net/api/" + generador)
			json = r.json()
			mar = json["scheme"]


			if mar == brand_card:
				print("CC: " + str(generador))
				print("CVV: " + str(cvv))
				print("EXP: " + str(fecha_exp))
				print("MARCA: ", json["scheme"])
				print("TIPO: ", json["type"])
				print("NIVEL: ", json["level"])
				country = json["country"]
				pais = country["name"]
				codigo = country["code"]
				print("NOMBRE PAIS: ", pais)
				print("CODIGO PAIS: ", codigo)
				bank = json["bank"]
				nombre = bank["name"]
				sitioweb = bank["website"]
				numero = bank["phone"]
				print("NOMBRE BANCO: ", nombre)
				print("SITIO WEB BANCO: ", sitioweb)
				print("NUMERO BANCO: ", numero)
				todo = str("CC: " + str(generador +
					"\nCVV: " + str(cvv) +
					"\nEXP: " + str(fecha_exp) +
					"\nMARCA: " + json["scheme"] + 
					"\nTIPO: " + json["type"] + 
					"\nNIVEL: " + json["level"] + 
					"\nNOMBRE PAIS: " + pais + 
					"\nCODIGO PAIS: " + codigo + 
					"\nNOMBRE BANCO: " + nombre + 
					"\nSITIO WEB BANCO: " + sitioweb + 
					"\nNUMERO BANCO: " + numero + 
					"\nººººººººººººººººººººººººººººººººººº"))
				print(todo, file=open("CCGenCardType.txt", "a+"))
				print("ººººººººººººººººººººººººººººººººººº")
				aumentando += 1

		print("\033[1;33mDesea continuar usando el programa \033[1;37msi/no")
		volver = input("\033[1;37m>>> ").lower()
		if volver == "si":
			return Aio.modules()
		else:
			print("\033[1;37mCerrando . . .")

	def cc_gen_cardtype():		
		print("""

\033[1;32m  ____ ____   _______   ______  _____
\033[1;32m / ___/ ___| |_   _\ \ / /  _ \| ____|
\033[1;32m| |  | |       | |  \ V /| |_) |  _|
\033[1;32m| |__| |___    | |   | | |  __/| |___
\033[1;32m \____\____|   |_|   |_| |_|   |_____|
                                                                    
\033[m1) CREDIT                         
\033[m2) DEBIT             
\033[m3) CHARGE CARD
\033[m4) DEBIT OR CREDIT
\033[m5) BANKCARD(INACTIVE) """)          
		types_card = ["CREDIT", "DEBIT", "CHARGE CARD","DEBIT OR CREDIT","BANKCARD(INACTIVE)" "-"]

		num = int(input("Escoge un tipo de tarjeta: "))
		cantidad = int(input("Cuantas CC'S te gustaria generar: "))
		type_card = types_card[num-1]
		aumentando = 1

		while aumentando <= cantidad:
			generador = str(random.randint(2,6)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) +  str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

			separar, separar1, separar2, separar3, separar4, separar5 = generador[0], generador[1], generador[3], generador[4], generador[5], generador[6]
			separadores_dos = separar + separar1
			separadores_tres = separar + separar1 + separar2 
			separadores_cuatro = separar + separar1 + separar2 + separar3
			separadores_cinco = separar + separar1 + separar2 + separar3 + separar4
			separadores_seis = separar + separar1 + separar2 + separar3 + separar4 + separar5
			entero_dos = int(separadores_dos)
			entero_tres = int(separadores_tres)
			entero_cuatro = int(separadores_cuatro)
			entero_cinco =  int(separadores_cinco)
			entero_seis =+ int(separadores_seis)

			cvv = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			dia = str(random.randint(0,30))
			mes = str(random.randint(1,12))
			año = str(20) + str(random.randint(21,30))
			fecha_exp = dia + "/" + mes + "/" + año

			if separadores_dos == "34" or separadores_dos == "37":
				generador += str(random.randint(0,9))
			###############################################################
			elif separadores_dos == "62":
				a = random.randint(1, 4)
				if a == 1:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 2:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif entero_tres >= 300 and entero_tres <= 305:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif separadores_cuatro == "5610" or entero_seis >= 560221 and entero_seis <= 560225: 
				#CC NO FUNCIONAL
				print("\nLoading") 
			###############################################################
			elif separadores_cuatro == "2014" or separadores_cuatro == "2149":
				#CC NO FUNCIONAL
				print("\nLoading") 
			################################################################
			elif separadores_tres == "309"  or separadores_dos == "36" or entero_dos >= 38 and entero_dos <= 39:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif separadores_dos == "54" or separadores_dos == "55":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_cuatro == "6011" or entero_seis >= 622126 and entero_seis <= 622925 or entero_tres >= 644 and entero_tres <= 649 or separadores_dos == "65":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_tres == "636":
				a = random.randint(1, 4)
				if a == 1:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 2:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))		
			#################################################################
			elif entero_tres >= 637 and entero_tres <= 639:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif entero_cuatro >= 3528 and entero_cuatro <= 3589:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_cuatro == "6304" or separadores_cuatro == "6706" or separadores_cuatro == "6771" or separadores_cuatro == "6709":
				#CC NO FUNCIONAL
				print("\nLoading") 
			#################################################################
			elif entero_seis >= 500000 and entero_seis <= 509999 or entero_seis >= 560000 and entero_seis <= 699999:
				a = random.randint(1,8)
				if a == 1:
					cd = 1
				elif a == 2:
					generador += str(random.randint(0,9))
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9))	
				elif a == 4:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 5:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 6:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 7:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			##################################################################
			elif separadores_cuatro == "5019":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			###################################################################
			elif entero_seis >= 222100 and entero_seis <= 272099:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			###################################################################
			elif entero_dos >= 51 and entero_dos <= 55:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#####################################################################
			elif separadores_cuatro == "6334" or separadores_cuatro == "6767":
				print("\nLoading") 
			#####################################################################
			elif separadores_cuatro == "4903" or separadores_cuatro == "4905" or separadores_cuatro == "4911" or separadores_cuatro == "4936" or separadores_seis == "564182" or separadores_seis == "633110" or separadores_cuatro == "6333" or separadores_cuatro == "6759":
				print("\nLoading") 
			#####################################################################
			elif separar == "4" or separadores_cuatro == "4026" or separadores_seis == "417500" or separadores_cuatro == "4405" or separadores_cuatro == "4508" or separadores_cuatro == "4508" or separadores_cuatro == "4844" or separadores_cuatro == "4913" or separadores_cuatro == "4917":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			##########################################################
			else:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

			r = requests.get("https://bin-checker.net/api/" + generador)
			json = r.json()
			tipo = json["type"]


			if tipo == type_card:
				print("CC: " + str(generador))
				print("CVV: " + str(cvv))
				print("EXP: " + str(fecha_exp))
				print("MARCA: ", json["scheme"])
				print("TIPO: ", json["type"])
				print("NIVEL: ", json["level"])
				country = json["country"]
				pais = country["name"]
				codigo = country["code"]
				print("NOMBRE PAIS: ", pais)
				print("CODIGO PAIS: ", codigo)
				bank = json["bank"]
				nombre = bank["name"]
				sitioweb = bank["website"]
				numero = bank["phone"]
				print("NOMBRE BANCO: ", nombre)
				print("SITIO WEB BANCO: ", sitioweb)
				print("NUMERO BANCO: ", numero)
				todo = str("CC: " + str(generador +
					"\nCVV: " + str(cvv) +
					"\nEXP: " + str(fecha_exp) +
					"\nMARCA: " + json["scheme"] + 
					"\nTIPO: " + json["type"] + 
					"\nNIVEL: " + json["level"] + 
					"\nNOMBRE PAIS: " + pais + 
					"\nCODIGO PAIS: " + codigo + 
					"\nNOMBRE BANCO: " + nombre + 
					"\nSITIO WEB BANCO: " + sitioweb + 
					"\nNUMERO BANCO: " + numero + 
					"\nººººººººººººººººººººººººººººººººººº"))
				print(todo, file=open("CCGenCardType.txt", "a+"))
				print("ººººººººººººººººººººººººººººººººººº")
				aumentando += 1

		print("\033[1;33mDesea continuar usando el programa \033[1;37msi/no")
		volver = input("\033[1;37m>>> ").lower()
		if volver == "si":
			return Aio.modules()
		else:
			print("\033[1;37mCerrando . . .")

	def cc_gen_level():
		print("""
  _____ _____    _____ ______ _   _   _      ________      ________ _      
 / ____/ ____|  / ____|  ____| \ | | | |    |  ____\ \    / /  ____| |     
| |   | |      | |  __| |__  |  \| | | |    | |__   \ \  / /| |__  | |     
| |   | |      | | |_ |  __| | . ` | | |    |  __|   \ \/ / |  __| | |     
| |___| |____  | |__| | |____| |\  | | |____| |____   \  /  | |____| |____ 
 \_____\_____|  \_____|______|_| \_| |______|______|   \/   |______|______|
                                                                           
                                                                           

\033[m1) ELECTRON                                  \033[m81) PAYPASS                           \033[m171) CORPORATE/BUSINESS 
\033[m2) PREPAID                                   \033[m82) CONSUMER REVOLVE (CO-BRAND)       \033[m172) PURCHASING CARD 
\033[m3) CLASSIC                                   \033[m83) CANADA CHARGE CARD                \033[m173) CORPORATE EXECUTIVE  
\033[m4) STANDARD                                  \033[m84) PRIVATE LABEL                     \033[m174) HEALTH SAVINGS
\033[m5) PURCHASING                                \033[m85) GSA                               \033[m175) BLUE CHARGE
\033[m6) FLEET                                     \033[m86) ALIMENTACAO                       \033[m176) PROFESSIONAL 
\033[m7) BUSINESS                                  \033[m87) PERSONAL GREEN/GOLD GRCC          \033[m177) REVOLVE (CONSUMER / SBS) 
\033[m8) GOLD                                      \033[m88) BUSINESS/STANDARD                 \033[m178) CORPORATE CO-BRAND CHARGE
\033[m9) PROPRIETARY                               \033[m89) NH CARD                           \033[m179) CANADIAN CD
\033[m10) WORLD ELITE                              \033[m90) WORLD BLACK EDITION               \033[m180) PERSONAL BLUE CHARGE
\033[m11) CCSG LENDING                             \033[m91) SMALL CORPORATE                   \033[m181) PERSONAL GOLD REVOLVE
\033[m12) LAROC INTERNATIONAL CORPORATE            \033[m92) PREPAID BUSINESS                  \033[m182) GOLD/CORPORATE
\033[m13) ENHANCED                                 \033[m93) COMMERCIAL                        \033[m183) PLATINUM REWARDS
\033[m14) PLATINUM                                 \033[m94) PREPAID HSA NON-SUBSTANTIATED     \033[m184) GSA CORPORATE T&E
\033[m15) PREMIUM PLUS                             \033[m95) PERSONAL/ COMPANY                 \033[m185) GRCC PLATINUM
\033[m16) PERSONAL PLATINUM REVOLVE                \033[m96) EXECUTIVE                         \033[m186) CREDIT
\033[m17) CORE CARD                                \033[m97) CONSUMER PREMIUM CARD             \033[m187) OPEN GOLD REVOLVE
\033[m18) PERSONAL                                 \033[m98) GNS GREEN CHARGE                  \033[m188) CORPORATE FLEET CARD
\033[m19) REWARDS                                  \033[m99) TITANIUM MASTERCARD               \033[m189) PURCHASING WITH FLEET
\033[m20) CONSUMER LENDING                         \033[m100) BUSINESS WORLD ELITE             \033[m190) GRCC PLATINUM
\033[m21) PREPAID RELOADABLE                       \033[m111) STANDARD/GOLD                    \033[m191) NH PLATINUM 
\033[m22) WORLD                                    \033[m112) LOTTE CARD
\033[m23) STANDARD/GOLD/PLATINUM                   \033[m113) GRCC
\033[m24) WORLD/GOLD                               \033[m114) GREEN GRCC 
\033[m25) V PAY                                    \033[m115) WORLD SIGNIA 
\033[m26) PREPAID ELECTRON                         \033[m116) PREPAID CASH
\033[m27) INFINITE                                 \033[m117) FLEET CARD 
\033[m28) CORPORATE T&E                            \033[m118) SAMSUNG CARD
\033[m29) CORPORATE                                \033[m119) STANDARD/TITANIUM/PLATINUM
\033[m30) GOLD/PLATINUM                            \033[m120) STANDARD/PLATINUM
\033[m31) PERSONAL GREEN CHARGE                    \033[m121) MIXED 
\033[m32) SEARS                                    \033[m122) FOOD CARD 
\033[m33) CHARGE CARD                              \033[m123) SUPER PREMIUM 
\033[m34) GRMS CORPORATE CONTROL                   \033[m124) PIN ONLY W/O EBT
\033[m35) PERSONAL BLUE REVOLVE                    \033[m125) SHINHAN CARD - CHECK
\033[m36) INDIVIDUAL                               \033[m126) BUSINESS SIGNATURE
\033[m37) PERSONAL GOLD CHARGE                     \033[m127) PERSONAL/GOLD
\033[m38) ATM                                      \033[m128) EUROPEAN REGULATED INDIVIDUAL PAY
\033[m39) GNS PLATINUM CHARGE                      \033[m129) GSA  T&E 
\033[m40) TITANIUM                                 \033[m130) PERSONAL GOLD
\033[m41) PREMIUM                                  \033[m131) FSA-INVALID
\033[m42) CONSUMER CARD                            \033[m132) PREPAID V PAY 
\033[m43) GIFT                                     \033[m133) TRIUMPH - SBS LIMITS  
\033[m44) PERSONAL REVOLVE                         \033[m134) LOTTE WEAVER SKY
\033[m45) STANDARD UNEMBOSSED                      \033[m135) PLATINUM/STANDARD 
\033[m46) SIGNATURE                                \033[m136) ACCOR CO-BRAND
\033[m47) PERSONAL GREEN REVOLVE                   \033[m137) DEFERRED DEBIT 
\033[m48) OPTIMA                                   \033[m138) GREEN 
\033[m49) EXECUTIVE BUSINESS                       \033[m139) PREPAID HEALTHCARE 
\033[m50) STANDARD/WORLD                           \033[m140) GOLD/WORLD ELITE
\033[m51) BLACK                                    \033[m141) DEBIT
\033[m52) VIRTUAL                                  \033[m142) PERSONAL GREEN PREPAID  
\033[m53) PREPAID TRAVEL MONEY                     \033[m143) OPEN LENDING
\033[m54) IKEA CARD                                \033[m144) UNITED AIRLINES  CARD-(RHAPSODY)
\033[m55) SALUTE                                   \033[m145) RELOADABLE PREPAID  
\033[m56) COMPANY REVOLVE                          \033[m146) WORLD CARD
\033[m57) STANDARD/GOLD/PLATINUM/WORLD             \033[m147) CONSUMER LIMITS EXPANSION  
\033[m58) MULTIPLO                                 \033[m148) GLOBAL PAYMENT 
\033[m59) WORLD FOR BUSINESS                       \033[m149) SMALL BUSINESS CARD
\033[m60) CORPORATE NETWORK CARD                   \033[m150) WORLD ELITE BUSINESS  
\033[m61) HSA NON SUBSTANTIATED                    \033[m151) RELOADABLE PREPAID
\033[m62) COMPANY                                  \033[m152) BUSINESS INFINITE  
\033[m63) CIRRUS                                   \033[m153) QUANTUM
\033[m64) CORP-GOLD                                \033[m154) PERSONAL PLATINUM CHARGE 
\033[m65) PERSONAL CHARGE                          \033[m155) OPEN CHARGE 
\033[m66) PERSONAL BLACK CHARGE                    \033[m156) LINE OF CREDIT
\033[m67) WORLD BLACK                              \033[m157) OTHER  
\033[m68) GRCC GREEN                               \033[m158) BC CARD
\033[m69) STUDENT                                  \033[m159) PREPAID HEALTHCARE  
\033[m70) MIXED BIN                                \033[m160) BUSAN BC CARD 
\033[m71) B2B                                      \033[m161) REPAID VIRTUAL 
\033[m72) PREPAID PAYROLL                          \033[m162) GOVERNMENT 
\033[m73) MICRO BUSINESS                           \033[m163) GPP
\033[m74) LOWES CARD                               \033[m164) FLEET/BUSINESS
\033[m75) CONSUMER CHARGE                          \033[m165) PREPAID PLATINUM TRAVEL
\033[m76) CONSUMER REVOLVE                         \033[m166) ARGENTINA
\033[m77) LOWES CARD                               \033[m167) GM CARD
\033[m78) CORPORATE GREEN CHARGE                   \033[m168) PERSONAL GREEN PREPAID 
\033[m79) ELECTRONIC                               \033[m169) GREEN/GOLD 
\033[m80) OUR CARD                                 \033[m170) AUTO
						""")  


		levels_card = ["ELECTRON", "PREPAID", "CLASSIC", "STANDARD", "PURCHASING", 
		"FLEET", "BUSINESS", 
		"GOLD", "PROPRIETARY", "WORLD ELITE", "CCSG LENDING", "LAROC INTERNATIONAL CORPORATE", 
		"ENHANCED", "PLATINUM", "PREMIUM PLUS", "PERSONAL PLATINUM REVOLVE", "CORE CARD",
		"PERSONAL", "REWARDS", "CONSUMER LENDING", "PREPAID RELOADABLE", "WORLD", "STANDARD/GOLD/PLATINUM", 
		"WORLD/GOLD", "V PAY", "PREPAID ELECTRON", "INFINITE", "CORPORATE T&E", "CORPORATE", "GOLD/PLATINUM", 
		"PERSONAL GREEN CHARGE", "SEARS", "CHARGE CARD", "GRMS CORPORATE CONTROL", "PERSONAL BLUE REVOLVE", 
		"INDIVIDUAL", "PERSONAL GOLD CHARGE", "ATM", "GNS PLATINUM CHARGE", "TITANIUM", "PREMIUM", "CONSUMER CARD", 
		"GIFT", "PERSONAL REVOLVE", "STANDARD UNEMBOSSED", "SIGNATURE", "PERSONAL GREEN REVOLVE", "OPTIMA", 
		"EXECUTIVE BUSINESS", "STANDARD/WORLD", "BLACK", "VIRTUAL", "PREPAID TRAVEL MONEY", "IKEA CARD", "SALUTE", 
		"COMPANY REVOLVE", "STANDARD/GOLD/PLATINUM/WORLD", "MULTIPLO", "WORLD FOR BUSINESS", "CORPORATE NETWORK CARD",
		"HSA NON SUBSTANTIATED", "COMPANY", "CIRRUS", "CORP-GOLD", "PERSONAL CHARGE", "PERSONAL BLACK CHARGE", 
		"WORLD BLACK", "GRCC GREEN", "STUDENT", "MIXED BIN", "B2B", "PREPAID PAYROLL", 
		"MICRO BUSINESS", "LOWES CARD", "CONSUMER CHARGE", "CONSUMER REVOLVE", "LOWES CARD", 
		"CORPORATE GREEN CHARGE", "ELECTRONIC", "OUR CARD", "PAYPASS","CONSUMER REVOLVE (CO-BRAND)",
		"CANADA CHARGE CARD","PRIVATE LABEL","GSA","ALIMENTACAO","PERSONAL GREEN/GOLD GRCC"
		"ICARD", "BUSINESS/STANDARD", "NH CARD","WORLD BLACK EDITION","SMALL CORPORATE","PREPAID BUSINESS",
		"COMMERCIAL","PREPAID HSA NON-SUBSTANTIATED","PERSONAL/ COMPANY","EXECUTIVE","CONSUMER PREMIUM CARD",
		"GNS GREEN CHARGE","TITANIUM MASTERCARD","BUSINESS WORLD ELITE", "BLUE AIRMILES CASH BACK CARD", 
		"KB KOOKMIN CARD", "PERSONAL/BLUE", "CULTURA", "OPEN PLATINUM REVOLVE", "MASTERMONEY",
		"BLUE", "CREDIT COEMITIDA", "CORPORATE", "REVOLVE", "STANDARD/GOLD", "LOTTE CARD", "GRCC", "GREEN GRCC", "WORLD SIGNIA",
		"PREPAID CASH", "FLEET CARD", "SAMSUNG CARD", "STANDARD/TITANIUM/PLATINUM", "STANDARD/PLATINUM",
		"MIXED","FOOD CARD","SUPER PREMIUM","PIN ONLY W/O EBT","SHINHAN CARD - CHECK",
		"BUSINESS SIGNATURE","PERSONAL/GOLD","EUROPEAN REGULATED INDIVIDUAL PAY","GSA  T&E","PERSONAL GOLD",
		"FSA-INVALID", "PREPAID V PAY","TRIUMPH - SBS LIMITS","LOTTE WEAVER SKY","PLATINUM/STANDARD",
		"ACCOR CO-BRAND","DEFERRED DEBIT","GREEN","PREPAID HEALTHCARE","GOLD/WORLD ELITE",
		"DEBIT","PERSONAL GREEN PREPAID","OPEN LENDING","UNITED AIRLINES  CARD-(RHAPSODY)",
		"RELOADABLE PREPAID","WORLD CARD","CONSUMER LIMITS EXPANSION","GLOBAL PAYMENT","SMALL BUSINESS CARD",
		"WORLD ELITE BUSINESS","RELOADABLE PREPAID","BUSINESS INFINITE","QUANTUM","PERSONAL PLATINUM CHARGE",
		"OPEN CHARGE","LINE OF CREDIT","OTHER","BC CARD","PREPAID HEALTHCARE","BUSAN BC CARD","PREPAID VIRTUAL",
		"GOVERNMENT","GPP","FLEET/BUSINESS","PREPAID PLATINUM TRAVEL","ARGENTINA","GM CARD","PERSONAL GREEN PREPAID",
		"GREEN/GOLD","AUTO","CORPORATE/BUSINESS","PURCHASING CARD","CORPORATE EXECUTIVE","HEALTH SAVINGS","BLUE CHARGE","PROFESSIONAL", 
		"REVOLVE (CONSUMER / SBS)","CORPORATE CO-BRAND CHARGE","CANADIAN CD","PERSONAL BLUE CHARGE","PERSONAL GOLD REVOLVE",
		"GOLD/CORPORATE","PLATINUM REWARDS","GSA CORPORATE T&E","GRCC PLATINUM","CREDIT","OPEN GOLD REVOLVE","CORPORATE FLEET CARD","PURCHASING WITH FLEET",
		"GRCC PLATINUM","NH PLATINUM", "-"]

		num = int(input("Digita el numero del nivel: "))
		cantidad = int(input("Cuantas CC'S te gustaria generar: "))
		level_card = levels_card[num-1]
		aumentando = 1

		cvv = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
		dia = str(random.randint(0,30))
		mes = str(random.randint(1,12))
		año = str(20) + str(random.randint(21,30))
		fecha_exp = dia + "/" + mes + "/" + año

		while aumentando <= cantidad:
			generador = str(random.randint(2,6)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) +  str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

			separar, separar1, separar2, separar3, separar4, separar5 = generador[0], generador[1], generador[3], generador[4], generador[5], generador[6]
			separadores_dos = separar + separar1
			separadores_tres = separar + separar1 + separar2 
			separadores_cuatro = separar + separar1 + separar2 + separar3
			separadores_cinco = separar + separar1 + separar2 + separar3 + separar4
			separadores_seis = separar + separar1 + separar2 + separar3 + separar4 + separar5
			entero_dos = int(separadores_dos)
			entero_tres = int(separadores_tres)
			entero_cuatro = int(separadores_cuatro)
			entero_cinco =  int(separadores_cinco)
			entero_seis =+ int(separadores_seis)


			if separadores_dos == "34" or separadores_dos == "37":
				generador += str(random.randint(0,9))
			###############################################################
			elif separadores_dos == "62":
				a = random.randint(1, 4)
				if a == 1:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 2:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))	
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif entero_tres >= 300 and entero_tres <= 305:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif separadores_cuatro == "5610" or entero_seis >= 560221 and entero_seis <= 560225: 
				#CC NO FUNCIONAL
				print("\nLoading") 
			###############################################################
			elif separadores_cuatro == "2014" or separadores_cuatro == "2149":
				#CC NO FUNCIONAL
				print("\nLoading") 
			################################################################
			elif separadores_tres == "309"  or separadores_dos == "36" or entero_dos >= 38 and entero_dos <= 39:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			################################################################
			elif separadores_dos == "54" or separadores_dos == "55":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_cuatro == "6011" or entero_seis >= 622126 and entero_seis <= 622925 or entero_tres >= 644 and entero_tres <= 649 or separadores_dos == "65":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_tres == "636":
				a = random.randint(1, 4)
				if a == 1:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))		
			#################################################################
			elif entero_tres >= 637 and entero_tres <= 639:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif entero_cuatro >= 3528 and entero_cuatro <= 3589:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#################################################################
			elif separadores_cuatro == "6304" or separadores_cuatro == "6706" or separadores_cuatro == "6771" or separadores_cuatro == "6709":
				#CC NO FUNCIONAL
				print("\nLoading") 
			#################################################################
			elif entero_seis >= 500000 and entero_seis <= 509999 or entero_seis >= 560000 and entero_seis <= 699999:
				a = random.randint(1,8)
				if a == 1:
					cd = 1
				elif a == 2:
					generador += str(random.randint(0,9))
				elif a == 3:
					generador += str(random.randint(0,9)) + str(random.randint(0,9))	
				elif a == 4:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 5:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 6:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				elif a == 7:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			##################################################################
			elif separadores_cuatro == "5019":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			###################################################################
			elif entero_seis >= 222100 and entero_seis <= 272099:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			###################################################################
			elif entero_dos >= 51 and entero_dos <= 55:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			#####################################################################
			elif separadores_cuatro == "6334" or separadores_cuatro == "6767":
				#CC NO FUNCIONAL
				print("\nLoading") 
			#####################################################################
			elif separadores_cuatro == "4903" or separadores_cuatro == "4905" or separadores_cuatro == "4911" or separadores_cuatro == "4936" or separadores_seis == "564182" or separadores_seis == "633110" or separadores_cuatro == "6333" or separadores_cuatro == "6759":
				#CC NO FUNCIONAL
				print("\nLoading") 
			#####################################################################
			elif separar == "4" or separadores_cuatro == "4026" or separadores_seis == "417500" or separadores_cuatro == "4405" or separadores_cuatro == "4508" or separadores_cuatro == "4508" or separadores_cuatro == "4844" or separadores_cuatro == "4913" or separadores_cuatro == "4917":
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			##########################################################
			else:
				generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

			r = requests.get("https://bin-checker.net/api/" + generador)
			json = r.json()
			code = json["level"]
			levels = level_card

			if  code == levels:
				print("CC: " + str(generador))
				print("CVV: " + str(cvv))
				print("EXP: " + str(fecha_exp))
				print("MARCA: ", json["scheme"])
				print("TIPO: ", json["type"])
				print("NIVEL: ", json["level"])
				country = json["country"]
				pais = country["name"]
				codigo = country["code"]
				print("NOMBRE PAIS: ", pais)
				print("CODIGO PAIS: ", codigo)
				bank = json["bank"]
				nombre = bank["name"]
				sitioweb = bank["website"]
				numero = bank["phone"]
				print("NOMBRE BANCO: ", nombre)
				print("SITIO WEB BANCO: ", sitioweb)
				print("NUMERO BANCO: ", numero)
				todo = str("CC: " + str(generador +
					"\nCVV: " + str(cvv) +
					"\nEXP: " + str(fecha_exp) +
					"\nMARCA: " + json["scheme"] + 
					"\nTIPO: " + json["type"] + 
					"\nNIVEL: " + json["level"] + 
					"\nNOMBRE PAIS: " + pais + 
					"\nCODIGO PAIS: " + codigo + 
					"\nNOMBRE BANCO: " + nombre + 
					"\nSITIO WEB BANCO: " + sitioweb + 
					"\nNUMERO BANCO: " + numero + 
					"\nººººººººººººººººººººººººººººººººººº"))
				print(todo, file=open("CCGenCountry.txt", "a+"))
				print("ººººººººººººººººººººººººººººººººººº")
				aumentando += 1

		print("Desea continuar usando el programa si/no")
		volver = input(">>> ").lower()
		if volver == "si":
			return Aio.modules()
		else:
			print("Cerrando . . .")

	def cc_gen_all():
			print("""

  _____ _____    _____ ______ _   _            _      _      
 / ____/ ____|  / ____|  ____| \ | |     /\   | |    | |     
| |   | |      | |  __| |__  |  \| |    /  \  | |    | |     
| |   | |      | | |_ |  __| | . ` |   / /\ \ | |    | |     
| |___| |____  | |__| | |____| |\  |  / ____ \| |____| |____ 
 \_____\_____|  \_____|______|_| \_| /_/    \_\______|______|
                                                             
\033[m1) United States                \033[m31) Mexico                \033[m61) Moldova
\033[m2) Japan                        \033[m32) Finland               \033[m62) Nicaragua
\033[m3) Italy                        \033[m33) China                 \033[m63) Malta
\033[m4) Korea                        \033[m34) Chile                 \033[m64) Trinidad And Tobago
\033[m5) France                       \033[m35) South Africa          \033[m65) Soudi Arabia
\033[m6) Germany                      \033[m36) Slovakia              \033[m66) Croatia
\033[m7) Taiwan                       \033[m37) Hungary               \033[m67) Cyprus
\033[m8) Russian Federation           \033[m38) Ireland               \033[m68) Pakistan
\033[m9) United Kingdom               \033[m39) Egypt                 \033[m69) United Arab Emirates
\033[m10) Netherlands                 \033[m40) Thailand              \033[m70) Kazakhstan
\033[m11) Czech Republic              \033[m41) Ukraine               \033[m71) Kuwait
\033[m12) Turkey                      \033[m42) Serbia                \033[m72) Venezuela
\033[m13) Austria                     \033[m43) Hong Kong             \033[m73) Georgia
\033[m14) Switzerland                 \033[m44) Greece                \033[m74) Montenegro
\033[m15) Spain                       \033[m45) Portugal              \033[m75) El Salvador
\033[m16) Canada                      \033[m46) Latvia                \033[m76) Luxembourg
\033[m17) Sweden                      \033[m47) Singapore             \033[m77) Curacao
\033[m18) Israel                      \033[m48) Iceland               \033[m78) Puerto Rico
\033[m19) Iran                        \033[m49) Malaysia              \033[m79) Costa Rica
\033[m20) Poland                      \033[m50) Colombia              \033[m80) Belarus
\033[m21) India                       \033[m51) Tunisia               \033[m81) Albania
\033[m22) Norway                      \033[m52) Estonia               \033[m82) Liechtenstein
\033[m23) Romania                     \033[m53) Dominican Republic    \033[m83) Bosnia And Herzegovia
\033[m24) Viet Nam                    \033[m54) Sloveania             \033[m84) Paraguay
\033[m25) Belgium                     \033[m55) Ecuador               \033[m85) Philippines
\033[m26) Brazil                      \033[m56) Lithuania             \033[m86) Faroe Islands
\033[m27) Bulgaria                    \033[m57) Palestinian           \033[m87) Guatemala
\033[m28) Indonesia                   \033[m58) New Zealand           \033[m88) Nepal
\033[m29) Denmark                     \033[m59) Bangladeh             \033[m89) Peru
\033[m30) Argentina                   \033[m60) Panama                \033[m90) Uruguay
								""")
			country1 = int(input("Escoge un pais: "))
			countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
			             "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
			             "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
			             "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
			             "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
			             "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
			             "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
			             "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
			             "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
			             "-"]
			country0 = countries[country1-1]
			print("""
\033[m1) VISA                         \033[m11) LOCAL BRAND     \033[m21) UNIONPAY                        
\033[m2) MASTERCARD                   \033[m12) GLOBAL BC       \033[m22) CARNET
\033[m3) AMERICAN EXPRESS             \033[m13) ELO             \033[m23) EFTPOS                 
\033[m4) DISCOVER                     \033[m14) RUPAY           \033[m24) GE CAPITAL
\033[m5) DINERS CLUB INTERNATIONAL    \033[m15) MAESTRO         \033[m25)
\033[m6) CIRRUS                       \033[m16) NSPK MIR        \033[m26)
\033[m7) PRIVATE LABEL                \033[m17) VISA/DANKORT    \033[m27)
\033[m8) MASTERCARD                   \033[m18) NEWDAY          \033[m28)
\033[m9) JCB                          \033[m19) DANKORT         \033[m29)
\033[m10) CHINA UNION PAY             \033[m20) DUE             \033[m30)
					""")
			types_card = ["VISA", "MASTERCARD", "AMERICAN EXPRESS", "DISCOVER", 
			"DINERS CLUB INTERNATIONAL", "CIRRUS", "PRIVATE LABEL", "MASTERCARD", 
			"JCB", "CHINA UNION PAY", "LOCAL BRAND", "GLOBAL BC", "ELO", "RUPAY", 
			"MAESTRO", "NSPK MIR", "VISA/DANKORT", "NEWDAY", "DANKORT", "DUET" "UNIONPAY",
			"CARNET", "EFTPOS","GE CAPITAL", "-"]
			marcaa = int(input("Escoge una marca: "))
			brand_card = types_card[marcaa-1]

			print("""
\033[m1) CREDIT                         
\033[m2) DEBIT             
\033[m3) CHARGE CARD
\033[m4) DEBIT OR CREDIT
\033[m5) BANKCARD(INACTIVE) """)          
			types_card = ["CREDIT", "DEBIT", "CHARGE CARD","DEBIT OR CREDIT","BANKCARD(INACTIVE)" "-"]
			tipo = int(input("Digita un numero: "))
			type_card = types_card[tipo-1]
			cantidad = int(input("Cuantas CC'S te gustaria generar: "))
			aumentando = 1

			while aumentando <= cantidad:
				generador = str(random.randint(2,6)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) +  str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

				separar, separar1, separar2, separar3, separar4, separar5 = generador[0], generador[1], generador[3], generador[4], generador[5], generador[6]
				separadores_dos = separar + separar1
				separadores_tres = separar + separar1 + separar2 
				separadores_cuatro = separar + separar1 + separar2 + separar3
				separadores_cinco = separar + separar1 + separar2 + separar3 + separar4
				separadores_seis = separar + separar1 + separar2 + separar3 + separar4 + separar5
				entero_dos = int(separadores_dos)
				entero_tres = int(separadores_tres)
				entero_cuatro = int(separadores_cuatro)
				entero_cinco =  int(separadores_cinco)
				entero_seis =+ int(separadores_seis)

				cvv = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				dia = str(random.randint(0,30))
				mes = str(random.randint(1,12))
				año = str(20) + str(random.randint(21,30))
				fecha_exp = dia + "/" + mes + "/" + año


				if separadores_dos == "34" or separadores_dos == "37":
					generador += str(random.randint(0,9))
				###############################################################
				elif separadores_dos == "62":
					a = random.randint(1, 4)
					if a == 1:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					elif a == 2:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))	
					elif a == 3:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					else:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				################################################################
				elif entero_tres >= 300 and entero_tres <= 305:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				################################################################
				elif separadores_cuatro == "5610" or entero_seis >= 560221 and entero_seis <= 560225: 
					#CC NO FUNCIONAL
					print("\nLoading") 
				###############################################################
				elif separadores_cuatro == "2014" or separadores_cuatro == "2149":
					#CC NO FUNCIONAL
					print("\nLoading") 
				################################################################
				elif separadores_tres == "309"  or separadores_dos == "36" or entero_dos >= 38 and entero_dos <= 39:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				################################################################
				elif separadores_dos == "54" or separadores_dos == "55":
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				#################################################################
				elif separadores_cuatro == "6011" or entero_seis >= 622126 and entero_seis <= 622925 or entero_tres >= 644 and entero_tres <= 649 or separadores_dos == "65":
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				#################################################################
				elif separadores_tres == "636":
					a = random.randint(1, 4)
					if a == 1:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					elif a == 3:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					else:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))		
				#################################################################
				elif entero_tres >= 637 and entero_tres <= 639:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				#################################################################
				elif entero_cuatro >= 3528 and entero_cuatro <= 3589:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				#################################################################
				elif separadores_cuatro == "6304" or separadores_cuatro == "6706" or separadores_cuatro == "6771" or separadores_cuatro == "6709":
					#CC NO FUNCIONAL
					print("\nLoading") 
				#################################################################
				elif entero_seis >= 500000 and entero_seis <= 509999 or entero_seis >= 560000 and entero_seis <= 699999:
					a = random.randint(1,8)
					if a == 1:
						cd = 1
					elif a == 2:
						generador += str(random.randint(0,9))
					elif a == 3:
						generador += str(random.randint(0,9)) + str(random.randint(0,9))	
					elif a == 4:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					elif a == 5:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					elif a == 6:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					elif a == 7:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					else:
						generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				##################################################################
				elif separadores_cuatro == "5019":
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				###################################################################
				elif entero_seis >= 222100 and entero_seis <= 272099:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				###################################################################
				elif entero_dos >= 51 and entero_dos <= 55:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				#####################################################################
				elif separadores_cuatro == "6334" or separadores_cuatro == "6767":
					#CC NO FUNCIONAL
					print("\nLoading") 
				#####################################################################
				elif separadores_cuatro == "4903" or separadores_cuatro == "4905" or separadores_cuatro == "4911" or separadores_cuatro == "4936" or separadores_seis == "564182" or separadores_seis == "633110" or separadores_cuatro == "6333" or separadores_cuatro == "6759":
					#CC NO FUNCIONAL
					print("\nLoading") 
				#####################################################################
				elif separar == "4" or separadores_cuatro == "4026" or separadores_seis == "417500" or separadores_cuatro == "4405" or separadores_cuatro == "4508" or separadores_cuatro == "4508" or separadores_cuatro == "4844" or separadores_cuatro == "4913" or separadores_cuatro == "4917":
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				##########################################################
				else:
					generador += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

				r = requests.get("https://bin-checker.net/api/" + generador)
				json = r.json()
				country = json["country"]
				codigo = country["code"]
				marcaaa = json["scheme"]
				tipoo = json["type"]

				if codigo == country0 and marcaaa == brand_card and tipo == type_card:
					print("CC: " + str(generador))
					print("CVV: " + str(cvv))
					print("EXP: " + str(fecha_exp))
					print("MARCA: ", json["scheme"])
					print("TIPO: ", json["type"])
					print("NIVEL: ", json["level"])
					country = json["country"]
					pais = country["name"]
					codigo = country["code"]
					print("NOMBRE PAIS: ", pais)
					print("CODIGO PAIS: ", codigo)
					bank = json["bank"]
					nombre = bank["name"]
					sitioweb = bank["website"]
					numero = bank["phone"]
					print("NOMBRE BANCO: ", nombre)
					print("SITIO WEB BANCO: ", sitioweb)
					print("NUMERO BANCO: ", numero)
					todo = str("CC: " + str(generador +
						"\nCVV: " + str(cvv) +
						"\nEXP: " + str(fecha_exp) +
						"\nMARCA: " + json["scheme"] + 
						"\nTIPO: " + json["type"] + 
						"\nNIVEL: " + json["level"] + 
						"\nNOMBRE PAIS: " + pais + 
						"\nCODIGO PAIS: " + codigo + 
						"\nNOMBRE BANCO: " + nombre + 
						"\nSITIO WEB BANCO: " + sitioweb + 
						"\nNUMERO BANCO: " + numero + 
						"\nººººººººººººººººººººººººººººººººººº"))
					print(todo, file=open("CCGenAll.txt", "a+"))
					print("ººººººººººººººººººººººººººººººººººº")
					aumentando += 1

			print("\033[1;32mDesea continuar usando el programa \033[1;37msi/no")
			volver = input("\033[1;37m>>> ").lower()
			if volver == "si":
				return Aio.modules()
			else:
				print("\033[1;37mCerrando . . .")

		
	def get_info():

		decision = int(input("Deseas obtener informarcion de \n1.Un unico BIN/CC\n2.Obtener informarcion de un .txt\n>>> "))
		if decision == 1:
			ccbin = input("Digita el BIN/CC: ")
			r = requests.get("https://bin-checker.net/api/" + ccbin)
			json = r.json()
			print("CC o Bin: " + str(ccbin))
			print("MARCA: ", json["scheme"])
			print("TIPO: ", json["type"])
			print("NIVEL: ", json["level"])
			country = json["country"]
			pais = country["name"]
			codigo = country["code"]
			print("NOMBRE PAIS: ", pais)
			print("CODIGO PAIS: ", codigo)
			bank = json["bank"]
			nombre = bank["name"]
			sitioweb = bank["website"]
			numero = bank["phone"]
			print("NOMBRE BANCO: ", nombre)
			print("SITIO WEB BANCO: ", sitioweb)
			print("NUMERO BANCO: ", numero)
			todo = str("CC: " + str(ccbin +
				"\nMARCA: " + json["scheme"] + 
				"\nTIPO: " + json["type"] + 
				"\nNIVEL: " + json["level"] + 
				"\nNOMBRE PAIS: " + pais + 
				"\nCODIGO PAIS: " + codigo + 
				"\nNOMBRE BANCO: " + nombre + 
				"\nSITIO WEB BANCO: " + sitioweb + 
				"\nNUMERO BANCO: " + numero + 
				"\nººººººººººººººººººººººººººººººººººº"))
			print(todo, file=open("CCBinInfo.txt", "a+"))
			print("ººººººººººººººººººººººººººººººººººº")
			print("\033[1;33mDesea continuar usando el programa \033[1;37msi/no")
			volver = input("\033[1;37m>>> ").lower()
			if volver == "si":
				return Aio.modules()
			else:
				print("\033[1;37mCerrando . . .")

		else:		
			combo = input("Ubicacion de las CC'S o los BINS: ")
			combo = open(combo, 'r').readlines()
			combo = [linea.replace('\n',"") for linea in combo]
			combo = [linea.replace('xxxxxxxxxx',"") for linea in combo]

			for linea in combo:
					datos = linea.split(':')
					r = requests.get("https://lookup.binlist.net/" + datos[0])
					json = r.json()
					binn = str(linea) + "xxxxxxxxxx"
					print("CC o Bin: " + str(binn))
					print("MARCA: ", json["scheme"])
					print("TIPO: ", json["type"])
					print("NIVEL: ", json["level"])
					country = json["country"]
					pais = country["name"]
					codigo = country["code"]
					print("NOMBRE PAIS: ", pais)
					print("CODIGO PAIS: ", codigo)
					bank = json["bank"]
					nombre = bank["name"]
					sitioweb = bank["website"]
					numero = bank["phone"]
					print("NOMBRE BANCO: ", nombre)
					print("SITIO WEB BANCO: ", sitioweb)
					print("NUMERO BANCO: ", numero)
					todo = str("CC: " + str(binn +
						"\nMARCA: " + json["scheme"] + 
						"\nTIPO: " + json["type"] + 
						"\nNIVEL: " + json["level"] + 
						"\nNOMBRE PAIS: " + pais + 
						"\nCODIGO PAIS: " + codigo + 
						"\nNOMBRE BANCO: " + nombre + 
						"\nSITIO WEB BANCO: " + sitioweb + 
						"\nNUMERO BANCO: " + numero + 
						"\nººººººººººººººººººººººººººººººººººº"))
					print(todo, file=open("CCInfo.txt", "a+"))
					print("ººººººººººººººººººººººººººººººººººº")

			print("\033[1;33mDesea continuar usando el programa \033[1;37msi/no")
			volver = input("\033[1;37m>>> ").lower()
			if volver == "si":
				return Aio.modules()
			else:
				print("\033[1;37mCerrando . . .")


	def modules():
		os.system("clear")
		print("""
 \033[1;31m _________________________________________________
 \033[1;31m|                                                 |
 \033[1;36m# \033[1;33mGrupos de Bin WhatsApp \033[1;36m#                        \033[1;31m|
 \033[1;31m|\033[1;34m-------------------------------------------------\033[1;31m|
 \033[1;31m| \033[1;32mhttps://chat.whatsapp.com/BQQ9ARePQEJGz99DFz8CN8\033[1;31m|
 \033[1;31m|                                                 |
 \033[1;31m| \033[1;32mhttps://chat.whatsapp.com/JLcQsSsZ1mr8UpOI8AmmUM[1;31m|
 \033[1;31m|                                                 | 
 \033[1;31m| \033[1;32mhttps://chat.whatsapp.com/IITNRso0vjOGkrpuf8NsND\033[1;31m|
 \033[1;31m|                                                 |
 \033[1;31m| \033[1;32mhttps://chat.whatsapp.com/E1eIGYtJzwRDQZlL7eOEnp\033[1;31m|
 \033[1;31m|\033[1;34m-------------------------------------------------\033[1;31m|
 \033[1;31m|                                                 |
 \033[1;36m# \033[1;33mCreated by : \033[1;37mzTobiCode  \033[1;36m#                       \033[1;31m|
 \033[1;31m|_________________________________________________| 

\033[1;32m          _____ ____  
\033[1;32m    /\   |_   _/ __ \ 
\033[1;32m   /  \    | || |  | | 
\033[1;32m  / /\ \   | || |  | |
\033[1;32m / ____ \ _| || |__| | 
\033[1;32m/_/    \_\_____\____/ 

\033[1;31m1.\033[1;36mGenerador BINS aleatorios
\033[1;31m2.\033[1;36mGenerador CC'S aleatorias
\033[1;31m3.\033[1;36mGenerar CC'S por pais (necesita conexion a internet)
\033[1;31m4.\033[1;36mGenerar CC'S por marca de tarjeta (necesita conexion a internet)
\033[1;31m5.\033[1;36mGenerar CC'S por tipo (necesita conexion a internet)
\033[1;31m6.\033[1;36mObtener info de las CC'S y BINS
""")

		resp = int(input("\033[1;33mAIO \033[1;37m>>> "))

		#TOMA DE RESPUESTA
		if resp == 1:
			Aio.bin_gen()
		elif resp == 2:
			Aio.cc_gen_random()
		elif resp == 3:
			Aio.cc_gen_country()
		elif resp == 4:
			Aio.cc_gen_cardmarca()
		elif resp == 5:
			Aio.cc_gen_cardtype()	
		elif resp == 6:
			Aio.get_info()
		else:
			print("\033[1;31mRespuesta Erronea")
			return

Aio.modules()

