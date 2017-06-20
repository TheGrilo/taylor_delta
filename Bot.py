#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# encoding: utf-8

import time,random,sys,datetime,cores,os,telepot,config
os.system("clear")
reload(sys)
sys.setdefaultencoding('utf8')
##########( configurações )########
today = datetime.datetime.today()
hora = today.strftime("[%H:%M] - ")
bot = config.bot
NomeBot = config.nome_bot

print(config.iniciado)
print(config.iniciado_nome)
print(config.iniciado_user)
print(config.iniciado_id)
time.sleep(2)
def handle(msg):
#############( parâmetros ) ###########
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == "new_chat_member":  
        bot.sendMessage(chat_id, " Bem vindo(a) ao *{}*", "Markdown")
         
    chat_id = msg['chat']['id']
    try:nome_chat = msg['chat']['title']
    except: " "
    tipo = msg['chat']['type']
    privado = "private"
    grupo = "supergroup"
    from_id = msg['from']['id']
    nome = msg['from']['first_name']
    try:user = msg['from']['username']
    except: " "
    cmd = msg['text']
    send = bot.sendMessage
    markdown = "Markdown"
    msg_id = msg['message_id']
    print("\n"+cores.vermelho + hora + cores.ciano + 'Mensagem executada: %s' % cores.vermelho + cmd + cores.original)
#############( comandos )##############
    if cmd == "/start":
        send(chat_id, "Olá! *{}*\n sou o `{}`". format(nome, config.nome_bot), markdown)
    elif cmd == "/id":
        send(chat_id, "Nome: *{}*\nUsername:` @{}`\nId: `{}`".format(nome,user,id), msrkdown)
    elif cmd == "/chat":
        if tipo == privado:
            send(chat_id, " apenas em grupos")
        else:
            send(chat_id, "Nome: {}\nId: {}\nMensagens: {}".format(nome_chat, chat_id, msg_id))


os.system("clear")
#########( start )########
print(config.cabecalho)
print(config.projeto)
print(config.dev)
print(config.vs)
print(config.gp)
time.sleep(2)
bot.message_loop(handle)
while 1:
    time.sleep(10)
