from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alex'}
    posts = [
        {'author': {'username': 'Fedor'},
         'body': 'The weather is not great and not terrible'},
        {'author': {'username': 'John'},
         'body': 'What are you think about po...ny?'}
    ]
    return render_template(
        'index.html',
        title='Home',
        user=user,
        posts=posts
    )
