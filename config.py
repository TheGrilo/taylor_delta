#: encoding: utf-8 -*-
import telepot,os,sys,cores

reload(sys)

sys.setdefaultencoding('utf8')
TOKEN = "" ##insira sua token
bot = telepot.Bot(TOKEN)
info_bot = bot.getMe()

nome_bot = info_bot['first_name']
id_bot = info_bot['id']
user_bot = info_bot['username']


cabecalho = cores.branco+"""
================"""+cores.vermelho+"{"+cores.ciano+" Cybion "+cores.vermelho+"}"+cores.branco+"==============="
projeto = cores.ciano+"projeto:"+cores.branco+" Git-Hub"
dev = cores.ciano+"Desenvolvedor: "+cores.branco+"Francis Taylor"
vs = cores.ciano+"versão:"+cores.vermelho+" 1.0"
gp = cores.ciano+"grupo:"+cores.branco+" @RoboTaylor"

iniciado = cores.ciano+"=============="+cores.branco+"{"+cores.ciano+" INICIADO "+cores.branco+"}"+cores.ciano+"==============="
iniciado_nome = cores.branco+"Nome: "+cores.ciano+" {}".format(nome_bot)
iniciado_id = cores.branco+"ID: "+cores.ciano+" {}".format(id_bot)
iniciado_user = cores.branco+"User: "+cores.ciano+" @{}".format(user_bot)
