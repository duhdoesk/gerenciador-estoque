from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, LoginManager
from flask_table import Table, Col
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://aplicacao:123456@localhost/gerenciamento'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

login_manager = LoginManager(app)
db = SQLAlchemy(app)

@app.route('/')
def start():
	return redirect(url_for('home')) 

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	from usuarios import User

	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')

		user = User.query.filter_by(username=username).first()

		if not user or not user.verify_password(password):
			flash('Usuário ou senha inválidos.')
			return redirect(url_for('login'))

		login_user(user)
		return redirect(url_for('home'))

	return render_template('login.html')

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	from usuarios import User

	if request.method == 'POST':
		username = request.form.get('user')
		regkey = request.form.get('regkey')
		password = request.form.get('key')
		reppwd = request.form.get('repkey')

		if username and regkey and password and reppwd:
			if regkey == 'cmc2020':
				if password == reppwd:
					user = User(username, password)
					db.session.add(user)
					db.session.commit()

					flash('Cadastro realizado!')
					return redirect(url_for('home'))

				flash('- Você inseriu valores diferentes nos campos de senha.')
				return render_template('register.html')
			flash('- Chave de Registro inválida.')
			return render_template('register.html')
		flash('- Por favor, preencha todos os campos do formulário.')
		return render_template('register.html')

	return render_template('register.html')

@app.route('/produtos')
def lista_produtos():
	from lista_produtos import product_list
	produtos = product_list('produtos') # retorna uma lista json de objetos json
	time = last_update()
	return render_template('produtos.html', produtos=produtos, time=str(time))

@app.route('/materiais', methods=['GET', 'POST'])
def lista_materiais():
	from lista_materiais import material_list

	if request.method == 'POST':
		filter = request.form.get('filter')
		materiais = material_list('materiais', filter)
	else:
		materiais = material_list('materiais')

	time = last_update()
	return render_template('materiais.html', materiais=materiais, time=str(time))

@app.route('/expedicao', methods=['GET', 'POST'])
def expedicao():
	from lista_produtos import product_list
	produtos = product_list('produtos') # retorna uma lista json de objetos json

	return render_template('expedicao.html', produtos=produtos)

def last_update():
	registry = open(r"C:\Users\edusc\OneDrive\Área de Trabalho\gerenciador estoque\atualizacoes.txt", 'r')
	lines = registry.readlines()
	last_line = lines[-1][:20]
	return last_line

@login_manager.user_loader
def get_user(user_id):
	from usuarios import User
	return User.query.get(user_id)

if __name__ == "__main__":
	app.run(debug=True)