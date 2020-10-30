import pymysql
import funcoes_produtos as fprod 

host, user, pw, db, port = 'localhost', 'aplicacao', '123456', 'gerenciamento', 3306
con = pymysql.connect(host, user, pw, db, port)
c = con.cursor(pymysql.cursors.DictCursor)


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
		materiais_bau(quantidade, id_produto)

def materiais_mesa(quantidade, id_produto):
	quantidade = int(quantidade)
	tampo = cabecote = quantidade * 2
	puxador = cantoneira = p40x30 = quantidade * 4
	p35x12 = quantidade * 6
	p40x25ox = quantidade * 8

	atualiza('MTDTP', tampo)
	atualiza('MTDCB', cabecote)
	atualiza('MTD14', cabecote)
	atualiza('PF3512', p35x12)
	atualiza('PF4025O', p40x25ox)
	atualiza('PF4030', p40x30)
	atualiza('PLCMS', cantoneira)

	cond = retorna_condicao(id_produto)
	if cond != 'Elgin':
		atualiza('CXMS', quantidade)
	else:
		atualiza('CXEL', quantidade)

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
	tampo = cabecote = dob_porta = fecho_rolete = p40x25ox = p40x22 = quantidade * 2
	sapata = p40x30 = quantidade * 4
	p25x10 = p30x12ox = p35x40 = corredica = quantidade * 6
	p25x16 = cantoneira = quantidade * 8
	p35x12 = quantidade * 12
	cavilha = quantidade * 14

	atualiza('PXGOV', puxador)
	atualiza('MTDTP', tampo)
	atualiza('MTDCB', cabecote)
	atualiza('MTDPT', dob_porta)
	atualiza('MTD14', dob_porta)
	atualiza('MTFRL', fecho_rolete)
	atualiza('PF4025O', p40x25ox)
	atualiza('PF4030', p40x30)
	atualiza('PF2510', p25x10)
	atualiza('PF3012O', p30x12ox)
	atualiza('PF3540', p35x40)
	atualiza('PF2516', p25x16)
	atualiza('PF3512', p35x12)
	atualiza('CAVI', cavilha)
	atualiza('PF4022', p40x22)
	atualiza('PLCGB', cantoneira)

	cor = retorna_cor(id_produto)
	if cor == 'Marfim':
		atualiza('PLS02', sapata)
	
	else:
		atualiza('PLS01', sapata)

	cond = retorna_condicao(id_produto)
	if cond == 'Montado':
		atualiza('CXGTM', quantidade)
	else:
		atualiza('CXGTD', quantidade)

	aba = retorna_aba(id_produto)
	if aba == 'PP':
		atualiza('PLCRP', corredica)
		pf = corredica * 4
		atualiza('PF3512', pf) 


def materiais_gabluxo(quantidade, id_produto):
	quantidade = int(quantidade)
	puxador = quantidade
	tampo = cabecote = dob_porta = fecho_rolete = p40x25ox = p40x22 = quantidade * 2
	p40x30 = p35x40 = quantidade * 9
	p25x10 = p30x12ox = corredica = sapata = quantidade * 6
	p25x16 = cantoneira = quantidade * 8
	p35x12 = quantidade * 14
	cavilha = quantidade * 24

	atualiza('PXGOV', puxador)
	atualiza('MTDTP', tampo)
	atualiza('MTDCB', cabecote)
	atualiza('MTDPT', dob_porta)
	atualiza('MTD14', dob_porta)
	atualiza('MTFRL', fecho_rolete)
	atualiza('PF4025O', p40x25ox)
	atualiza('PF4030', p40x30)
	atualiza('PF2510', p25x10)
	atualiza('PF3012O', p30x12ox)
	atualiza('PF3540', p35x40)
	atualiza('PF2516', p25x16)
	atualiza('PF3512', p35x12)
	atualiza('CAVI', cavilha)
	atualiza('PF4022', p40x22)
	atualiza('PLCGB', cantoneira)

	cor = retorna_cor(id_produto)
	if cor == 'Marfim':
		atualiza('PLS02', sapata)
	else:
		atualiza('PLS01', sapata)

	cond = retorna_condicao(id_produto)
	if cond == 'Montado':
		atualiza('CXGLM', quantidade)
	else:
		atualiza('CXGLD', quantidade)

	aba = retorna_aba(id_produto)
	if aba == 'PP':
		atualiza('PLCRP', corredica)
		pf = corredica * 4
		atualiza('PF3512', pf)


def materiais_base(quantidade, id_produto):
	quantidade = int(quantidade)
	pino_base = quantidade * 2
	embalagem = quantidade // 10

	atualiza('MTPBS', pino_base)
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
	quantidade = int(quantidade)
	p40x25 = trinco = cabecote = quantidade * 2
	p35x12 = sapata = quantidade * 4

	atualiza('PF3512', p35x12)
	atualiza('PF4025', p40x25)
	atualiza('PLALB', quantidade)
	atualiza('MTTBA', trinco)
	atualiza('MTDCBA', cabecote)
	atualiza('PLS03', sapata)
	atualiza('CXBA', quantidade)


def atualiza(id_material, quantidade, operador='-'):
	estoque = retorna_estoque(id_material)
	novo_estoque = calcula_estoque(id_material, quantidade, operador)
	material = str(retorna_material(id_material) + ' (' + id_material + ')')

	if novo_estoque >= 0:
		query = 'UPDATE materiais SET estoque = "' + str(novo_estoque) + '" WHERE (id_material = "' + str(id_material) + '")'
		c.execute(query)
		con.commit()
		
		if operador == '-':
			texto = '	- ' + str(quantidade) + ' unidade(s) do material ' + material + ' consumida(s) (' + str(estoque) + ' > ' + str(novo_estoque) + ').\n'
			registro(texto)

	else:
		if operador == '-':
			texto = '	##### operação cancelada: só existe(m) ' + str(estoque) + ' unidade(s) do material ' + material + ' (' + str(quantidade) + ') em estoque.\n'
			registro(texto)
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

def retorna_condicao(id_produto):
	global c, con
	
	query = 'SELECT condicao FROM produtos WHERE (id_produto = "' + str(id_produto) + '")'
	c.execute(query)
	
	condicao = c.fetchone()
	condicao = condicao['condicao']
	
	return condicao

def retorna_material(id_material):
	global c, con

	query = 'SELECT nome FROM materiais WHERE (id_material = "' + str(id_material) + '")'
	c.execute(query)

	material = c.fetchone()
	material = material['nome']

	return material

def retorna_estmin(id_material):
	global c, con
	
	query = 'SELECT estoque_minimo FROM materiais WHERE (id_material = "' + str(id_material) + '")'
	c.execute(query)
	
	estoque_minimo = c.fetchone()
	estoque_minimo = estoque_minimo['estoque_minimo']
	
	return estoque_minimo

def retorna_mes(id_material):
	estoque = retorna_estoque(id_material)
	estmin = retorna_estmin(id_material)

	try:
		coeficiente = estoque / estmin
		coeficiente = float("{:.2f}".format(coeficiente))
	except:
		coeficiente = 0

	if estmin == 0 or estmin is None:
		coeficiente = 999

	query = 'UPDATE materiais SET estoque_mes = "' + str(coeficiente) + '" WHERE (id_material = "' + str(id_material) + '")'
	c.execute(query)
	con.commit()

def calcula_mes():
	global c, con

	query = 'SELECT id_material FROM materiais'
	c.execute(query)

	lista_id = c.fetchall()
	aas = []
	
	i = 0
	while i < len(lista_id):
		for key, value in lista_id[i].items():
			aas.append(value)
		i += 1

	for id in aas:
		retorna_mes(id)

def registro(texto):
		registro = open('C:/Users/edusc/OneDrive/Área de Trabalho/gerenciador estoque/registro.txt', 'a')
		registro.write(texto)
		registro.close()