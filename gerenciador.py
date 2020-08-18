import MySQLdb
import funcoes_produtos as fprod
import funcoes_materiais as fmat 

host, user, pw, db, port = 'localhost', 'aplicacao', '123456', 'gerenciamento', 3306
con = MySQLdb.connect(host, user, pw, db, port)
c = con.cursor(MySQLdb.cursors.DictCursor)


def entrada_produtos(lista_id, lista_quantidade):
	# inserir argumentos em forma de listas com itens tipo int
	i = 0
	while i < len(lista_id):
		fprod.movimenta_estoque(lista_id[i], lista_quantidade[i], 'soma')
		fmat.baixa_materiais(lista_id[i], lista_quantidade[i])
		i += 1


def saida_produtos(lista_id, lista_quantidade):
	# inserir argumentos em forma de listas com itens tipo int
	i = 0
	while i < len(lista_id):
		fprod.movimenta_estoque(lista_id[i], lista_quantidade[i])
		i += 1


def entrada_materiais(lista_id, lista_quantidades):
	# inserir argumentos em forma de listas com itens tipo str
	i = 0
	while i < len(lista_id):
		fmat.entrada_material(lista_id[i], lista_quantidades[i])
		i += 1