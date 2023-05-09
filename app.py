from functools import wraps
import pymongo
from bson.objectid import ObjectId
from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = b'\xb1]=\xd9\x89\x15\x92(T\x8b\xda\xc92\xbf\xff5'

# Database
client = pymongo.MongoClient('localhost', 27017)
# client = MongoClient('localhost', 27017, username='maddie', password='mongo2023')
db_user = client.user_login_system
db = client.flask_db
todos = db.todos


# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


@app.route('/', methods=('GET', 'POST'))
def index():
    print("index")
    if request.method == 'POST':
        print("in post")
        content = request.form['content']
        degree = request.form['degree']
        due_date = request.form['due-date']
        user_id = session['user_id']  # get the current user's ID
        todos.insert_one({'content': content, 'degree': degree, 'due_date': due_date, 'user_id': user_id})
        return redirect(url_for('index'))

    if 'logged_in' in session:
        user_id = session['user_id']  # get the current user's ID
        all_todos = todos.find({'user_id': user_id})  # only fetch todos for the current user
        for todo in all_todos:
            if 'due_date' not in todo:
                todo['due_date'] = None
        return render_template('index.html', todos=all_todos)
    else:
        return redirect('/')


@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


# Route
from user.routes import *


@app.route('/home')
def home():
    return render_template('home.html')


# @app.route('/dashboard/')
# @login_required
# def dashboard():
#     return render_template('dashboard.html')


@app.route('/signup')
def signup():
    return redirect(url_for('index.html'))


@app.route('/signin', methods=['POST'])
def signin():
    return redirect(url_for('index.html'))
