import os

# Usuários para autenticação.
# Esse usuário deve ser passado através de variável de ambiente


class Auth:
    zabbixServer = os.getenv('ZABBIXSERVER', 'http://127.0.0.1/zabbix')
    zabbixUser = os.getenv('ZABBIXUSER', 'Admin')
    zabbixPassword = os.getenv('ZABBIXPASSWORD', 'zabbix')
