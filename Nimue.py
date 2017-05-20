# -*- Coding: UTF-8 -*-
# Python 3
# By: LawlietJH
# Nimue
# v1.0.2

import time
import os



#=======================================================================



# Función Que Permite Esconder El Texto de la Pantalla.
# Para escribrir por ejemplo contraseñas y evitar a los curiosos.
def Pass(Text=""):
	
	from getpass import getpass as pwd
	
	Pwd = pwd(Text)
	
	return Pwd



# Funcion Que pide escribir una contraseña y si Coincide con la Contraseña
# Que fue pasada a la función con los argumentos, devolvera True.
def Access(Pwd = "xD", String = "\n\n\t Pwd: "):
	
	Cadena = Pass(String)
	
	if Cadena == Pwd: return True
	else: return False



def Pause(Quiet=True):
	
	if Quiet: os.system("Pause > Nul")
	else:  os.system("Pause")



def Sleep(Time=1.5):
	
	time.sleep(Time)



def Sys(Com=""):
	
	os.system(Com)



def Cls():
	
	os.system("Cls")



def WinSize(Lines, Cols):
	
	os.system("mode con lines={} cols={}".format(Lines, Cols))



#=======================================================================



def Confirm():
	
	while True:
		
		Cls()
		
		print("\n\n\t [+] Activar Clave (S/N):\n\n")
		
		Opc = input("\t  > ").lower()
		
		if Opc == "s" or Opc == "si":
			Lock()
		elif Opc == "n" or Opc == "no":
			print("\n\n\t [*] Bye...")
			End(1)
		else:
			print("\n\n\t [!] Escribe Si/No")
			Sleep()



def Lock():
	
	Sys('ren Protegida "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
	Sys('attrib +h +s +r "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
	
	print("\n\t [*] Carpeta Protegida Exitosamente!")
	End(0)



def Unlock():
	
	Cont = 0
	
	while Cont < 3:
		
		Cls()
		
		Cont += 1
		
		print("\n\n\t [+] Ingrese La Clave Para Poder Acceder A Su Carpeta Protegida.\n")
		Clave = Access("EnyLane","\t  > ")
		
		if Clave == True:
			
			Sys('attrib -h -s -r "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
			Sys('ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Protegida')
			
			print("\n\t [*] Carpeta Desbloqueada Exitosamente!")
			End(0)
		
		else:
			
			print("\n\t\t\t [!] Clave Incorrecta!")
			Sleep()
		
	Fail()


def MDLocker():
	
	Sys("md Protegida")
	
	print("\n\t [*] La Carpeta 'Protegida' Fue Creada Satisfactoriamente.")
	End(0)



def Fail():
	
	print("\n\t [!] Lo Siento, Pero Tu No Eres El Propietario.\n")
	End(1, 2.5)



def End(num=0, Time=1.5):
	
	Sleep(Time)
	exit(num)



def Menu():
	
	Cls()
	Sys("Title Carpeta Protegida")
	WinSize(12,80)
	
	if os.path.exists("Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"): Unlock()
	if not os.path.exists("Protegida"): MDLocker()
	else: Confirm()


#=======================================================================



if __name__ == "__main__":
	
	Menu()

