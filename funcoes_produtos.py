import pymysql
import time
from datetime import date

host, user, pw, db, port = 'localhost', 'aplicacao', '123456', 'gerenciamento', 3306
con = pymysql.connect(host, user, pw, db, port)
c = con.cursor(pymysql.cursors.DictCursor)


def carga(id_produto, quantidade, destino, descricao, data= ''):
	global c, con

	if not (data):
		data = date.today()

	query = str('(DEFAULT, "' + str(data) + '", "' + str(destino) + '", "' + str(id_produto) + '", "' + str(quantidade) + '", "' + str(descricao) + '"')
	query = 'INSERT INTO cargas VALUES ' + query + ')'

	c.execute(query)
	con.commit()


def movimenta_estoque(id_produto, quantidade, operacao='subtração'):
	global c, con

	estoque = retorna_estoque(id_produto)

	if operacao == 'subtração':
		novo_estoque = calcula_estoque(estoque, quantidade)
	elif operacao == 'soma':
		novo_estoque = calcula_estoque(estoque, quantidade, '+')
	
	if novo_estoque >= 0:
		query = 'UPDATE produtos SET estoque = "' + str(novo_estoque) + '" WHERE (id_produto = "' + str(id_produto) + '")'
		c.execute(query)
		con.commit()
	else:
		return 'o volume a ser expedido é maior do que há no estoque'


def retorna_estoque(id_produto):
	global c, con
	
	query = 'SELECT estoque FROM produtos WHERE (id_produto = "' + str(id_produto) + '")'
	c.execute(query)
	
	estoque = c.fetchone()
	estoque = estoque['estoque']
	
	return estoque


def calcula_estoque(estoque, quantidade, operador='-'):
	if operador == '-':
		novo_estoque = int(estoque) - int(quantidade)
		return novo_estoque
	elif operador == '+':
		novo_estoque = int(estoque) + int(quantidade)
		return novo_estoque