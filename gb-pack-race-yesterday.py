#!/usr/bin/python
# gb-pack-race.py
#-----------------------------------------------------------
# Points earned by "pack" member between two dates
# and spread 
#-----------------------------------------------------------
import pandas as pd
import os
import easygui
import glob
import datetime


 
#os.system('clear')
print'======================================='
print 'GB Pack Race'
print'======================================='


os.chdir('/home/juren/Projects/GB/Data')


db1 = max([f for f in os.listdir('.') if f.lower().endswith('.csv')], key=os.path.getctime)

db1 = db1[0:13]+'-0000.csv'        # Rebuilds most recent filename at midnite


print db1[3:18]
day = db1[3:13]

day1f = datetime.date(*[int(i) for i in day.split("-")]) 

one_day = datetime.timedelta(days=1)

day2f= day1f-one_day

db2="GB-"+str(day2f)+'-0000.csv'


lines = []
with open('list.csv', 'r') as f:
    for line in f.readlines():
        l,name = line.strip().split(',')
        lines.append((l,name))


pack = []
with open('list.txt', 'r') as f:
    for line in f.readlines():
        l,name = line.strip().split(',')
        pack.append((l,name))



#-----  jimbeaux53 baseline --------

df1 = pd.read_csv(db1,index_col='Name')
jaupts1 = df1.loc['jimbeaux53','Points']
df2 = pd.read_csv(db2,index_col='Name')
jaupts2 = df2.loc['jimbeaux53','Points']



for x in pack:

        name = x[1]
        

	df1 = pd.read_csv(db1,index_col='Name')
	pts1 = df1.loc[name,'Points']
	df2 = pd.read_csv(db2,index_col='Name')
	pts2 = df2.loc[name,'Points']
	
	print name," ",'\t',\
	"{0:>7,}".format(pts1-pts2),\
	"{0:>4,}".format(pts1),\
	"{0:>8,}".format(pts1-jaupts1)








