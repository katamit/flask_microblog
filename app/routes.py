from app import application
from flask import render_template, flash, redirect, url_for
from app import forms

@application.route('/')
@application.route('/index')
def index():
	user = {'username': 'Migul'}
	posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
	return render_template('index.html',user=user, posts=posts)#,title='Home',user=user)

# @application.route('/login')
@application.route('/login', methods=['GET', 'POST'])
def login():
	form = forms.LoginForm()
	print('before validate_on_submit---')
	if form.validate_on_submit():
		print("insidre the validate_on_submit-----")
		flash('Login requested fro user  {}, remember_me {}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', form=form)
