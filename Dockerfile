FROM tiangolo/uwsgi-nginx-flask:python3.7
MAINTAINER "Diego Rodrigues"

# Copia os arquivos do diretório do projeto para o diretório /app
COPY . /app
WORKDIR /app

ENV ZABBIXSERVER "http://127.0.0.1/zabbix"
ENV ZABBIXUSER "Admin"
ENV ZABBIXPASSWORD "zabbix"

# Instala o pacote para Python
RUN pip install -r requirements.txt