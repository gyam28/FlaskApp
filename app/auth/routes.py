from app.auth import auth
from flask import render_template, redirect, url_for, flash, request
from app.auth.forms import RegistrationForm, LoginForm, UpdateAccount
from app import bcrypt, db
from app.auth.models import User
from flask_login import login_user,current_user,logout_user,login_required
from app.auth.utils import save_picture

@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already logged in!","warning")
        return redirect(url_for("posts.home"))


    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(username=username, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash("Cool, you're done,{}".format(username), "success")
        print(username)
        return redirect(url_for('auth.login'))
    return render_template('register.html', reg_form = form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in!","warning")
        return redirect(url_for("posts.home"))

    login_form =LoginForm()
    if login_form.validate_on_submit():
        password = login_form.password.data
        email = login_form.email.data
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            flash("Welcome to your new home","success")
            login_user(user, remember=login_form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for('posts.home'))
        else:
            flash("Wrong credentials! Please try again.","danger")

    return render_template('login.html', form = login_form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("posts.home"))

@auth.route("/account",methods =["GET","POST"])
@login_required
def account():
    form = UpdateAccount()
    if request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    elif form.validate_on_submit():
        pic_data = form.picture.data
        if pic_data:
            profile_picture = save_picture(pic_data)
            current_user.image_file = profile_picture
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Account has been updated!","success")
        return redirect(url_for("auth.account"))
    return render_template("account.html",form = form)
