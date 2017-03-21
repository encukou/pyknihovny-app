from flask import Flask, url_for, render_template
from jinja2 import Markup

app = Flask(__name__)

@app.route('/')
def hello():
    return url_for('hello_english',
                   username='Petr',
                   count=3)

@app.route('/hello/')
@app.route('/hello/<username>/')
@app.route('/hello/<username>/<int:count>/')
def hello_english(username=None, count=1):
    return render_template('hello.html',
                           name=username)

@app.template_filter('em')
def em(text):
    return Markup('<em>{}</em>').format(text)
