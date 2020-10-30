from tkinter import *
from tkinter import ttk
import gerenciador
import funcoes_produtos as fprod
import funcoes_materiais as fmat
import pymysql

host, user, pw, db, port = 'localhost', 'aplicacao', '123456', 'gerenciamento', 3306
con = pymysql.connect(host, user, pw, db, port)
c = con.cursor(pymysql.cursors.DictCursor)
y = 8

class Application:
	def __init__(self, master=None):

		fmat.calcula_mes()

		root.title('Gerenciador de Estoques ES 2020')
		root.geometry('1000x480+160+100')
		root['bg'] = ('black')

		menu = Frame(root, bg='gray20', width='300', height='500')
		menu.place(x=0, y=0)

		self.visual = Frame(root, bg='gray10', width='700', height='500')
		self.visual.place(x=300, y=0)

		exit_button = Button(menu, text="Sair", width='24', fg='black', bg='gray70', font=("Tahoma", 16))
		exit_button.place(x=1, y=435)

		exp_button = Button(menu, text='Expedição', width='24', fg='white', bg='gray20', font=('Tahoma', 16), command=self.butt1)
		exp_button.place(x=1, y=y)

		paEntry_button = Button(menu, text='Entrada de Produto Acabado', width='24', fg='white', bg='gray20', font=('Tahoma', 16),
			command=self.butt2)
		paEntry_button.place(x=1, y=y+40)

		matEntry_button = Button(menu, text='Entrada de Material', width='24', fg='white', bg='gray20', font=('Tahoma', 16),
			command=self.butt3)
		matEntry_button.place(x=1, y=y+80)

		paList_button = Button(menu, text='Lista de Produtos', width='24', fg='white', bg='gray20', font=('Tahoma', 16), command=self.butt4)
		paList_button.place(x=1, y=y+120)

		matList_button = Button(menu, text='Lista de Materiais', width='24', fg='white', bg='gray20', font=('Tahoma', 16), command=self.butt5)
		matList_button.place(x=1, y=y+160)

		titlelabel = Label(self.visual, bg='gray10', fg='white', text='BEM-VINDO!', font=('Tahoma', 42))
		titlelabel.place(x=100, y=80)

		titlelabel2 = Label(self.visual, bg='gray10', fg='white', text='Gerenciador de Estoques ES 2020 - Guará Móveis Especiais', font=('Tahoma', 12))
		titlelabel2.place(x=100, y=140)

		credits = Label(self.visual, bg='gray10', fg='gray40', text='Aplicação desenvolvida por Eduardo Scaranari Tessmer', font=('Tahoma', 10, 'italic'))
		credits.place(x=100, y=160)

		self.treestyle()

############################################################################################################################

	def butt1(self):
		self.visualclear()

		title_label = Label(self.visual, text='Ferramenta de Expedição', fg='white', bg='gray10', font=('Calibri', 20))
		title_label.place(x=210, y=8)

		data_label = Label(self.visual, text='Data', fg='white', bg='gray10', font=('Calibri', 12))
		data_label.place(x=8, y=430)

		id_label = Label(self.visual, text='Id do Produto', fg='white', bg='gray10', font=('Calibri', 12))
		id_label.place(x=8, y=60)

		est_label = Label(self.visual, text='Estoque', fg='gray60', bg='gray10', font=('Calibri', 12))
		est_label.place(x=181, y=60)

		quant_label = Label(self.visual, text='Quantidade', fg='white', bg='gray10', font=('Calibri', 12))
		quant_label.place(x=354, y=60)

		dest_label = Label(self.visual, text='Destino', fg='white', bg='gray10', font=('Calibri', 12))
		dest_label.place(x=527, y=60)

		data_entry = Entry(self.visual, width='16', font=('Calibri, 12'), justify='center')
		data_entry.place(x=8, y=455)

		id_entry = Entry(self.visual, width='20', font=('Calibri', 12), justify='center')
		id_entry.place(x=8, y=85)
		id_entry.bind('<Return>', lambda x: [self.textlabel(id_entry.get()), quant_entry.focus_set()])

		self.est = StringVar()
		self.est.set('')
		est_entry = Entry(self.visual, width='20', font=('Calibri', 12), justify='center', state='disabled', textvariable=self.est)
		est_entry.place(x=181, y=85)

		quant_entry = Entry(self.visual, width='20', font=('Calibri', 12), justify='center')
		quant_entry.place(x=354, y=85)
		quant_entry.bind('<Return>', lambda x: dest_entry.focus_set())

		dest_entry = Entry(self.visual, width='20', font=('Calibri', 12), justify='center')
		dest_entry.place(x=527, y=85)
		dest_entry.bind('<Return>', lambda x: append())

		self.text = StringVar()
		self.text.set('Texto onde será preenchida a descrição do produto')
		produto_label = Label(self.visual, textvariable=self.text, fg='gray60',
			bg='gray10', font=('Calibri', 12, 'italic'))
		produto_label.place(x=8, y=110)

		tree_label = Label(self.visual, text='Lista de Carga', fg='white', bg='gray10', font=('Calibri', 12))
		tree_label.place(x=8, y=175)

		self.tv = ttk.Treeview(self.visual, columns=(1, 2, 3, 4, 5), show='headings', height='10', style='Custom.Treeview')
		self.tv.place(x=8, y=200)

		self.tv.heading(1, text = ' id', anchor='w')
		self.tv.heading(2, text = ' produto', anchor='w')
		self.tv.heading(3, text = ' estoque', anchor='w')
		self.tv.heading(4, text = ' expedir', anchor='w')
		self.tv.heading(5, text = ' destino', anchor='w')
	
		self.tv.column(1, width = '70')
		self.tv.column(2, width = '350')
		self.tv.column(3, width = '70')
		self.tv.column(4, width = '70')
		self.tv.column(5, width = '120')

		add_button = Button(self.visual, text='Adicionar', width='20', fg='white', bg='blue', font=('Tahoma', 10),
			command=lambda: append())
		add_button.place(x=542, y=115)

		remove_button = Button(self.visual, text='Remover', width='20', fg='white', bg='red', font=('Tahoma', 10),
			command=lambda: delete())
		remove_button.place(x=542, y=145)

		confirm_button = Button(self.visual, text='Confirmar', width='20', fg='white', bg='green', font=('Tahoma', 10),
			command=lambda: confirm())
		confirm_button.place(x=542, y=435)

		def append():
			self.tv.insert('', 'end',
				values=(id_entry.get(), produto_label.cget('text'), est_entry.get(), quant_entry.get(), dest_entry.get()))

			id_entry.delete(0, 'end')
			self.est.set('')
			self.text.set('')
			quant_entry.delete(0, 'end')
			dest_entry.delete(0, 'end')
			id_entry.focus_set()

		def delete():
		    selected_item = self.tv.selection()[0]
		    self.tv.delete(selected_item)

		def confirm():
			lista_id = []
			lista_quantidade = []
			lista_destino = []
			lista_descricao = []
			data = data_entry.get()

			for item in self.tv.get_children():
				lista_id.append(self.tv.item(item)['values'][0])
				lista_descricao.append(self.tv.item(item)['values'][1])
				lista_quantidade.append(self.tv.item(item)['values'][3])
				lista_destino.append(self.tv.item(item)['values'][4])

			gerenciador.saida_produtos_inter(lista_id, lista_quantidade, lista_destino, lista_descricao, data)

############################################################################################################################

	def butt2(self):
		self.visualclear()

		title_label = Label(self.visual, text='Gestão de Produto Acabado', fg='white', bg='gray10', font=('Calibri', 20))
		title_label.place(x=210, y=8)

		id_label = Label(self.visual, text='Id do Produto', fg='white', bg='gray10', font=('Calibri', 12))
		id_label.place(x=8, y=60)

		est_label = Label(self.visual, text='Estoque', fg='gray60', bg='gray10', font=('Calibri', 12))
		est_label.place(x=181, y=60)

		quant_label = Label(self.visual, text='Quantidade', fg='white', bg='gray10', font=('Calibri', 12))
		quant_label.place(x=354, y=60)

		id_entry = Entry(self.visual, width='20', font=('Calibri', 12), justify='center')
		id_entry.place(x=8, y=85)
		id_entry.bind('<Return>', lambda x: [self.textlabel(id_entry.get()), quant_entry.focus_set()])

		self.est = StringVar()
		self.est.set('')
		est_entry = Entry(self.visual, width='20', font=('Calibri', 12), justify='center', state='disabled', textvariable=self.est)
		est_entry.place(x=181, y=85)

		quant_entry = Entry(self.visual, width='20', font=('Calibri', 12), justify='center')
		quant_entry.place(x=354, y=85)
		quant_entry.bind('<Return>', lambda x: append())

		data_label = Label(self.visual, text='Data', fg='white', bg='gray10', font=('Calibri', 12))
		data_label.place(x=8, y=430)

		data_entry = Entry(self.visual, width='16', font=('Calibri, 12'), justify='center')
		data_entry.place(x=8, y=455)

		self.text = StringVar()
		self.text.set('Texto onde será preenchida a descrição do produto')
		produto_label = Label(self.visual, textvariable=self.text, fg='gray60',
			bg='gray10', font=('Calibri', 12, 'italic'))
		produto_label.place(x=8, y=110)

		tree_label = Label(self.visual, text='Lista de Carga', fg='white', bg='gray10', font=('Calibri', 12))
		tree_label.place(x=8, y=175)

		self.tv = ttk.Treeview(self.visual, columns=(1, 2, 3, 4, 5), show='headings', height='10', style='Custom.Treeview')
		self.tv.place(x=8, y=200)

		self.tv.heading(1, text = ' id', anchor='w')
		self.tv.heading(2, text = ' produto', anchor='w')
		self.tv.heading(3, text = ' estoque', anchor='w')
		self.tv.heading(4, text = ' quantidade', anchor='w')
		self.tv.heading(5, text = '', anchor='w')
	
		self.tv.column(1, width = '70')
		self.tv.column(2, width = '350')
		self.tv.column(3, width = '70')
		self.tv.column(4, width = '70')
		self.tv.column(5, width = '120')

		add_button = Button(self.visual, text='Adicionar', width='20', fg='white', bg='blue', font=('Tahoma', 10),
			command=lambda: append())
		add_button.place(x=542, y=115)

		remove_button = Button(self.visual, text='Remover', width='20', fg='white', bg='red', font=('Tahoma', 10),
			command=lambda: delete())
		remove_button.place(x=542, y=145)

		confirm_button = Button(self.visual, text='Confirmar', width='20', fg='white', bg='green', font=('Tahoma', 10),
			command=lambda: confirm())
		confirm_button.place(x=542, y=435)

		def append():
			self.tv.insert('', 'end',
				values=(id_entry.get(), produto_label.cget('text'), est_entry.get(), quant_entry.get()))

			id_entry.delete(0, 'end')
			self.est.set('')
			self.text.set('')
			quant_entry.delete(0, 'end')
			id_entry.focus_set()

		def delete():
		    selected_item = self.tv.selection()[0]
		    self.tv.delete(selected_item)

		def confirm():
			lista_id = []
			lista_quantidade = []

			for item in self.tv.get_children():
				lista_id.append(self.tv.item(item)['values'][0])
				lista_quantidade.append(self.tv.item(item)['values'][3])

			gerenciador.entrada_produtos(lista_id, lista_quantidade)

############################################################################################################################

	def butt3(self):
		self.visualclear()

		title_label = Label(self.visual, text='Gestão de Materiais', fg='white', bg='gray10', font=('Calibri', 20))
		title_label.place(x=210, y=8)

		id_label = Label(self.visual, text='Id do Material', fg='white', bg='gray10', font=('Calibri', 12))
		id_label.place(x=8, y=60)

		est_label = Label(self.visual, text='Estoque', fg='gray60', bg='gray10', font=('Calibri', 12))
		est_label.place(x=181, y=60)

		quant_label = Label(self.visual, text='Quantidade', fg='white', bg='gray10', font=('Calibri', 12))
		quant_label.place(x=354, y=60)

		id_entry = Entry(self.visual, width='20', font=('Calibri', 12), justify='center')
		id_entry.place(x=8, y=85)
		id_entry.bind('<Return>', lambda x: [self.textlabel(id_entry.get(), 'x'), quant_entry.focus_set()])

		self.est = StringVar()
		self.est.set('')
		est_entry = Entry(self.visual, width='20', font=('Calibri', 12), justify='center', state='disabled', textvariable=self.est)
		est_entry.place(x=181, y=85)

		quant_entry = Entry(self.visual, width='20', font=('Calibri', 12), justify='center')
		quant_entry.place(x=354, y=85)
		quant_entry.bind('<Return>', lambda x: append())

		data_label = Label(self.visual, text='Data', fg='white', bg='gray10', font=('Calibri', 12))
		data_label.place(x=8, y=430)

		data_entry = Entry(self.visual, width='16', font=('Calibri, 12'), justify='center')
		data_entry.place(x=8, y=455)

		self.text = StringVar()
		self.text.set('Texto onde será preenchida a descrição do material')
		produto_label = Label(self.visual, textvariable=self.text, fg='gray60',
			bg='gray10', font=('Calibri', 12, 'italic'))
		produto_label.place(x=8, y=110)

		tree_label = Label(self.visual, text='Lista de Carga', fg='white', bg='gray10', font=('Calibri', 12))
		tree_label.place(x=8, y=175)

		self.tv = ttk.Treeview(self.visual, columns=(1, 2, 3, 4, 5), show='headings', height='10', style='Custom.Treeview')
		self.tv.place(x=8, y=200)

		self.tv.heading(1, text = ' id', anchor='w')
		self.tv.heading(2, text = ' material', anchor='w')
		self.tv.heading(3, text = ' estoque', anchor='w')
		self.tv.heading(4, text = ' quantidade', anchor='w')
		self.tv.heading(5, text = ' ', anchor='w')
	
		self.tv.column(1, width = '70')
		self.tv.column(2, width = '350')
		self.tv.column(3, width = '70')
		self.tv.column(4, width = '70')
		self.tv.column(5, width = '120')

		add_button = Button(self.visual, text='Adicionar', width='20', fg='white', bg='blue', font=('Tahoma', 10),
			command=lambda: append())
		add_button.place(x=542, y=115)

		remove_button = Button(self.visual, text='Remover', width='20', fg='white', bg='red', font=('Tahoma', 10),
			command=lambda: delete())
		remove_button.place(x=542, y=145)

		confirm_button = Button(self.visual, text='Confirmar', width='20', fg='white', bg='green', font=('Tahoma', 10),
			command=lambda: confirm())
		confirm_button.place(x=542, y=435)

		def append():
			self.tv.insert('', 'end',
				values=(id_entry.get(), produto_label.cget('text'), est_entry.get(), quant_entry.get()))

			id_entry.delete(0, 'end')
			self.est.set('')
			self.text.set('')
			quant_entry.delete(0, 'end')
			id_entry.focus_set()

		def delete():
		    selected_item = self.tv.selection()[0]
		    self.tv.delete(selected_item)

		def confirm():
			lista_id = []
			lista_quantidade = []

			for item in self.tv.get_children():
				lista_id.append(self.tv.item(item)['values'][0])
				lista_quantidade.append(self.tv.item(item)['values'][3])

			gerenciador.entrada_materiais(lista_id, lista_quantidade)

############################################################################################################################

	def butt4(self):
		try:
			self.estoque.destroy()
			self.completa.destroy()
		except:
			pass

		self.estoque = Button(self.visual, width='24', command = lambda: self.visualtree('produtos', '1'),
			text='Produtos com estoque', font=('Calibri', 12, 'italic'), bg='gray10', fg='lightgoldenrod')
		self.estoque.place(x=1, y=y+120)

		self.completa = Button(self.visual, width='24', command = lambda: self.visualtree('produtos', '2'),
			text='Lista Completa', font=('Calibri', 12, 'italic'), bg='gray10', fg='lightgoldenrod')
		self.completa.place(x=1, y=y+150)

############################################################################################################################

	def butt5(self):
		try:
			self.estoque.destroy()
			self.completa.destroy()
		except:
			pass

		self.estoque = Button(self.visual, width='24', command = lambda: self.visualtree('materiais', '1'),
			text='Materiais com estoque', font=('Calibri', 12, 'italic'), bg='gray10', fg='lightgoldenrod')
		self.estoque.place(x=1, y=y+160)

		self.completa = Button(self.visual, width='24', command = lambda: self.visualtree('materiais', '2'),
			text='Lista Completa', font=('Calibri', 12, 'italic'), bg='gray10', fg='lightgoldenrod')
		self.completa.place(x=1, y=y+190)

############################################################################################################################

	def visualtree(self, tabela, opcao):
		self.visualclear()

		if opcao == '1':
			query = 'SELECT * FROM ' + tabela + ' WHERE estoque > 0'
		else:
			query = 'SELECT * FROM ' + tabela

		c.execute(query)
		rows = c.fetchall()

		if tabela == 'materiais':
			columns = (' id', ' material', ' estoque', ' estoque minimo', ' coeficiente')
			self.tv = ttk.Treeview(self.visual, columns=columns, show='headings', height='20', style='Custom.Treeview')
			self.tv.place(x=8, y=8)

			self.tv.heading(' id', text = ' id', anchor='w')
			self.tv.heading(' material', text = ' material', anchor='w')
			self.tv.heading(' estoque', text = ' estoque', anchor='w')
			self.tv.heading(' estoque minimo', text = ' estoque mínimo', anchor='w')
			self.tv.heading(' coeficiente', text = ' coeficiente', anchor='w')
		
			self.tv.column(' id', width = '100')
			self.tv.column(' material', width = '300')
			self.tv.column(' estoque', width = '100')
			self.tv.column(' estoque minimo', width = '100')
			self.tv.column(' coeficiente', width = '80')

			for i in rows:
				self.tv.insert('', 'end', values = (i['id_material'], i['nome'], i['estoque'], i['estoque_minimo'], i['estoque_mes']))

			att_button = Button(self.visual, text='Atualizar Coeficiente', width='20', fg='white', bg='blue', font=('Tahoma', 10),
				command=lambda: fmat.calcula_mes())
			att_button.place(x=542, y=435)

		else:
			columns=(' id', ' classe', ' condição', ' aba', ' cor', ' estoque')
			self.tv = ttk.Treeview(self.visual, columns = columns, show = 'headings', height = '22', style='Custom.Treeview')
			self.tv.place(x=8, y=8)

			self.tv.heading(' id', text = ' id', anchor='w')
			self.tv.heading(' classe', text = ' classe', anchor='w')
			self.tv.heading(' condição', text = ' condição', anchor='w')
			self.tv.heading(' aba', text = ' aba', anchor='w')
			self.tv.heading(' cor', text = ' cor', anchor='w')
			self.tv.heading(' estoque', text = ' estoque', anchor='w')

			self.tv.column(' id', width = '90')
			self.tv.column(' classe', width = '160')
			self.tv.column(' condição', width = '160')
			self.tv.column(' aba', width = '90')
			self.tv.column(' cor', width = '90')
			self.tv.column(' estoque', width = '90')

			for i in rows:
				self.tv.insert('', 'end', values = (i['id_produto'], i['classe'], i['condicao'], i['aba'], i['cor'], i['estoque']))

		def treeview_sort_column(tv, col, reverse):
			l = [(self.tv.set(k, col), k) for k in self.tv.get_children('')]
			l.sort(reverse=reverse)
			for index, (val, k) in enumerate(l):
				self.tv.move(k, '', index)
			self.tv.heading(col, command=lambda _col=col: treeview_sort_column(tv, _col, not reverse))

		for col in columns:
			self.tv.heading(col, text=col,command=lambda _col=col: treeview_sort_column(self.tv, _col, False))

	def visualclear(self):
		for children in self.visual.winfo_children():
			children.destroy()

	def treestyle(self):
		try:
			style = ttk.Style()
			style.element_create("Custom.Treeheading.border", "from", "default")
			style.layout("Custom.Treeview.Heading", [
				("Custom.Treeheading.cell", {'sticky': 'nswe'}),
				("Custom.Treeheading.border", {'sticky':'nswe', 'children': [
				("Custom.Treeheading.padding", {'sticky':'nswe', 'children': [
				("Custom.Treeheading.image", {'side':'right', 'sticky':''}),
					("Custom.Treeheading.text", {'sticky':'we'})
						]})
					]}),
				])
			style.configure("Custom.Treeview.Heading",
				background="gray80", foreground="black", relief="flat")
			style.map("Custom.Treeview.Heading",
				relief=[('active','groove'),('pressed','sunken')])
		except:
			pass

	def textlabel(self, id_produto, tabela=''):
		if not (tabela):
			try:
				classe = str(fmat.retorna_classe(id_produto))
				condicao = str(fmat.retorna_condicao(id_produto))
				cor = str(fmat.retorna_cor(id_produto))
				aba = str(fmat.retorna_aba(id_produto))
				estoque = str(fprod.retorna_estoque(id_produto))
				string = (classe + ' ' + condicao + ' ' +  cor + ' ' + aba)
				string = string.replace('None', '')
				self.text.set(string)
				self.est.set(estoque)
			except:
				self.text.set('Id inválido')
		else:
			try: 
				material = str(fmat.retorna_material(id_produto))
				estoque = str(fmat.retorna_estoque(id_produto))
				self.text.set(material)
				self.est.set(estoque)
			except:
				self.text.set('Id inválido')


root = Tk()
Application(root)
root.mainloop()