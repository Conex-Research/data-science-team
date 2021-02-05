# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:49:45 2021

@author: Prinzessin
"""

from datetime import datetime
import pandas as pd
import numpy as np

from pathlib import Path

import os

mag_time = "1989-08-30T00:00:00.691Z"


date_time = datetime.strptime(mag_time, "%Y-%m-%dT%H:%M:%S.%fZ")
print("date and time:",date_time)


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

p = os.path.abspath('..')
print(p)
print(os.path.join(p, "\data\VG2_N_MAG\DATA\ASCDATA.FMT")) 

# Get the column names
column_names = []
f = open("C://", "r")
for x in f:
    if "NAME" in x:
        s = x.split('"')
        column_names.append(s[1])
        #print(s[1])

column_names.remove("DFLAG")
print(column_names)


whole_data = []
row_data = []
data = []
data_file = open("C://Users\Prinzessin\Downloads\VG2-N-MAG-4-RDR-HGCOORDS-1.92SEC-V1.0\DATA\T890822_ASC.TAB", "r")
for index2, x in enumerate(data_file):
    
    x = x.replace (" ", "")
    x = x.replace (",\n", "")
    data = x.split(',')
        
    # print("*****", data)
    
    
    for index, col in enumerate(column_names):    
        
        # print("here", data[index])
        
        if(col == "PDSTIME"):
            data[index] = datetime.strptime(data[index], "%Y-%m-%dT%H:%M:%S.%fZ")
            row_data.append(data[index])
        else:        
            row_data.append(float(data[index]))
        
        # break
        
    #break
    whole_data.append(row_data)
    row_data = []
    

df = pd.DataFrame(whole_data, columns=column_names)

df.dropna()

df.drop(df[df['BN'] >= 999].index, inplace = True)

df.drop(df[df['BT'] >= 999].index, inplace = True)
df.drop(df[df['BR'] >= 999].index, inplace = True)
df.drop(df[df['BMAG'] >= 999].index, inplace = True)

df.drop(df[df['BR_RMS'] >= 999].index, inplace = True)
df.drop(df[df['BT_RMS'] >= 999].index, inplace = True)
df.drop(df[df['BN_RMS'] >= 999].index, inplace = True)

#print(df.head(50))

print(df.describe())


        
    #whole_data.append(row_data) 

        
        #for a in data:
        #    row_data.append(a)
        #print(x)
        #whole_data.append(row_data)
        #break
            

#df = pd.DataFrame(whole_data, columns=column_names)

#print(df.head())

#row_data.columns = column_names

#all = pd.DataFrame(list(zip(column_names, row_data)))  
#print(all)    

#row = df.loc['NAME']


#for index, row in df.iterrows():
#   if "NAME" in str(row).upper():
#        print(row)


"""
for ij in np.ndindex(df.shape[:2]):
    print(ij, df[ij])
"""