#!/usr/bin/python
#-----------------------------------------------------------
#      Finds common GB Users in a selected timeframe        
#-----------------------------------------------------------
import pandas as pd
import os
import easygui
import glob
import numpy as np
from pandas import DataFrame, Series



#os.system('clear')		# clears the screen

print("=======================================")
print("Find common GB users between two data files")
print("=======================================")

os.chdir('/home/juren/Projects/GB/Data')


# following two lines creates GUI choice box allowing user to choose files from current 
# directory 
db1 = max([f for f in os.listdir('.') if f.lower().endswith('.csv')], key=os.path.getctime)
print db1
#db2 = easygui.fileopenbox(title="Ending Data File ", filetypes = [glob.glob("GB*.*")])
db2 = db1[0:13]+'-0000.csv'
print db2

df1 = pd.read_csv(db1,index_col='Name')
df2 = pd.read_csv(db2,index_col='Name')


result = pd.merge(df1, df2, right_index=True, left_index=True)
#result = pd.merge(df1, df2, right_index=True, left_index=True, how='inner')
#result = pd.merge(left=df1,right=df2, left_on='Name', right_on='Name')

# print(result)

print("=======================================")
df3 = result

df3["Points"] = result["Points_x"]-result["Points_y"]

df3 = df3.drop('Rank_x', 1)		# Delete col
#df3 = df3.drop('Rank_y', 1)		# Delete col
df3 = df3.drop('Location_y', 1)		# Delete col
df3 = df3.drop('Points_x', 1)		# Delete col


print df3.loc[:'jimbeaux53']
#print df3.iloc[50:60]

#print df3.index.get_loc[jimbeaux53]

print("=======================================")

#print db1[32:47] # extracts the date embedded in the filename and prints it
print db1
#print db2[32:47]# extracts the date embedded in the filename and prints it
print db2
print("=======================================")
