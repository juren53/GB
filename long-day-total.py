#!/usr/bin/python
#-----------------------------------------------------------
#      Finds day totals for a selected user w/ a loop
#             Created Mon 19 Sep 2016 07:36:44 PM CDT 
#             Updated Tue 20 Sep 2016 09:17:48 AM CDT 
#-----------------------------------------------------------
import pandas as pd
import os
import easygui
import glob
import numpy as np
from pandas import DataFrame, Series
import datetime
import csv
import math

# os.system('clear')		# clears the screen

print("=======================================")
print("      Day Totals for Last 7 Days ")
print("=======================================")

os.chdir('/home/juren/Projects/GB/Data')


# The following looks for the last CSV file created in the directory
db1 = max([f for f in os.listdir('.') if f.lower().endswith('.csv')], key=os.path.getctime)

# The following routine builds a list of names from the corrected.csv file
with open(db1, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	list = []
	r = 0
	for row in reader:
		r = r+1
		#print ', '.join(row)
		Rank = row[1]
		Name = row[0]
		list.append(Name)


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



print '\t','\t','  ',\
"Rank",\
"  ",db2[8:13],\
"  ",db3[8:13],\
"  ",db4[8:13],\
"  ",db5[8:13],\
"  ",db6[8:13],\
"  ",db7[8:13],\
"  ",db8[8:13],\
"     Total"
	
for x in list:

   try:

        name = x
	

	#------------------------------------------------

	df = pd.read_csv(db1,index_col='Name')
	pts1 = df.loc[name,'Points']
	

	df = pd.read_csv(db2,index_col='Name')

	pts2 = df.loc[name,'Points']


	p1 = pts1-pts2

	rank = df.loc[name,'Rank']

	if math.isnan(rank) == True:
		rank = 9999

	# -------------------------------------------------

	df = pd.read_csv(db2,index_col='Name')
	pts1 = df.loc[name,'Points']


	df = pd.read_csv(db3,index_col='Name')

	pts2 = df.loc[name,'Points']



	p2 = pts1-pts2
	# -------------------------------------------------

	df = pd.read_csv(db3,index_col='Name')
	pts1 = df.loc[name,'Points']


	df = pd.read_csv(db4,index_col='Name')

	pts2 = df.loc[name,'Points']



	p3 = pts1-pts2

	# -------------------------------------------------

	df = pd.read_csv(db4,index_col='Name')
	pts1 = df.loc[name,'Points']


	df = pd.read_csv(db5,index_col='Name')

	pts2 = df.loc[name,'Points']



	p4 = pts1-pts2
	#-------------------------------------------------

	df = pd.read_csv(db5,index_col='Name')
	pts1 = df.loc[name,'Points']


	df = pd.read_csv(db6,index_col='Name')

	pts2 = df.loc[name,'Points']



	p5 = pts1-pts2
	#-------------------------------------------------

	df = pd.read_csv(db6,index_col='Name')
	pts1 = df.loc[name,'Points']


	df = pd.read_csv(db7,index_col='Name')

	pts2 = df.loc[name,'Points']



	p6 = pts1-pts2
	#-------------------------------------------------

	df = pd.read_csv(db7,index_col='Name')
	pts1 = df.loc[name,'Points']


	df = pd.read_csv(db8,index_col='Name')

	pts2 = df.loc[name,'Points']



	p7 = pts1-pts2
	#-------------------------------------------------

 
	print "{:<17}".format(name),"",int(rank)," "\
	"{0:>7,}".format(p1),"",\
	"{0:>7,}".format(p2),"",\
	"{0:>7,}".format(p3),"",\
	"{0:>7,}".format(p4),"",\
	"{0:>7,}".format(p5),"",\
	"{0:>7,}".format(p6),"",\
	"{0:>7,}".format(p7),"  ",\
	"{0:>7,}".format(p1+p2+p3+p4+p5+p6+p7)



   except KeyError, e:
 	  	#return list.next()
	
		continue

