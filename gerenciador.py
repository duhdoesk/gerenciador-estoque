import pymysql
import funcoes_produtos as fprod
import funcoes_materiais as fmat 
import dicionario as dicio

host, user, pw, db, port = 'localhost', 'aplicacao', '123456', 'gerenciamento', 3306
con = pymysql.connect(host, user, pw, db, port)
c = con.cursor(pymysql.cursors.DictCursor)


def time():
	from datetime import datetime
	# localtime = time.asctime( time.localtime(time.time()) )
	localtime = f"{datetime.now():%d/%m/%Y às %H:%M}"
	return str(localtime)

def entrada_produtos(lista_id, lista_quantidade):
	# inserir argumentos em forma de listas com itens tipo int
	i = 0
	while i < len(lista_id):
		# movimentando estoque de produto acabado
		fprod.movimenta_estoque(lista_id[i], lista_quantidade[i], 'soma')

		# inserindo informações no registro
		tempo = time()
		texto = str(tempo + ' - ' + str(lista_quantidade[i]) + ' unidades do produto ' + str(lista_id[i]) + ' foram inseridas no estoque de produto acabado.\n')
		registro(texto)

		# movimentando estoque de materiais
		fmat.baixa_materiais(lista_id[i], lista_quantidade[i])
		i += 1


def saida_produtos(lista_id, lista_quantidade, destino, data = ''):
	# inserir argumentos em forma de listas com itens tipo int
	i = 0
	while i < len(lista_id):
		fprod.movimenta_estoque(lista_id[i], lista_quantidade[i])
		fprod.carga(lista_id[i], lista_quantidade[i], destino, descricao, data)
		# inserindo informações no registro
		tempo = time()
		texto = str(tempo + ' - ' + str(lista_quantidade[i]) + ' unidades do produto ' + str(lista_id[i]) + ' foram expedidas do estoque de produto acabado.\n')
		registro(texto)
		i += 1

def saida_produtos_inter(lista_id, lista_quantidade, lista_destino, lista_descricao, data = ''):
	# inserir argumentos em forma de listas com itens tipo int
	i = 0
	while i < len(lista_id):
		fprod.movimenta_estoque(lista_id[i], lista_quantidade[i])
		fprod.carga(lista_id[i], lista_quantidade[i], lista_destino[i], lista_descricao[i], data)
		# inserindo informações no registro
		tempo = time()
		texto = str(tempo + ' - ' + str(lista_quantidade[i]) + ' unidades do produto ' + str(lista_id[i]) + ' - ' + str(lista_descricao[i]) + ' foram expedidas do estoque de produto acabado.\n')
		registro(texto)
		i += 1


def entrada_materiais(lista_id, lista_quantidades):
	# inserir argumentos em forma de listas com itens tipo str
	i = 0
	while i < len(lista_id):
		fmat.entrada_material(lista_id[i], lista_quantidades[i])
		# inserindo informações no registro
		tempo = time()
		texto = str(tempo + ' - ' + str(lista_quantidades[i]) + ' unidades do material ' + str(lista_id[i]) + ' foram inseridas no estoque de materiais.\n')
		registro(texto)
		i += 1


def registro(texto):
		registro = open('C:/Users/edusc/OneDrive/Área de Trabalho/gerenciador estoque/registro.txt', 'a')
		registro.write(texto)
		registro.close()
		registro = open('C:/Users/edusc/OneDrive/Área de Trabalho/gerenciador estoque/atualizacoes.txt', 'a')
		registro.write(texto)
		registro.close()


def format_list(opcao, estoque, id_item, item, c01='', c02='',c03=''):
	estoque = str(estoque)
	id_item = str(id_item)
	item = str(item)
	c01 = str(c01)
	c02 = str(c02)
	c03 = str(c03)

	if opcao == '1':
		return f'{estoque: <8}{id_item: <10}{item: <24}{c01: <14}{c02: <10}{c03: <10}'
	else:
		return f'{c01: <8}{estoque: <8}{id_item: <10}{item: <24}'


def imprime_lista(tabela, opcao='1'):
	if opcao == '1':
		opcao = 'estoque > 0'
	else:
		opcao = 'estoque >= 0'

	query = 'SELECT * FROM ' + tabela + ' WHERE ' + opcao
	c.execute(query)

	itens = []
	linhas = c.fetchall()
	for linha in linhas:
		itens.append(list(linha.values()))

	if tabela == 'materiais':
		print('\n' + ('#' * 80) + '\n', '\n' + 'Opção: Imprimir lista de materiais em estoque' + '\n')
		print(format_list('2', 'estoque', 'id', 'material', 'minimo') + '\n' + ('-' * 80))
		for item in itens:
			print(format_list('2', item[-2], item[-0], item[1], item[-1]))
		print('\n' + ('#' * 80) + '\n')	
	else:
		print('\n' + ('#' * 80) + '\n', '\n' + 'Opção: Imprimir lista de produtos em estoque' + '\n')
		print(format_list('1', 'estoque', 'id', 'produto', 'condição', 'aba', 'cor') + '\n' + ('-' * 80))
		for item in itens:
			print(format_list('1', item[-1], item[0], item[1], item[2], item[3], item[4]))
		print('\n' + ('#' * 80) + '\n')



def main():

	global c, con

	menu = '9'
	while menu != '0':
		print(
			'Bem vindo ao Gerenciador de Estoques ES 2020!\n\n'
			'Selecione a opção desejada:\n\n'
			'1 - Entrada de Produto Acabado.\n'
			'2 - Expedição de Produto Acabado.\n'
			'3 - Entrada de Materiais / Insumos.\n'
			'4 - Imprimir lista de Produtos em estoque.\n'
			'5 - Imprimir lista de Materiais em estoque.\n'
			'0 - Sair.\n'
			)
		menu = str(input())

		if menu == '1':
			lista_id = []
			lista_quantidade = []
			produto = '1'

			while produto != '0':
				produto = input('Insira o id do produto (ou 0 para encerrar): ')
				if produto != '0':
					quantidade = input('Insira a quantidade do produto a ser inserida: ')
					lista_id.append(str(produto))
					lista_quantidade.append(int(quantidade))

			print('')
			entrada_produtos(lista_id, lista_quantidade)

		if menu == '2':
			data = input('Insira a data referência (opcional): ')
			destino = input('Insira o destino da carga: ')
			lista_id = []
			lista_quantidade = []
			produto = '1'

			while produto != '0':
				produto = input('\nInsira o id do produto (ou 0 para encerrar): ')
				if produto != '0':
					quantidade = input('Insira a quantidade do produto a ser expedida: ')
					lista_id.append(str(produto))
					lista_quantidade.append(int(quantidade))

			print('')
			saida_produtos(lista_id, lista_quantidade, destino, data)

		if menu == '3':
			lista_id = []
			lista_quantidade = []
			produto = '1'

			while produto != '0':
				produto = input('\nInsira o id do material (ou 0 para encerrar): ')
				if produto != '0':
					quantidade = input('Insira a quantidade de material a ser inserido: ')
					lista_id.append(str(produto))
					lista_quantidade.append(int(quantidade))

			print('')
			entrada_materiais(lista_id, lista_quantidade)

		if menu == '4':
			print(
				'Escolha a opção de visualização:\n\n'
				'1 - Somente produtos em estoque\n'
				'2 - Lista Completa\n'
				)
			opcao = str(input())
			print('')
			imprime_lista('produtos', opcao)

		if menu == '5':
			print(
				'Escolha a opção de visualização:\n\n'
				'1 - Somente materiais em estoque\n'
				'2 - Lista Completa\n'
				)
			opcao = str(input())
			print('')
			imprime_lista('materiais', opcao)

		if menu == '0':
			return

# main()