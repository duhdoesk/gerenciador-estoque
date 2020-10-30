from run import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
	return User.get(user_id)

class User(db.Model, UserMixin):
	__tablename__ = 'accounts'

	id = db.Column(db.Integer, autoincrement = True, primary_key = True)
	username = db.Column(db.String(50), nullable = False, unique = True)
	password = db.Column(db.String(255), nullable = False)

	def __init__(self, username, password):
		self.username = username
		self.password = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password, password)
