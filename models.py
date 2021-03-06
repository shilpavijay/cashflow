from cashflow import db
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))
   
  def __init__(self, firstname, lastname, email, password):
    self.username = firstname.title()
    self.email = email.lower()
    self.set_password(password)
     
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)
   
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

class Expenses(db.Model):
  __tablename__ = 'expenses'
  uid = db.Column(db.Integer, primary_key = True)
  expname = db.Column(db.String(100))
  amount = db.Column(db.Float)

  def __init__(self,expname,amount):
    self.expname = expname.title()
    self.amount = amount

db.create_all()    