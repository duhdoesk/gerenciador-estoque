import MySQLdb
import funcoes_produtos as fprod 
import dicionario as dicio 

host, user, pw, db, port = 'localhost', 'aplicacao', '123456', 'gerenciamento', 3306
con = MySQLdb.connect(host, user, pw, db, port)
c = con.cursor(MySQLdb.cursors.DictCursor)


def entrada_material(id_material, quantidade):
	atualiza(id_material, quantidade, '+')


def baixa_materiais(id_produto, quantidade):
	global c, con

	classe = retorna_classe(id_produto)

	if classe == 'Mesa':
		materiais_mesa(quantidade, id_produto)

	elif classe == 'Gabinete Tradicional':
		materiais_gabtrad(quantidade, id_produto)

	elif classe == 'Gabinete Luxo':
		materiais_gabluxo(quantidade, id_produto)

	elif classe == 'Caixa-Base':
		materiais_base(quantidade, id_produto)

	elif classe == 'Bancada Mdf':
		aba = retorna_aba
		if aba == 'Padrão':
			materiais_bancada(quantidade, id_produto)
		else:
			materiais_bancadapp(quantidade, id_produto)

	elif classe == 'Baú':
		pass

def materiais_mesa(quantidade, id_produto):
	quantidade = int(quantidade)
	tampo = quantidade * 2
	cabecote = quantidade * 2
	puxador = quantidade * 4
	p35x12 = quantidade * 6
	p40x25ox = quantidade * 8
	p40x30 = quantidade * 4

	atualiza('MTDTP', tampo)
	atualiza('MTDCB', cabecote)
	atualiza('PF3512', p35x12)
	atualiza('PF4025O', p40x25ox)
	atualiza('PF4030', p40x30)
	atualiza('CXMS', quantidade)

	cor = retorna_cor(id_produto)
	
	if cor == 'Avelã' or cor == 'Cedro':
		atualiza('PXPCR', puxador)
	
	elif cor == 'Café' or cor == 'Mogno':
		atualiza('PXPMR', puxador)
	
	elif cor == 'Marfim':
		atualiza('PXPMF', puxador)


def materiais_gabtrad(quantidade, id_produto):
	quantidade = int(quantidade)
	puxador = quantidade
	tampo = cabecote = dob_porta = fecho_rolete = p40x25ox = quantidade * 2
	sapata = p40x30 = quantidade * 4
	p25x10 = p30x12ox = p35x40 = quantidade * 6
	p25x16 = quantidade * 8
	p35x12 = quantidade * 12
	cavilha = quantidade * 14

	atualiza('PXGOV', puxador)
	atualiza('MTDTP', tampo)
	atualiza('MTDCB', cabecote)
	atualiza('MTDPT', dob_porta)
	atualiza('MTFRL', fecho_rolete)
	atualiza('PF4025O', p40x25ox)
	atualiza('PF4030', p40x30)
	atualiza('PF2510', p25x10)
	atualiza('PF3012O', p30x12ox)
	atualiza('PF3540', p35x40)
	atualiza('PF2516', p25x16)
	atualiza('PF3512', p35x12)
	atualiza('CAVI', cavilha)

	cor = retorna_cor(id_produto)
	
	if cor == 'Marfim':
		atualiza('PLS02', sapata)
	
	else:
		atualiza('PLS01', sapata)


def materiais_gabluxo(quantidade, id_produto):
	quantidade = int(quantidade)
	puxador = quantidade
	tampo = cabecote = dob_porta = fecho_rolete = p40x25ox = quantidade * 2
	sapata = quantidade * 6
	p40x30 = p35x40 = quantidade * 9
	p25x10 = p30x12ox = quantidade * 6
	p25x16 = quantidade * 8
	p35x12 = quantidade * 14
	cavilha = quantidade * 24

	atualiza('PXGOV', puxador)
	atualiza('MTDTP', tampo)
	atualiza('MTDCB', cabecote)
	atualiza('MTDPT', dob_porta)
	atualiza('MTFRL', fecho_rolete)
	atualiza('PF4025O', p40x25ox)
	atualiza('PF4030', p40x30)
	atualiza('PF2510', p25x10)
	atualiza('PF3012O', p30x12ox)
	atualiza('PF3540', p35x40)
	atualiza('PF2516', p25x16)
	atualiza('PF3512', p35x12)
	atualiza('CAVI', cavilha)

	cor = retorna_cor(id_produto)
	if cor == 'Marfim':
		atualiza('PLS02', sapata)
	else:
		atualiza('PLS01', sapata)


def materiais_base(quantidade, id_produto):
	quantidade = int(quantidade)
	pino_base = quantidade * 2
	pino_f20 = quantidade * 8
	embalagem = quantidade // 10

	atualiza('MTPBS', pino_base)
	atualiza('PN20', pino_f20)
	atualiza('CXBS', embalagem)


def materiais_bancada(quantidade, id_produto):
	quantidade = int(quantidade)
	cavilha = quantidade * 16
	p35x40 = quantidade * 8
	p40x30 = sapata = quantidade * 4
	p35x12 = quantidade * 18

	atualiza('CAVI', cavilha)
	atualiza('PF3540', p35x40)
	atualiza('P4030', p40x30)
	atualiza('P3512', p35x12)
	atualiza('CXBC', quantidade)
	atualiza('PLGPP', quantidade)
	atualiza('PLPP', quantidade)

	cor = retorna_cor(id_produto)
	if cor == 'Marfim':
		atualiza('PLS02', sapata)
	else:
		atualiza('PLS01', sapata)

def materiais_bancadapp(quantidade, id_produto):
	quantidade = int(quantidade)
	cavilha = quantidade * 16
	p35x40 = quantidade * 8
	p40x30 = sapata = cantoneira = quantidade * 4
	p35x12 = quantidade * 20

	atualiza('CAVI', cavilha)
	atualiza('PF3540', p35x40)
	atualiza('P4030', p40x30)
	atualiza('P3512', p35x12)
	atualiza('CXBC', quantidade)
	atualiza('PLGPP', quantidade)
	atualiza('MTC2F', cantoneira)

	cor = retorna_cor(id_produto)
	if cor == 'Marfim':
		atualiza('PLS02', sapata)
	else:
		atualiza('PLS01', sapata)


def materiais_bau(quantidade, id_produto):
	return


def atualiza(id_material, quantidade, operador='-'):
	novo_estoque = calcula_estoque(id_material, quantidade, operador)

	if novo_estoque >= 0:
		query = 'UPDATE materiais SET estoque = "' + str(novo_estoque) + '" WHERE (id_material = "' + str(id_material) + '")'
		c.execute(query)
		con.commit()
	else:
		print('operação cancelada: volume a ser expedido é maior do que existente no estoque.')
		return


def retorna_estoque(id_material):
	global c, con
	
	query = 'SELECT estoque FROM materiais WHERE (id_material = "' + str(id_material) + '")'
	c.execute(query)
	
	estoque = c.fetchone()
	estoque = estoque['estoque']
	
	return estoque


def calcula_estoque(id_material, quantidade, operador='-'):
	estoque = retorna_estoque(id_material)

	if operador == '-':
		novo_estoque = int(estoque) - int(quantidade)
		return novo_estoque
	elif operador == '+':
		novo_estoque = int(estoque) + int(quantidade)
		return novo_estoque


def retorna_cor(id_produto):
	global c, con
	
	query = 'SELECT cor FROM produtos WHERE (id_produto = "' + str(id_produto) + '")'
	c.execute(query)
	
	cor = c.fetchone()
	cor = cor['cor']
	
	return cor


def retorna_classe(id_produto):
	global c, con
	
	query = 'SELECT classe FROM produtos WHERE (id_produto = "' + str(id_produto) + '")'
	c.execute(query)
	
	classe = c.fetchone()
	classe = classe['classe']
	
	return classe


def retorna_aba(id_produto):
	global c, con
	
	query = 'SELECT aba FROM produtos WHERE (id_produto = "' + str(id_produto) + '")'
	c.execute(query)
	
	aba = c.fetchone()
	aba = aba['aba']
	
	return aba