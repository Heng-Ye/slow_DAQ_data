#import pandas as pd
#import xlrd as xl 
#from pandas import ExcelWriter
#from pandas import ExcelFile

#import math
#import numpy as np
#import matplotlib.pyplot as plt

#from datetime import datetime

import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import matplotlib.ticker as mtick

#from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#from datetime import datetime
#from datetime import datetime, timedelta
from dateutil.parser import parse

file_name='gp_data_0721_top.csv'
file_name2='gp_data_0721_bot.csv'
figName='Evt_Display.png'


majorLocator   = MultipleLocator(20)
xFormatter = FormatStrFormatter('%d')
yFormatter = FormatStrFormatter('%.2f')
minorLocator   = MultipleLocator(5)

n_ch = 6
nch = n_ch*2

lineNum = 0
time = []
time2 = []
x = []
x2 = []
chofchs = [ [], [], [], [], [], [], [], [], [], [], [], [] ]
leg_title = []
color_ch = ['black', 'red', 'orange', 'seagreen', 'blue', 'blueviolet', 'gray', 'deepskyblue', 'fuchsia', 'turquoise', 'sienna', 'greenyellow']

#for i in range(n_ch):
#    print(i+1)

#ch = []
with open(file_name, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        lineNum += 1        
        if lineNum ==2 :
            for jk in range(n_ch):
                leg_title.append(row[jk+1])

        if lineNum > 2:
            time.append(row[0])
            for j in range(n_ch):
                chofchs[j].append(100.*float(row[j+1]))

lineNum2 = 0
with open(file_name2, 'r') as f2:
    reader2 = csv.reader(f2, delimiter=',')
    for row2 in reader2:
        lineNum2 += 1        
        if lineNum2 ==2 :
            for jk2 in range(n_ch):
                leg_title.append(row2[jk2+1])

        if lineNum2 > 2:
            time2.append(row2[0])
            for j2 in range(n_ch):
                chofchs[n_ch+j2].append(100.*float(row2[j2+1]))
    #print(chofchs)
    #print(time)

#Conversion of string of x-axis to time
x = [dt.datetime.strptime(d,'%Y/%m/%d %H:%M:%S.%f') for d in time]
x2 = [dt.datetime.strptime(d,'%Y/%m/%d %H:%M:%S.%f') for d in time2]
#print(x)
print(leg_title)

#draw fig.
plt.figure(figsize=(20,10))
#plt.xlabel('time [us]')
#plt.ylabel('voltage [volt]')
#x_txt=0.8
#y_txt=0.85

#yFormatter = FormatStrFormatter('%.2f')

for k in range(nch):
  #plt.plot(time,chofchs[k], label='testing', color='black', marker='o')

  ax = plt.subplot(3,4,k+1)
  plt.rcParams['axes.grid'] = True
  #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

  plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
  plt.gca().xaxis.set_major_locator(mdates.DayLocator())
  ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
  #plt.gcf().autofmt_xdate()

  # rotates and right aligns the x labels, and moves the bottom of the
  # axes up to make room for them
  #plt.gcf().autofmt_xdate()
 
  #plt.plot(x[:-1], chofchs[k][:-1], label=leg_title[k])
  if k < n_ch:
    plt.plot(x[:-1], chofchs[k][:-1], label='{}'.format(leg_title[k]), color=color_ch[k])
  else :
    plt.plot(x2[:-1], chofchs[k][:-1], label='{}'.format(leg_title[k]), color=color_ch[k])

  plt.legend(loc="upper right")
  #plt.ylim([ymin[11],ymax[11]])
  if k==0 :
    plt.ylabel("Voltage [mV]")

  if k==nch-1 :
    plt.xlabel("Time")


# show plot
plt.show()




plt.savefig(figName)

#data = pd.read_csv(file_name, sheet_name="gp_data1")

#print("Column headings:")
#print(data.columns)

#n_row=data.shape[0] #gives number of row count
#n_col=data.shape[1] #gives number of col count

#print("number of rows: ", n_row)
#print("number of columns: ", n_col)
#ncol = data.ncols

