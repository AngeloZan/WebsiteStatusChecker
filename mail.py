'''email sender module'''
from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

load_dotenv() # loading .env variables containing email info

class Mail():
    '''Mail class'''
    def __init__(self, msg_subject, msg_content):
        self.msg_subject = msg_subject
        self.msg_content = msg_content
    
    def send(self):
        '''sends the email'''
        from_email = os.getenv('SENDER')
        from_password = os.getenv('SENDER_PWD')
        to_email = os.getenv('RECEIVER')
        msg = EmailMessage()
        msg.set_content(self.msg_content)
        msg['Subject'] = self.msg_subject
        msg['From'] = from_email
        msg['To'] = to_email

        # sending the email
        server = smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT'))
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
