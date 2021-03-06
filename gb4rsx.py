#!/usr/bin/python3
#-----------------------------------------------------------
#        Computes day totals for a range of  users 
#        with average and trunkated mean computed per day. 
#        Updated Sun 10 Nov 2019 05:35:56 PM CST 
#        gb4rsx.py   
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
print("      Day Totals for Last 7 Days       ",db1[3:18])
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

#print db1,db2,db3,db4,db5    

#"gb4rsx.py,"

print('gb4rsx.py         ',\
"",db2[8:13],\
"  ",db3[8:13],\
"  ",db4[8:13],\
"  ",db5[8:13],\
"  ",db6[8:13],\
"  ",db7[8:13],\
"  ",db8[8:13],\
"     Total",\
"      Ave",\
" T-Mean")
    
for x in slist:

    name = x 

    #------------------------------------------------

    df = pd.read_csv(db1,index_col='Name')
    pts1 = df.loc[name,'Points']
    
    df = pd.read_csv(db2,index_col='Name')
    #print db2[3:13],
    pts2 = df.loc[name,'Points']

    #print "Points =",pts1-pts2
    p1 = pts1-pts2
    # -------------------------------------------------

    df = pd.read_csv(db2,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db3,index_col='Name')
    #print db3[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p2 = pts1-pts2
    # -------------------------------------------------

    df = pd.read_csv(db3,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db4,index_col='Name')
    #print db4[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p3 = pts1-pts2

    # -------------------------------------------------

    df = pd.read_csv(db4,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db5,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p4 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db5,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db6,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p5 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db6,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db7,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p6 = pts1-pts2
    #-------------------------------------------------

    df = pd.read_csv(db7,index_col='Name')
    pts1 = df.loc[name,'Points']


    df = pd.read_csv(db8,index_col='Name')
    #print db5[3:13],
    pts2 = df.loc[name,'Points']


    #print "Points =",pts1-pts2
    p7 = pts1-pts2
    #-------------------------------------------------
   
    a=p1+p2+p3+p4+p5+p6+p7
    ave=a

    in_array = [int(p1),int(p2),int(p3),int(p4),int(p5),int(p6),int(p7)]
    out_array = np.clip(in_array, a_min = 0, a_max = 3000)
    # t-mean=int(np.mean(out_array))


    print("{:<17}".format(name),\
    "{0:>7,}".format(p1),"",\
    "{0:>7,}".format(p2),"",\
    "{0:>7,}".format(p3),"",\
    "{0:>7,}".format(p4),"",\
    "{0:>7,}".format(p5),"",\
    "{0:>7,}".format(p6),"",\
    "{0:>7,}".format(p7),"  ",\
    "{0:>7,}".format(p1+p2+p3+p4+p5+p6+p7)," ",\
    "{0:>7,}".format(int((p1+p2+p3+p4+p5+p6+p7)/7)),\
    "{0:>7,}".format(int(np.mean(out_array))))






    
