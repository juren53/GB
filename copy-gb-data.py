#!/usr/bin/python3
#-----------------------------------------------------------
#        Copies essential GB data files for analysis
#         
#        Updated  Thu 05 Dec 2019 07:29:06 AM CST 
#        copy-gb-data.py 
#-----------------------------------------------------------
import pandas as pd
import os
import glob
import numpy as np
from pandas import DataFrame, Series
import datetime
import csv

# os.system('clear')        # clears the screen
os.chdir('/home/juren/Projects/GB/Data')
db1 = max([f for f in os.listdir('.') if f.lower().endswith('.csv')], key=os.path.getctime)

print("=======================================")
print("      Copy 7 Days of GB Data to ~/tmp  ",db1[3:18])
print("=======================================")

os.chdir('/home/juren/Projects/GB/Data')


#db1 = max([f for f in os.listdir('.') if f.lower().endswith('.csv')], key=os.path.getctime)


# The following routine builds a list of names from the most recent GB*.csv file
with open(db1, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        list = []
        r = 0
        for row in reader:
                r = r+1
                Rank = row[1]
                Name = row[0]
                list.append(Name)

# The following routine builds a short list of names from the most the list
# using jimbeaux53 as the mid-point in the range of names
# print list.index('jimbeaux53')

slist = []
row = list.index('jimbeaux53') - 9
end = list.index('jimbeaux53') + 8

while row < end:
    
    slist.append(list[row])
    row = row + 1

#print slist



db1 = db1[0:13]+'-0000.csv'        # Rebuilds most recent filename at midnite

day = db1[3:13]

day1f = datetime.date(*[int(i) for i in day.split("-")]) 

one_day = datetime.timedelta(days=1)

day2f= day1f-one_day
day3f= day1f-(one_day*2)   
day4f= day1f-(one_day*3) 
day5f= day1f-(one_day*4)
day6f= day1f-(one_day*5)
day7f= day1f-(one_day*6)
day8f= day1f-(one_day*7)

db2="GB-"+str(day2f)+'-0000.csv'
db3="GB-"+str(day3f)+'-0000.csv'
db4="GB-"+str(day4f)+'-0000.csv'
db5="GB-"+str(day5f)+'-0000.csv'
db6="GB-"+str(day6f)+'-0000.csv'
db7="GB-"+str(day7f)+'-0000.csv'
db8="GB-"+str(day8f)+'-0000.csv'

#print(db1,db2,db3,db4,db5,db6,db7,db8)


os.system("cp " + db1 + " ~/tmp/" + db1)
os.system("cp " + db2 + " ~/tmp/" + db2)
os.system("cp " + db3 + " ~/tmp/" + db3)
os.system("cp " + db4 + " ~/tmp/" + db4)
os.system("cp " + db5 + " ~/tmp/" + db5)
os.system("cp " + db6 + " ~/tmp/" + db6)
os.system("cp " + db7 + " ~/tmp/" + db7)
os.system("cp " + db8 + " ~/tmp/" + db8)

os.chdir('/home/juren/Projects/GB/Data')

    
db1 = max([f for f in os.listdir('.') if f.lower().endswith('.csv')], key=os.path.getctime)

#db1 = db1[0:13]+'-0000.csv'        # Rebuilds most recent filename at midnite

day = db1[3:16]
print("gb2rs.py","                                           ",db1[3:18])

hour1f = datetime.datetime(*[int(i) for i in day.split("-")]) 

one_hour = datetime.timedelta(hours=1)


hour2f= hour1f-one_hour
hour3f= hour1f-(one_hour*2) 
hour4f= hour1f-(one_hour*3) 
hour5f= hour1f-(one_hour*4) 
hour6f= hour1f-(one_hour*5) 
hour7f= hour1f-(one_hour*6) 
hour8f= hour1f-(one_hour*7) 
hour9f= hour1f-(one_hour*8) 
hour10f= hour1f-(one_hour*9) 
hour11f= hour1f-(one_hour*10) 
hour12f= hour1f-(one_hour*11) 
hour13f= hour1f-(one_hour*12) 
hour14f= hour1f-(one_hour*13) 
hour15f= hour1f-(one_hour*14) 
hour16f= hour1f-(one_hour*15) 
hour17f= hour1f-(one_hour*16) 
hour18f= hour1f-(one_hour*17) 
hour19f= hour1f-(one_hour*18) 
hour20f= hour1f-(one_hour*19) 
hour21f= hour1f-(one_hour*20) 
hour22f= hour1f-(one_hour*21) 
hour23f= hour1f-(one_hour*22) 
hour24f= hour1f-(one_hour*23)
hour25f= hour1f-(one_hour*24)

db2="GB-"+str(hour2f)[0:10]+"-"+str(hour2f)[11:13]+'00.csv'
db3="GB-"+str(hour3f)[0:10]+"-"+str(hour3f)[11:13]+'00.csv'
db4="GB-"+str(hour4f)[0:10]+"-"+str(hour4f)[11:13]+'00.csv'
db5="GB-"+str(hour5f)[0:10]+"-"+str(hour5f)[11:13]+'00.csv'
db6="GB-"+str(hour6f)[0:10]+"-"+str(hour6f)[11:13]+'00.csv'
db7="GB-"+str(hour7f)[0:10]+"-"+str(hour7f)[11:13]+'00.csv'
db8="GB-"+str(hour8f)[0:10]+"-"+str(hour8f)[11:13]+'00.csv'
db9="GB-"+str(hour9f)[0:10]+"-"+str(hour9f)[11:13]+'00.csv'
db10="GB-"+str(hour10f)[0:10]+"-"+str(hour10f)[11:13]+'00.csv'
db11="GB-"+str(hour11f)[0:10]+"-"+str(hour11f)[11:13]+'00.csv'
db12="GB-"+str(hour12f)[0:10]+"-"+str(hour12f)[11:13]+'00.csv'
db13="GB-"+str(hour13f)[0:10]+"-"+str(hour13f)[11:13]+'00.csv'
db14="GB-"+str(hour14f)[0:10]+"-"+str(hour14f)[11:13]+'00.csv'
db15="GB-"+str(hour15f)[0:10]+"-"+str(hour15f)[11:13]+'00.csv'
db16="GB-"+str(hour16f)[0:10]+"-"+str(hour16f)[11:13]+'00.csv'
db17="GB-"+str(hour17f)[0:10]+"-"+str(hour17f)[11:13]+'00.csv'
db18="GB-"+str(hour18f)[0:10]+"-"+str(hour18f)[11:13]+'00.csv'
db19="GB-"+str(hour19f)[0:10]+"-"+str(hour19f)[11:13]+'00.csv'
db20="GB-"+str(hour20f)[0:10]+"-"+str(hour20f)[11:13]+'00.csv'
db21="GB-"+str(hour21f)[0:10]+"-"+str(hour21f)[11:13]+'00.csv'
db22="GB-"+str(hour22f)[0:10]+"-"+str(hour22f)[11:13]+'00.csv'
db23="GB-"+str(hour23f)[0:10]+"-"+str(hour23f)[11:13]+'00.csv'
db24="GB-"+str(hour24f)[0:10]+"-"+str(hour24f)[11:13]+'00.csv'
db25="GB-"+str(hour25f)[0:10]+"-"+str(hour25f)[11:13]+'00.csv'

os.system("cp " + db1 + " ~/tmp/" + db1)
os.system("cp " + db2 + " ~/tmp/" + db2)
os.system("cp " + db3 + " ~/tmp/" + db3)
os.system("cp " + db4 + " ~/tmp/" + db4)
os.system("cp " + db5 + " ~/tmp/" + db5)
os.system("cp " + db6 + " ~/tmp/" + db6)
os.system("cp " + db7 + " ~/tmp/" + db7)
os.system("cp " + db8 + " ~/tmp/" + db8)
os.system("cp " + db9 + " ~/tmp/" + db9)
os.system("cp " + db10 + " ~/tmp/" + db10)
os.system("cp " + db11 + " ~/tmp/" + db11)
os.system("cp " + db12 + " ~/tmp/" + db12)
os.system("cp " + db13 + " ~/tmp/" + db13)
os.system("cp " + db14 + " ~/tmp/" + db14)
os.system("cp " + db15 + " ~/tmp/" + db15)
os.system("cp " + db16 + " ~/tmp/" + db16)
os.system("cp " + db17 + " ~/tmp/" + db17)
os.system("cp " + db18 + " ~/tmp/" + db18)
os.system("cp " + db19 + " ~/tmp/" + db19)
os.system("cp " + db20 + " ~/tmp/" + db20)
os.system("cp " + db21 + " ~/tmp/" + db21)
os.system("cp " + db22 + " ~/tmp/" + db22)
os.system("cp " + db23 + " ~/tmp/" + db23)
os.system("cp " + db24 + " ~/tmp/" + db24)
os.system("cp " + db25 + " ~/tmp/" + db25)
