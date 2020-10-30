import pymysql
import json

host, user, pw, db, port = 'localhost', 'aplicacao', '123456', 'gerenciamento', 3306
con = pymysql.connect(host, user, pw, db, port)
c = con.cursor(pymysql.cursors.DictCursor)

class Item(object):
	def __init__(self, id, product, condition, aba, color, stock):
		self.id = id
		self.product = product
		self.condition = condition
		self.aba = aba
		self.color = color
		self.stock = stock

def product_list(tabela, opcao=''):
	query = 'SELECT * FROM ' + tabela + ' WHERE estoque >0 and classe != "tampo"'
	c.execute(query)

	itens = []
	linhas = c.fetchall()
	for linha in linhas:
		itens.append(list(linha.values()))

	itemobj = []
	for item in itens:
		obj = Item(item[0], item[1], item[2], item[3], item[4], item[5]) #transforma a lista em um objeto c seus att
		itemobj.append(obj) # cria a lista de objetos

	totaljson = []
	for obj in itemobj:
		ajson = retorna_json(obj) # converte o objeto p json
		bjson = replace_none_with_empty_str(ajson)
		totaljson.append(bjson) # lista de objetos json

	return totaljson

def retorna_json(self):
	return { 
		"id" : self.id,
		"product" : self.product,
		"condition" : self.condition,
		"aba" : self.aba,
		"color" : self.color,
		"stock" : self.stock
	}

def replace_none_with_empty_str(some_dict):
	return { k: ("" if v is None else v) for k, v in some_dict.items() }