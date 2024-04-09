from flask import render_template, Blueprint, redirect, flash, url_for
from capp import db, bcrypt
from capp.users.forms import RegistrationForm, LoginForm
from capp.models import User
from flask_login import login_user, current_user, logout_user
from wtforms.validators import ValidationError

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
      user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data, password=user_hashed_password)
      db.session.add(user)
      db.session.commit()
      flash('Your account has been created! Now, you are able to login!', 'success')
      return redirect(url_for('carbon_app.carbon_app_home'))
  return render_template('users/register.html', title='register', form=form)

@users.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
      return redirect(url_for('carbon_app.carbon_app_home'))
  
  if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
          if bcrypt.check_password_hash(user.password, form.password.data):
              login_user(user, remember=form.remember.data)
              flash('You have logged in! Now, you can start to use carbon app!', 'success')
              return redirect(url_for('carbon_app.carbon_app_home'))
          else:
            flash('Invalid email or password. Please try again', 'danger')
      
        else:
           flash('User does not exist. Please try again', 'danger')
     

  return render_template('users/login.html', title='login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('carbon_app.carbon_app_home'))
