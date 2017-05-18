#!/usr/bin/python
# gb-pack-race.py
#-----------------------------------------------------------
# Points earned by "pack" member between two dates
# and spread 
#-----------------------------------------------------------
import pandas as pd
import os
#import easygui
import glob
import datetime
import csv

 
#os.system('clear')
print'======================================='
print 'GB Range Race'
print'======================================='


os.chdir('/home/juren/Projects/GB/Data')

        
db1 = max([f for f in os.listdir('.') if f.lower().endswith('.csv')], key=os.path.getctime)



print db1[3:18]
day = db1[3:13]

day1f = datetime.date(*[int(i) for i in day.split("-")]) 

one_day = datetime.timedelta(days=1)

day2f= day1f-one_day

db2="GB-"+str(day1f)+'-0000.csv'


# The following routine builds a list of names from the most recent GB*.csv file
with open(db1, 'rb') as csvfile:
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
row = list.index('jimbeaux53') - 25
end = list.index('jimbeaux53') + 20

while row < end:
	
	slist.append(list[row])
	row = row + 1

#print slist

#-----  jimbeaux53 baseline --------

df1 = pd.read_csv(db1,index_col='Name')
jaupts1 = df1.loc['jimbeaux53','Points']
df2 = pd.read_csv(db2,index_col='Name')
jaupts2 = df2.loc['jimbeaux53','Points']



for x in slist:

        name = x
        

	df1 = pd.read_csv(db1,index_col='Name')
	pts1 = df1.loc[name,'Points']
	df2 = pd.read_csv(db2,index_col='Name')
	pts2 = df2.loc[name,'Points']

	rank = df1.loc[name,'Rank']

	print "{:<12}".format(name[:12]),\
	"{:<4}".format(str(rank)[:4]),\
        "{0:>7,}".format(pts1-pts2),\
        "{0:>4,}".format(pts1),\
        "{0:>7,}".format(pts1-jaupts1)

	

	#print "{:<17}".format(name)," ",'\t',\
	#str(rank)[0:4],\
	#"{0:>7,}".format(pts1-pts2),\
	#"{0:>4,}".format(pts1),\
	#"{0:>7,}".format(pts1-jaupts1)








