  
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5afd723422802a8cedff0e0ff00d8976'

posts = [
    {
        'author': 'Adam Pekalski',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 14, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 15, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/login")
def login():
    form = LoginForm
    return render_template('login.html', title='login', form=form)

@app.route("/register")
def register():
    form = RegistrationForm
    return render_template('register.html', title='register', form=form)

if __name__ == '__main__':
    app.run(debug=True)