# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:49:45 2021

@author: Prinzessin
"""

from datetime import datetime
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import figure

from pathlib import Path

import os, glob

# example of string to date time
# year-month-day | H:M:S.MS
mag_time = "1989-08-30T00:00:00.691Z"
date_time = datetime.strptime(mag_time, "%Y-%m-%dT%H:%M:%S.%fZ")
print("date and time:", date_time)


# example of numbers to date time
# year | day of year | hour | minute | second | ms
mag_time = "1989 236 18 0 0 557"
date_time = datetime.strptime(mag_time, "%Y %j %H %M %S %f")
print("date and time:", date_time)


# start here
whole_line = " 89 236 18  0 48 557  26.4105 -24.83 217.23    -0.41     0.46    -1.16"

# split data
data_list = whole_line.split(" ")

# delete all empty entries
data_list = list(filter(None, data_list))

# replace 89 with 1989 in entry zero
data_list[0] = data_list[0].replace("89", "1989")

# print list
print(data_list)

# get all date related entries and concatenate
date_of_list = data_list[0] + " " + data_list[1] + " " + data_list[2] + " " + data_list[3] + " " + data_list[4] + " " + data_list[5]

# year, julian day, hour, minute, second, fraction of second
a = datetime.strptime(date_of_list, "%Y %j %H %M %S %f")
print(a)

# path from python file to data
file_path = "ASCII/COMPREHE.ASC"

# r for read
data_file = open(file_path, "r")

"""
COMPREHE:
0 %YR% 
1 %DOY% 
2 %HR% 
3 %MIN% 
4 %SEC% 
5 %MSEC%
6 Range: Spacecraft range from the Neptune center of mass measured in Neptune radii where Rn = 24765 km
7 Latitude: Spacecraft planetocentric (Neptune)latitude, measured in degrees.
8 Longitude: Spacecraft planetographic (Neptune)longitude (west), measured in degrees.
9 Br: Radial component of the magnetic field
10 Btheta: Southward magnetic field component
11 Bphi: Azimuthal magnetic field component
"""

"""
INTERNAL:
0 Range: Spacecraft position vector radial component in units of Neptune radii where 1 Rn = 24,765km.
1 Theta: Theta component of spacecraft in radians
2 Phi: Phi component of spacecraft in radians
3 B_component: Value of the component of the magnetic field according to the type column
4 SIGMA: Estimated standard deviation of the observation in units on nT.
5 TYPE: 1 = Radial component, 2 = Theta component, 3 = Phi component, 4 = Magnitude of the magnetic field.
"""

whole_data = []

for row_number, data in enumerate(data_file):
    
    row_data = []
    
    # print(row_number)
    # print(data)
    
    # split data
    data = data.split(" ") # ****
    
    # delete all empty entries
    data = list(filter(None, data))
    
    # replace 89 with 1989 in entry zero
    data[0] = data[0].replace("89", "1989")
    
    # print list
    # print(data)
    
    # get all date related entries and concatenate
    date_data = data[0] + " " + data[1] + " " + data[2] + " " + data[3] + " " + data[4] + " " + data[5]
    
    # year, julian day, hour, minute, second, fraction of second
    a = datetime.strptime(date_data, "%Y %j %H %M %S %f")
    # print(a)
    
    row_data.append(row_number) # ****************
    row_data.append(a)
    row_data.append(float(data[6]))
    
    whole_data.append(row_data)

# print(whole_data)


column_names = ["id", "date", "br"] # ************
df = pd.DataFrame(whole_data, columns=column_names)

print(df.info())
print(df.head())
print(df["br"].describe())

df.drop(df[df['br'] == 9999.99].index, inplace = True)

#df = df.loc[2500:3500]

print(df["br"].max())
print(df["br"].min())

days = df["date"]
y_BR = df["br"]

plt.figure(1)
axis = plt.gca()
#axis.set_ylim(-0.12, 0.2)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d,%H'))

plt.yticks(np.arange(10000, -2000, step=-500))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
#plt.plot(days,)
plt.plot(days, y_BR, 'b+', label="BR")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
#plt.plot(days,y_BMAG, 'y+')

#plt.scatter(days, y)
plt.gcf().autofmt_xdate()
plt.show()




# nicht mehr abschreiben:
'''
# COLUMN NAMES
p = os.path.abspath('..')
path = os.path.join(p, "data/VG2_N_MAG/DATA/ASCDATA.FMT")

# Get the column names
column_names = []
f = open(path, "r")
for x in f:
    if "NAME" in x:
        s = x.split('"')
        column_names.append(s[1])
        #print(s[1])

column_names.remove("DFLAG")
print("Column names: ", column_names)


# DATA
whole_data = []
row_data = []
data = []

file1 = os.path.join(p, "data/VG2_N_MAG/DATA/T890822_ASC.TAB")
file2 = os.path.join(p, "data/VG2_N_MAG/DATA/T890823_ASC.TAB")
file3 = os.path.join(p, "data/VG2_N_MAG/DATA/T890824_ASC.TAB")
file4 = os.path.join(p, "data/VG2_N_MAG/DATA/T890825_ASC.TAB")
file5 = os.path.join(p, "data/VG2_N_MAG/DATA/T890826_ASC.TAB")
file6 = os.path.join(p, "data/VG2_N_MAG/DATA/T890827_ASC.TAB")
file7 = os.path.join(p, "data/VG2_N_MAG/DATA/T890828_ASC.TAB")
file8 = os.path.join(p, "data/VG2_N_MAG/DATA/T890829_ASC.TAB")
file9 = os.path.join(p, "data/VG2_N_MAG/DATA/T890830_ASC.TAB")

print(path)
    
"""
files = []

import os
for file in os.listdir(path):
    if file.endswith(".TAB"):
        #print("Hi")
        file_path = os.path.join(path, file)
        #print(file_path)
        files.append(file_path)
print(files)
"""

data_path = os.path.abspath('../data/VG2_N_MAG/DATA/')
print(data_path)
for file in os.listdir(data_path):
    if file.endswith(".TAB"):
        print(file)
        file_path = os.path.join(data_path, file)
        print(file_path)
        data_file = open(file_path, "r")
        print(data_file)
        for index2, x in enumerate(data_file):
            
            x = x.replace (" ", "")
            x = x.replace (",\n", "")
            data = x.split(',')
                
            # print("*****", data)
            
            
            for index, col in enumerate(column_names):    
                
                # print("here", data[index])
                
                if(col == "PDSTIME"):
                    try:
                        data[index] = datetime.strptime(data[index], "%Y-%m-%dT%H:%M:%S.%fZ")
                        row_data.append(data[index])
                    except:
                        print(data[index])
                        # data[index] = datetime.strptime(data[index], "%Y-%m-%dT%H:%M:%S.%fZ")
                    #print(data[index])
                    
                else:        
                    row_data.append(float(data[index]))
                
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

print("Describe:")
print(df.describe())



"""
time = [0, 1, 2, 3]
position = [0, 100, 500, 300]

plt.plot(time, position)
plt.xlabel('Time (sec)')
plt.ylabel('Position (km)')

plt.show()
"""


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
from matplotlib.pyplot import figure


figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

N = 100
y = np.random.rand(N)

#df = df.loc[0:600]

df = df[df.index % 10 == 0]



days = df["PDSTIME"]
y_BR = df['BR']
y_BT = df['BT']
y_BN = df['BN']
y_BMAG = df['BMAG']


print(y_BN)

plt.figure(1)
axis = plt.gca()
#axis.set_ylim(-0.12, 0.2)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d,%H'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
#plt.plot(days,)
plt.plot(days,y_BT, 'b+', label="BT - TANGENTIAL MAG COMPONENT")
plt.plot(days,y_BN, 'g+', label="BN - NORMAL MAG COMPONENT")
plt.plot(days,y_BR, 'r+', label="BR - RADIAL MAG COMPONENT")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
#plt.plot(days,y_BMAG, 'y+')

#plt.scatter(days, y)
plt.gcf().autofmt_xdate()
plt.show()




y_delta = df['DELTA']
y_lambda = df['LAMBDA']
y_npts = df['NPTS']

plt.figure(2)
figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
axis = plt.gca()
#axis.set_ylim(-0.12, 0.2)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d,%H'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
#plt.plot(days,)
plt.plot(days, y_delta, 'r*')
plt.plot(days, y_lambda, 'b+')
plt.plot(days, y_npts, 'go')

#plt.scatter(days, y)
plt.gcf().autofmt_xdate()
plt.show()





"""

ax = plt.subplot(111)
t1 = np.arange(0.0, 1.0, 0.01)

for n in [1, 2, 3, 4]:
    plt.plot(t1, t1**n, label=f"n={n}")

leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)
"""



        
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
#'''
