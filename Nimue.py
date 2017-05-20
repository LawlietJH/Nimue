# -*- Coding: UTF-8 -*-
# Python 3
# By: LawlietJH
# Nimue
# v1.0.5

import time
import os



#=======================================================================



# Función Que Permite Esconder El Cursor de la Pantalla (La rayita que parpadea xD).
def HiddenCursor(imp="Hide"):
	
	#~ imp = imp.title()		#Devuelve la cadena solo con la primera letra de cada palabra en mayuscula
	imp = imp.capitalize()		#Devuelve la cadena solo con la primera letra de la primer palabra en mayuscula

	if os.name == 'nt':
		import msvcrt
		import ctypes

		class _CursorInfo(ctypes.Structure):
			_fields_ = [("size", ctypes.c_int),
						("visible", ctypes.c_byte)]
	
	def hide_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = False
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25l")
			sys.stdout.flush()

	def show_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = True
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25h")
			sys.stdout.flush()
	
		
	if imp == "Hide": hide_cursor()
	elif imp =="Show": show_cursor()
	else: return



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



#=======================================================================



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



def End(num=0, Time=1.5):
	
	Sleep(Time)
	exit(num)



#=======================================================================



def Main():
	
	HiddenCursor()
	
	Cont = 0
	
	Cls()
	Sys("Title Carpeta Protegida")
	WinSize(12,80)
	
	if os.path.exists("Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"):
				
		while Cont < 3:
			
			Cls()
			
			Cont += 1
			
			print("\n\n\n\t [+] Ingrese La Clave Para Poder Acceder A Su Carpeta Protegida.\n")
			Clave = Access("ZióN","\t  > ")
			
			if Clave == True:
				
				Sys('attrib -h -s -r "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
				Sys('ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Protegida')
				
				print("\n\t [*] Carpeta Desbloqueada Exitosamente!")
				End(0)
			
			else:
				
				print("\n\t [!] Clave Incorrecta!")
				Sleep()
		
		print("\n\t [!] Lo Siento, Pero Tu No Eres El Propietario.\n")
		
		End(1, 2.5)
		
	if not os.path.exists("Protegida"):
		
		Sys("md Protegida")
		
		print("\n\n\n\t [*] La Carpeta 'Protegida' Fue Creada Satisfactoriamente.")
		
		End(0, 3)
	
	else:
		
		while True:
			
			Cls()
			
			print("\n\n\n\t [+] Activar Clave (S/N):\n")
			
			Opc = input("\t  > ").lower()
			
			if Opc == "s" or Opc == "si":
				
				Sys('ren Protegida "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
				Sys('attrib +h +s +r "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
				
				print("\n\t [*] Carpeta Protegida Exitosamente!")
				End(0)
				
			elif Opc == "n" or Opc == "no":
				print("\n\t [*] Bye...")
				End(1)
			else:
				print("\n\t [!] Escribe Si/No")
				Sleep()



#=======================================================================



if __name__ == "__main__":
	
	Main()


