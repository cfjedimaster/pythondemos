from flask import Flask
from flask import render_template

from blog import Blog 

app = Flask(__name__)
blog = Blog()

@app.route("/")
def homepage():
	posts = blog.getPosts()
	return render_template('index.html', posts=posts)

@app.route("/post/<string:slug>")
def post(slug):
	print(f"get post by slug, {slug}")
	post = blog.getPost(slug)
	return render_template('post.html', post=post)
