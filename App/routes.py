from flask import render_template, flash, redirect, url_for
from App import app
from App.forms import LoginForm


@app.route('/index')
@app.route('/')
def index():
    user = {'username': 'Mikey'}
    posts = [
        {
            'author': {'username': 'SexyMike'},
            'body': 'Beautiful day in MikeyTown!'
        },
        {
            'author': {'username': 'CuddlyMike'},
            'body': 'I still want to watch the Avengers!! 😭'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data,
                                                                   form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
