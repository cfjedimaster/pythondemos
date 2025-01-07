from flask import Flask
from markupsafe import escape
from flask import url_for, redirect, session
from flask import request
from flask import render_template

app = Flask(__name__)

app.secret_key = 'This would not be checked in as a hard coded string'

@app.route("/")
def hello_world():
    print(f"Request method, {request.method}")
    print(url_for('static',filename='style.css'))
    return "<p>Hello, World.</p>"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    print('running from func, was passed', post_id, 'url for test', url_for('hello', name='bob'))
    return f'Post {post_id}'

@app.route("/goodbye/")
@app.route("/goodbye/<name>")
def goodbye(name=None):
    return render_template('goodbye.html', person=name)

@app.route("/testlayout/")
def testlayout():
	return render_template('test_layout.html')

@app.route('/redirect')
def redirecttest():
     return redirect(url_for('hello', name='Redirect'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.get('/cats')
def getcats():
     return [{ "name":"Luna", "age":12 }, { "name":"Elise", "age":13 }]

@app.get('/counter')
def counter():
	app.logger.debug('Session testing')
	if 'hits' in session:
		session['hits'] = session['hits'] + 1
	else:
		session['hits'] = 1
            
	return f"You've been here {session['hits']} times."