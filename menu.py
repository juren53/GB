#!/usr/bin/python
# menu.py
#----------------------------------------------------------------------------
#    Front End Menu for GB Analysis Framework
#    Updated:  Tue 20 Sep 2016 09:55:51 AM CDT 
#----------------------------------------------------------------------------

import subprocess
import os

os.system('clear')
print("  Gas Buddy User Point Analysis")
ans=True
while ans:
#    print ("""  
#    1. Pack race(y,s)    3. Matches(d,y,l,p,s)                          
#    2. Hourly(y,s)       4. Days(s,d,l)            5. Exit                   
#    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1": 
      subprocess.call("~/anaconda2/bin/python  gb-pack-race-today.py", shell=True)
    elif ans=="1y":
      subprocess.call("~/anaconda2/bin/python  gb-pack-race-yesterday.py", shell=True)
    elif ans=="1s":
      subprocess.call("~/anaconda2/bin/python  gb-pack-race-select.py", shell=True)
    elif ans=="1r":
      subprocess.call("~/anaconda2/bin/python  gb-range-race-today.py", shell=True)

    elif ans=="1l":
      subprocess.call("~/anaconda2/bin/python  long-day-yesterday.py | less", shell=True)

    elif ans=="3":
      subprocess.call("~/anaconda2/bin/python  gb-match-today.py", shell=True)
    elif ans=="3d":
      subprocess.call("~/anaconda2/bin/python  gb-match-today-d.py", shell=True)
    elif ans=="3s":
      subprocess.call("~/anaconda2/bin/python  gb-match-select.py", shell=True)
    elif ans=="3y":
      subprocess.call("~/anaconda2/bin/python  gb-match-yesterday.py", shell=True)
    elif ans=="3l":
      subprocess.call("~/anaconda2/bin/python  gb-match-last-hour.py", shell=True)
    elif ans=="3n":
      subprocess.call("~/anaconda2/bin/python  gb-match-last-hour-d.py", shell=True)
    elif ans=="3p":
      subprocess.call("~/anaconda2/bin/python  gb-match-over-4k.py", shell=True)
    elif ans=="k":
      subprocess.call("~/anaconda2/bin/python  kc-menu.py", shell=True)
    elif ans=="2":
      subprocess.call("~/anaconda2/bin/python  by-hour-today.py", shell=True)	
    elif ans=="2y":
      subprocess.call("~/anaconda2/bin/python  by-hour.py", shell=True)	
    elif ans=="2s":
      subprocess.call("~/anaconda2/bin/python  by-hour-select.py", shell=True)	
    elif ans=="2l":
      subprocess.call("~/anaconda2/bin/python  long-hour-today.py | less", shell=True)	
    elif ans=="2r":
      subprocess.call("~/anaconda2/bin/python  range-by-hour-today.py", shell=True)	
    elif ans=="4":
      subprocess.call("~/anaconda2/bin/python  day-total.py", shell=True) 
    elif ans=="4s":
      subprocess.call("~/anaconda2/bin/python  day-total-select-user.py", shell=True)
    elif ans=="4d":
      subprocess.call("~/anaconda2/bin/python  day-total-select-date.py", shell=True)
    elif ans=="4l":
      subprocess.call("~/anaconda2/bin/python  long-day-total.py | less", shell=True)
    elif ans=="4r":
      subprocess.call("~/anaconda2/bin/python  day-range-total.py", shell=True)
    elif ans=="?":
      subprocess.call("~/anaconda2/bin/python  help.py", shell=True)	
    elif ans=="g":
      subprocess.call("~/Projects/GB/Extended/get-gb-data", shell=True)

    elif ans=="help":
      subprocess.call("less ~/Projects/GB/INFO_GB-Python-Scripts.txt", shell=True)	


    elif ans=="d":
      subprocess.call("ls -lag ~/Projects/GB/Data/GB* -r | less", shell=True)	

    elif ans=="touch":
      subprocess.call("~/Projects/GB/Data/gb-touch", shell=True)	


    elif ans=="t":
      subprocess.call("top", shell=True)	

    elif ans=="5":
      quit()
    elif ans !="":
      print("\n Not Valid Choice Try again") 
