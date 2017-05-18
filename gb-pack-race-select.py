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


 
os.system('clear')
print'======================================='
print 'GB Pack Race'
print'======================================='

os.chdir('/home/juren/Projects/GB/Data')

db1 = easygui.fileopenbox(title="Beginning Data File ", filetypes = [glob.glob("GB*.*")])
print db1
db2 = easygui.fileopenbox(title="Ending Data File ", filetypes = [glob.glob("GB*.*")])
print db2

#-----  jimbeaux53 baseline --------

df1 = pd.read_csv(db1,index_col='Name')
jaupts1 = df1.loc['jimbeaux53','Points']
df2 = pd.read_csv(db2,index_col='Name')
jaupts2 = df2.loc['jimbeaux53','Points']

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
        
	rank = df2.loc[name,'Rank']

	df1 = pd.read_csv(db1,index_col='Name')
	pts1 = df1.loc[name,'Points']
	df2 = pd.read_csv(db2,index_col='Name')
	pts2 = df2.loc[name,'Points']
	
	#print name," ",'\t',"{0:>5,}".format(pts1-pts2),"{0:>4,}".format(pts1),"{0:>7,}".format(pts1-jaupts1)

	print "{:<12}".format(name[:12]),\
	"{:<4}".format(str(rank)[:4]),\
        "{0:>7,}".format(pts1-pts2),\
        "{0:>4,}".format(pts1),\
        "{0:>8,}".format(pts1-jaupts1)






