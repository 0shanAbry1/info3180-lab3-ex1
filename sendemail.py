# Template - Email Sender 

import smtplib

from_name = 'First Last' #Sender's Name
from_addr = 'fromusername@gmail.com' #Sender's Email Address (Must be a GMAIL account)
to_name = 'First Last' #Recipient's Name
to_addr = 'tousername@someemail.com' #Recipient's Email Address (Not limited to any particular account)
subject = 'This is the Subject of the Email' #Email's Subject
msg = 'This is the Message of the Email' #Email's Message

message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

#Credentials
username = 'fromusername@gmail.com' #Sender's Email Address (Must be a GMAIL account)
password = '****************' #Generated Gmail App Password

#Sending Mail
server = smtplib.SMTP('smtp.gmail.com:587') #Gmail's Remote Mail Server & Port
server.starttls() #Start TLS (Transport Layer Security)
server.login(username, password) # Login using Credentials
server.sendmail(from_addr, to_addr, message_to_send) #Blast Off!
server.quit() #Close Connection
