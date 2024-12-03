import smtplib
from email.message import EmailMessage
import schedule
import time


def send_email(recipient, subject, msg):
   GMAIL_ID = '<email id>'
   GMAIL_PWD = '<email pwd>'

   email = EmailMessage()
   email['Subject'] = subject
   email['From'] = GMAIL_ID
   email['To'] = recipient
   email.set_content(msg)

   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail_obj:
       gmail_obj.ehlo()
       gmail_obj.login(GMAIL_ID, GMAIL_PWD)
       gmail_obj.send_message(email)
   print('Email sent to ' + str(recipient) + ' with Subject: \''
         + str(subject) + '\' and Message: \'' + str(msg) + '\'')

msg = 'I am thinking about you'
while True:
    schedule.run_pending()
    time.sleep(86400)
    send_email('<lover's email id>', 'love letter', msg)

