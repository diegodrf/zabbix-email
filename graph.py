import datetime
import requests
from Auth import Auth

# Função que acessa o gráfico do item para gerar a imagem

def graph(itemname, itemid):
    itemname = itemname
    period = 3600  # 1h
    width = 800
    height = 200
    stime = str(datetime.datetime.now() - datetime.timedelta(hours=1)).replace('-', '').replace(' ', '').replace(':', '').split('.')[0]
    itemid = itemid
    color = '218910'

    # Junta o endereço do servidor com o caminho para o gráfico
    server = Auth.zabbixServer
    url = server + f"/chart3.php?name={itemname}&period={period}&width={width}&height={height}&stime={stime}&items[0][itemid]={itemid}&items[0][drawtype]=5&items[0][color]={color}"

    # Autentica no Zabbix
    user = Auth.zabbixUser
    password = Auth.zabbixPassword
    payload = {'name': user, 'password': password, 'enter': 'Sign in'}

    # Retorna o imagem
    with requests.Session() as s:
        s.post(server + '/index.php', data=payload)
        img = s.get(url)

        return img.content
