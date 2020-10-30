import pymysql
import json

host, user, pw, db, port = 'localhost', 'aplicacao', '123456', 'gerenciamento', 3306
con = pymysql.connect(host, user, pw, db, port)
c = con.cursor(pymysql.cursors.DictCursor)

class Item(object):
	def __init__(self, id, material, estoque, est_min, est_mes):
		self.id = id
		self.material = material
		self.estoque = estoque
		self.est_min = est_min
		self.est_mes = est_mes

def material_list(tabela, filtro=''):
	if filtro:
		query = 'SELECT * FROM materiais WHERE nome LIKE "%' + filtro + '%" OR id_material LIKE "%' + filtro + '%" ORDER BY estoque_mes'
	else:
		query = 'SELECT * FROM ' + tabela + ' ORDER BY estoque_mes'
	
	c.execute(query)

	itens = []
	linhas = c.fetchall()
	for linha in linhas:
		itens.append(list(linha.values()))

	itemobj = []
	for item in itens:
		obj = Item(item[0], item[1], item[2], item[3], item[4]) #transforma a lista em um objeto c seus att
		itemobj.append(obj) # cria a lista de objetos

	totaljson = []
	for obj in itemobj:
		ajson = retorna_json(obj) # converte o objeto p json
		bjson = replace_none_with_empty_str(ajson)
		totaljson.append(bjson) # lista de objetos json

	return totaljson

def retorna_json(self):
	return { 
		"material" : self.material,
		"estoque" : self.estoque,
		"est_min" : self.est_min,
		"est_mes" : self.est_mes
	 }

def replace_none_with_empty_str(some_dict):
	return { k: ("" if v is None else v) for k, v in some_dict.items() }