# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:29:26 2020

@author: Rahul Hegde
"""

"""
imaplib: This module defines three classes, IMAP4, IMAP4_SSL and IMAP4_stream, which 
encapsulate a connection to an IMAP4 server and implement a large subset of the IMAP4rev1
client protocol as defined in RFC 2060.(Internet Message Access Protocol 4)

getpass: Portable password input

pandas: High level data analysis tool and it's key data structure is the dataframe
"""
import imaplib
import email
import getpass
import pandas as pd

username = "email@gmail.com"
password = "password"

mail = imaplib.IMAP4_SSL('imap.gmail.com') #EMail Server
mail.login(username,password)

mail.select("inbox")
result,numbers = mail.uid('search',None,"ALL")
#Requesting all mails in the mailbox

uids = numbers[0].split()
result,messages = mail.uid('fetch',b','.join(uids),'(BODY[])')
#b above indicates typecast to boolean(or else a type error is created). See link below for details
#https://stackoverflow.com/questions/32071536/typeerror-sequence-item-0-expected-str-instance-bytes-found

date_list = []
from_list = []
message_text = []

for _,message in messages[::2]:
    msg = email.message_from_string(message.decode("utf-8"))
    if msg.is_multipart():
        t = []
        for p in msg.get_payload():
            t.append(p.get_payload(decode=True))
        message_text.append(t[0])
    else:
        message_text.append(msg.get_payload(decode=True))
    date_list.append(msg.get('date'))
    from_list.append(msg.get('from'))
    datetime_list = pd.to_datetime(date_list)
    print(len(from_list))
    df = pd.DataFrame(data={'Date':datetime_list,'Sender':from_list,'Message':message_text})
    print(df.head())
    df.to_csv('inbox_email.csv',index=False)
#All the messages are put to the data frame df and also has been redirected to inbox_email.csv 