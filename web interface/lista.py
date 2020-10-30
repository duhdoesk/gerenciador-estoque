lista = [
	{'id': 'BS04', 'product': 'Caixa-Base', 'condition': '', 'aba': '', 'color': 'Marfim', 'stock': 480}, 
	{'id': 'GLD02A', 'product': 'Gabinete Luxo', 'condition': 'Desmontado', 'aba': 'PP', 'color': 'Café', 'stock': 5}, 
	{'id': 'GLD04A', 'product': 'Gabinete Luxo', 'condition': 'Desmontado', 'aba': 'PP', 'color': 'Marfim', 'stock': 5}, 
	{'id': 'GTD02', 'product': 'Gabinete Tradicional', 'condition': 'Desmontado', 'aba': 'Padrão', 'color': 'Café', 'stock': 40}, 
	{'id': 'GTD02A', 'product': 'Gabinete Tradicional', 'condition': 'Desmontado', 'aba': 'PP', 'color': 'Café', 'stock': 7}, 
	{'id': 'GTD02F', 'product': 'Gabinete Tradicional', 'condition': 'Desmontado', 'aba': 'Fechada', 'color': 'Café', 'stock': 10}, 
	{'id': 'GTD04A', 'product': 'Gabinete Tradicional', 'condition': 'Desmontado', 'aba': 'PP', 'color': 'Marfim', 'stock': 33}, 
	{'id': 'GTD04F', 'product': 'Gabinete Tradicional', 'condition': 'Desmontado', 'aba': 'Fechada', 'color': 'Marfim', 'stock': 21}, 
	{'id': 'GTM01A', 'product': 'Gabinete Tradicional', 'condition': 'Montado', 'aba': 'PP', 'color': 'Avelã', 'stock': 10}, 
	{'id': 'GTM01F', 'product': 'Gabinete Tradicional', 'condition': 'Montado', 'aba': 'Fechada', 'color': 'Avelã', 'stock': 10}
]

id_item = 'BS04'

for item in lista:
	if item['id'] == id_item:
		cor = item['color']
		produto = item['product']

print(produto + ' ' + cor)