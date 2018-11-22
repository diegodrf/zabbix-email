import os

# Usuários para autenticação.
# Esse usuário deve ser passado através de variável de ambiente


class Auth:
    zabbixServer = os.getenv('ZABBIXSERVER', 'http://docker.westus2.cloudapp.azure.com/zabbix')
    zabbixUser = os.getenv('ZABBIXUSER', 'Admin')
    zabbixPassword = os.getenv('ZABBIXPASSWORD', 'zabbix')
