from flask import Flask, render_template, url_for, flash
from flask_wtf import FlaskForm
from data import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'sdmak12n292edf9nrn1f1d9end1'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)

@app.route('/')
def home():
    return "hello"



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)
                           
                          

if (__name__) == '__main__':
    app.run(debug=True)
