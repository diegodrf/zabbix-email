#!/usr/bin/python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from sys import argv
import graph

def encode(text):
    return text.encode('utf-8')

def send_email(user, password, from_addr, smtp_server, smtp_port, to_addrs, subject, message):

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = to_addrs

    text = MIMEText('Teste')
    msg.attach(text)
    image = MIMEImage(graph.graph())
    msg.attach(image)

    smtpObj = smtplib.SMTP(host=smtp_server, port=smtp_port)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(user=user, password=password)
    # smtpObj.sendmail(from_addr=from_addr, to_addrs=to_addrs, msg=email_body)
    smtpObj.sendmail(from_addr=from_addr, to_addrs=to_addrs, msg=msg.as_string())
    smtpObj.quit()

if __name__ == '__main__':

    """
    Exemplo:

    user = 'monitoramento@solor'
    password = 'XSEfde1sc'
    from_addr = user

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    to_addrs = [fulano@aaa.com, beltrano@bbb.com]
    subject = 'Hello World!'
    message = "<h1>send email html</h1>

    """

    # Usuario
    user = argv[1]
    password = argv[2]
    from_addr = user

    # SMTP server
    smtp_server = argv[3]
    smtp_port = argv[4]

    # Destinatario
    to_addrs = argv[5]
    subject = argv[6]
    # message = argv[7]
    message = ''
    try:
        send_email(user, password, from_addr, smtp_server, smtp_port, to_addrs, subject, message)
        print('OK')
    except Exception as error:
        print(error)