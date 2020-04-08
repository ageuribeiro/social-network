from app import app
from flask import Flask, render_template, url_for, flash, redirect
from app.models.forms import RegistrationForm, LoginForm


app.config['SECRET_KEY'] = '886855575cf9628ee70e100744cacb8b'

posts = [
    {
        'author':'Ageu Ribeiro',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 03, 2020'
    },
    {
        'author':'Corey Schafer',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'April 20, 2018'
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 3',
        'content':'Third post content',
        'date_posted':'April 21, 2020'
    }
]

@app.route("/")
def index():
    return render_template('index.html', title='Index')

@app.route("/test")
@app.route("/test/<name>")
def test(name=None):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, usuário!"

@app.route("/home")
def home(name):
    return render_template('home.html', posts=posts, title='Home')
    # return 'Olá, %s!' % name

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/comunidade")
def comunidade():
    return render_template('comunidade.html', title='Comunidade')

@app.route("/foruns")
def foruns():
    return render_template('foruns.html', title='Foruns')

@app.route("/friends")
def friends():
    return render_template('friends.html', title='Amigos')


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@dashspark.com' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
