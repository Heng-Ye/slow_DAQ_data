#DCS Event display for ground planes 

import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import matplotlib.ticker as mtick

from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from dateutil.parser import parse

#input csv files & ouput file name
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

x = [dt.datetime.strptime(d,'%Y/%m/%d %H:%M:%S.%f') for d in time]
x2 = [dt.datetime.strptime(d,'%Y/%m/%d %H:%M:%S.%f') for d in time2]
print(leg_title)

#draw fig.
plt.figure(figsize=(20,10))

for k in range(nch):

  ax = plt.subplot(3,4,k+1)
  plt.rcParams['axes.grid'] = True

  plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
  plt.gca().xaxis.set_major_locator(mdates.DayLocator())
  ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

  if k < n_ch:
    plt.plot(x[:-1], chofchs[k][:-1], label='{}'.format(leg_title[k]), color=color_ch[k])
  else :
    plt.plot(x2[:-1], chofchs[k][:-1], label='{}'.format(leg_title[k]), color=color_ch[k])

  plt.legend(loc="upper right")
  if k==0 :
    plt.ylabel("Voltage [mV]")
  if k==nch-1 :
    plt.xlabel("Time")

# show plot & save figure
plt.show()
plt.savefig(figName)
