from app.posts import posts
from flask import render_template, redirect

@posts.route("/")
def home():
    return render_template("home.html")
