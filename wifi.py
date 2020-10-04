import colorama, time, os, sys
from py import *
from con.wi import *
from colorama import *

os.system("apt install python3")

print("""\033[1;31;40m
██╗    ██╗██╗███████╗██╗              ██╗  ██╗ █████╗  ██████╗██╗  ██╗
██║    ██║██║██╔════╝██║              ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
██║ █╗ ██║██║█████╗  ██║    █████╗    ███████║███████║██║     █████╔╝ 
██║███╗██║██║██╔══╝  ██║    ╚════╝    ██╔══██║██╔══██║██║     ██╔═██╗ 
╚███╔███╔╝██║██║     ██║              ██║  ██║██║  ██║╚██████╗██║  ██╗
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝              ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ 
                                                                      
""")
print(Fore.GREEN +"Team: SudoCyberHacker/Centercorp")
print("Coded by: Anikin Luke")
print("Welcome to SudoCentercorp Wifi hack\n")
print("Type 'help' to show commands!")

def main():

	uii = input(">").lower()
	if(uii == "start"):
		wi()
	elif(uii == "help"):
		
		print("""
=============================================
+| 	Wifi-Hack coded by Anikin Luke     |+
=============================================
+|     COMMANDS            Decription      |+
+|-----------------------------------------|+
+|     start   --  To Start hacking wifi's |+
+|     About   --  To show dev info.       |+
+|     Exit    --  To quit the program.    |+
+|                                         |+
+|     scan    -- To scan or find hidden   |+
+|                   wifi name's.          |+
+|     Help    -- To show commands         |+
+|    update   --   To update to tool      |+                       
 ===========================================  
		
		""")
		main()
		
	elif(uii =="about"):
		print("""
		
	=============================================
	+|             About this tool             |+
	=============================================
	+|              This Tool Is               |+
	+|               Is Created                |+
	+|                   By                    |+
	+|            Anikin Luke Abales           |+
	+|  for SudoCentercorp team CyberHackers   |+
	+|-----------------------------------------|+
	+| Tool name: WIFI-HACK     	           |+
	+| Use To Hack Wifi Networks		   |+
	+| Tool version: 1.0                       |+
	+|-----------------------------------------|+
	+|                Contact                  |+
	+| 	      Facebook-Group         	   |+
	+|  facebook.com/groups/sudocyberhackers   |+
	+|--------------^--------^-----------------|+
	+|   Email: Anonnewshacker@gmail.com       |+
	+|   Github: abalesluke                    |+
	+|                                         |+
	+|                 Note!                   |+
	+|    This tool is now available on github |+
	+|    so please dont republish it on github|+
	+|    i do not autorized you to edit this  |+
	+|    tool or republish it on github.      |+
	+|                                         |+
	+|         Editing or changing the         |+
	+|       name of the coder or developer    |+
	+|        wont make's you a programmer.    |+
	+|                                         |+
	+|        [+]Respect the coder's[+]        |+
	 ===========================================  		
		
		""")
		main()
	elif(uii=="exit"):
		return
	elif(uii=="scan"):
		print("\nSorry this feature comming soon!!")
		main()
	elif(uii=="update"):

  		print("updating!")
  		os.system("git clone https://github.com/abalesluke/wifi-hack")
  		os.system('mv wifi-hack /data/data/com.termux/files/home/')
  		print("Updated successfully!")  
	else:
		print("Error! Command not found!")
		print("try typing 'help'")
		main()
main()




