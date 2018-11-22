#!/usr/bin/python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from regexs import get_itemName, get_itemID
from graph import graph


# Função para codificar o texto recebido em utf-8
def encode(text):
    return text.encode('utf-8')

# Função que monta o e-mail e envia.
def send_email(user, password, from_addr, smtp_server, smtp_port, to_addrs, subject, message):

    # Parse do ID e nome do item
    itemName = get_itemName(message)
    itemID = get_itemID(message)

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = to_addrs

    text = MIMEText(message, 'html')
    msg.attach(text)

    # Só anexa a imagem se a mesma for encontrada
    if (itemName or itemID) is not None:
        image = MIMEImage(graph(itemName, itemID), 'png')
        image.add_header('Content-ID', '<image1>')
        image.add_header('Content-Disposition', 'inline', filename='graph.png')
        msg.attach(image)

    smtpObj = smtplib.SMTP(host=smtp_server, port=smtp_port)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(user=user, password=password)
    smtpObj.sendmail(from_addr=from_addr, to_addrs=to_addrs, msg=msg.as_string())
    smtpObj.quit()
