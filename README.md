**Este recurso faz parte do magic_stack**

## Ordem de montagem:

* URL para container
* email do remetente
* senha do remetente
* servidor smtp
* port do servidor mtp
* usuário de destino
* assunto
* mensagem

## Para executar

`docker container run --rm --name zabbix-email -d -p 8002:80 -e ZABBIXSERVER="http://URL_DO_ZABBIX/zabbix" -e ZABBIXUSER="USUARIO_DO_ZABBIX" -e ZABBIXPASSWORD="SENHA_DO_ZABBIX" diegodrf/zabbix-email:latest`