# get-a-gb-file.py - - downloads a gb file from jaunet 
# file to DL entered as sys.argv[1]
# e.g. python3 get-a-gb-file.py <file_name>
#
from ftplib import FTP
import sys
import os

ftp = FTP('192.168.1.1')     # connect to host, default port

ftp.login(user='admin', passwd = 'jimbo')  # pass ID PW

ftp.cwd('/9E20-90F6/Projects/GB/Data')  # change working dir on server

#ftp.getwelcome()

#ftp.dir()

#ftp.retrlines('LIST') 

#ftp.size('test.csv')

filename = sys.argv[1]  #use file passed as ys.argv[1]


#print (sys.argv[1])

os.chdir('/home/juren/Projects/GB/Data')


ftp.retrbinary('RETR '+ filename, open(filename, 'wb').write)  #DL file




