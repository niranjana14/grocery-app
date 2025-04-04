from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)
print('Running models.py')



class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(32),unique=True)
    passhash=db.Column(db.String(256),nullable=False)
    name=db.Column(db.String(64),nullable=True)
    is_admin=db.Column(db.Boolean,nullable=False,default=False)

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32),unique=True)
    products=db.relationship('Product',backref='Category',lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),nullable=False)
    price=db.Column(db.Float,nullable=False)
    description = db.Column(db.String(256),nullable=True)
    category_id=db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    man_date=db.Column(db.Date,nullable=False)

    carts=db.relationship('Cart',backref='Product',lazy=True)
    orders=db.relationship('Order',backref='Product',lazy=True)


class Cart(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    product_id=db.Column(db.Integer,db.ForeignKey('product.id'),nullable=False)
    quantity=db.Column(db.Integer,nullable=False)

class Transaction(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    datetime=db.Column(db.Date,nullable=False)

    orders=db.relationship('Order',backref='Transaction',lazy=True)

class Order(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    product_id=db.Column(db.Integer,db.ForeignKey('product.id'),nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    price=db.Column(db.Float,nullable=False)


with app.app_context():
    print('creating db')
    db.create_all()




