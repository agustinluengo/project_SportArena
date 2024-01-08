# pip install Flask 
# pip install flask-wtf
# pip install flask-sqlalchemy

### initiating flask ### 
# export FLASK_APP=config.py (linux/mac)
# export FLASK_DEBUG=1 (linux/mac)
# flask run

from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gz3nsrkonCAP882Z'
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)        
    username = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), unique=True, nullable=False, default='default.jpg')
    password = db.Column(db.String(20), unique=True, nullable=False)
    

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

# Profile Information Page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('profile.html', title='Login', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
        form = LoginForm()
        if form.validate_on_submit():
        return render_template('login.html', title='Login', form=form)

@app.route("/profile")
def reservation():
    return render_template('profile.html')

@app.route("/sports")
def reservation():
    return render_template('sports.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

