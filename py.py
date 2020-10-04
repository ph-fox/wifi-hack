import os, sys

def update():

  print("updating!")
  os.system("rm -rf wifi.py")
  os.system("rm -rf con")
  os.system("cd ..")
  os.system("git clone https://github.com/abalesluke/wifi-hack")
  os.system('mv wifi-hack {}'.format(homeDir))
  print("Updated successfully!")  
  
