#!/usr/bin/python
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

def send_mail(send_from,send_to,subject,text,files,server,port,username='lanemcunningham@gmail.com',password='Enfectme.87',isTls=True):
    msg = MIMEMultipart()
    msg['From'] = "lanemcunningham@gmail.com"
    msg['To'] = "lanemcunningham@gmail.com"
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = "Test"
    msg.attach(MIMEText("messageText"))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("results.txt", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="results.txt"')
    msg.attach(part)

    #context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
    #SSL connection only working on Python 3+
    smtp = smtplib.SMTP(server, port)
    if isTls:
        smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
