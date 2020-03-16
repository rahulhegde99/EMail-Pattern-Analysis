# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:30:03 2020

@author: Rahul Hegde
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 18:00:13 2020

@author: Rahul Hegde
"""

"""
https://stackoverflow.com/questions/9439480/from-import-vs-import

Something helpful
"""

#Now lets visualise this data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from scipy import stats
from scipy.stats import kde

email_data = pd.read_csv('inbox_email.csv')

#Length of each message will be calculated and appended to the dataframe as a new column
leng_list = []
for msg in email_data['Message']:
    if isinstance(msg,str):
        leng_list.append(len(msg))
    else:
        leng_list.append(0)
email_data["MsgLen"] = leng_list

FMT = '%H:%M:%S'
email_data['Time'] = email_data['Date'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S%z').strftime(FMT))#%z is the timezone
email_data['SinceMidnight'] = email_data['Time'].apply(lambda x: (datetime.strptime(x, FMT) - datetime.strptime("00:00:00", FMT)).seconds)/60/60
#Time since midnight is calculated and appended to dataframe as a new column

#Textual Statistics
print("Number of messages recieved is",len(email_data['Sender']))
print("Number of unique senders is",email_data['Sender'].nunique())
print("Maximum message length is",email_data['MsgLen'].max(),"characters")
print("Average message length is",email_data['MsgLen'].mean(),"characters")
print("All the senders are")
print(email_data['Sender'].unique())

#Histogram
plt.hist(email_data['SinceMidnight'])
plt.title('DISTRIBUTION OF EMAILS RECEIVED THROUGHOUT THE DAY')
plt.xlabel('Time')
plt.ylabel('Number of Mails')
plt.savefig('MailDensity.png', bbox_inches='tight')
plt.show()

#Histogram
plt.hist(email_data['MsgLen'])
plt.title('DISTRIBUTION OF MESSAGE LENGTHS')
plt.xlabel('Message Length')
plt.ylabel('Number of Mails')
plt.savefig('MessageLength.png', bbox_inches='tight')
plt.show()


#Kernel Density Plot
nbins=400
k = kde.gaussian_kde([email_data['MsgLen'],email_data['SinceMidnight']])
xi, yi = np.mgrid[email_data['MsgLen'].min():email_data['MsgLen'].max():nbins*1j, email_data['SinceMidnight'].min():email_data['SinceMidnight'].max():nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))
plt.pcolormesh(xi, yi, zi.reshape(xi.shape))
plt.colorbar()
plt.xlabel('Message Length')
plt.ylabel('Time')
plt.title('2D Kernel Density Estimate')
#plt.axis([email_data['MsgLen'].min(),email_data['MsgLen'].max(),email_data['SinceMidnight'].min(),email_data['SinceMidnight'].max()])
plt.tight_layout()
plt.savefig('KDPlot.png', bbox_inches='tight')
plt.show()

slope, intercept, r_value, p_value, std_err = stats.linregress(email_data["SinceMidnight"],
email_data["MsgLen"])
print("Slope:", slope)
print("Standard Error:", std_err)
print("P Value:", p_value)
print("r-squared", r_value**2)











