from flask import  render_template,request,url_for,flash,redirect,session
from app import app
from models import db,User,Category,Product,Cart,Transaction,Order
from werkzeug.security import generate_password_hash,check_password_hash
# Define the route for the index page
@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('index.html')
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        flash('Please fill out all fields')
        return redirect(url_for('login'))
    
    
    user= User.query.filter_by(username=username).first()

    if not user:
        flash('Username does not exist')
        return redirect(url_for('login'))
    
    if not check_password_hash(user.passhash,password):
        flash('Incorrect password')
        return redirect(url_for('login'))
    
    session['user_id']= user.id
    flash('Login Successful')
    return redirect(url_for('index'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    name= request.form.get('name')

    if not username or not password or not confirm_password:
        flash('Please fill out all fields')
        return redirect(url_for('register'))
    
    if password!=confirm_password:
        flash('Passwords do not match')
        return redirect(url_for('register'))
    
    user= User.query.filter_by(username=username).first()

    if user:
        flash('Username already exist')
        return redirect(url_for('register'))
    
    password_hash=generate_password_hash(password)
    new_user=User(username=username,passhash=password_hash,name=name)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))


    
   



