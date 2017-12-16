# coding=utf-8
import requests
from flask import Flask, render_template, request, make_response, session
from flask import redirect, send_from_directory, url_for
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'A0Zr98/3@#X R~asd#LWX/,?RT'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon')


@app.route('/lumpOpen/<id>/<stat>')
def lampOpen(id, stat):
    if 'user' in session:
        headers = {'AppCode': 'h28D3^1r*nhxc&213'}
        params = {'lumpNo': id, 'stat': stat}
        requests.get(
            'http://127.0.0.1:8881/lump', params=params, headers=headers)
        return '200'
    else:
        return '404'


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
    return render_template('index.htm', name=None)


@app.route('/')
def mainpage():
    if 'user' in session:
        return render_template('index.htm', name=session['user'])
    else:
        return render_template('index.htm', name=None)


@app.route('/', methods=['POST'])
def login():
    user = request.form['user']
    key = request.form['key']

    db = sqlite3.connect('./DB/mainDb.db')
    db.cursor().execute('''
    CREATE TABLE IF NOT EXISTS USER
    (ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    PASSWORD TEXT NOT NULL);
''')
    c = db.cursor()
    contact = ()
    try:
        contact = c.execute('''
            SELECT PASSWORD FROM USER WHERE NAME = '%s'
        ''' % (user))
    except:
        return render_template(
            'index.htm', name=None, alert_content="用户名或密码错误")

    for row in contact:
        if key != row[0]:
            db.close()
            return render_template(
                'index.htm', name=None, alert_content="用户名或密码错误")
        else:
            session['user'] = user
            session['stat'] = 'True'
            db.close()
            return render_template('index.htm', name=session['user'])
    db.close()
    return render_template('index.htm', name=None, alert_content="用户名或密码错误")


@app.route('/home')
def homepage():
    if 'user' in session:
        return render_template('home.htm', name=session['user'])
    else:
        return render_template('index.htm', name=None, alert_content="请先登录")


@app.route('/dog')
def dogpage():
    if 'user' in session:
        return render_template('dog.htm', name=session['user'])
    else:
        return render_template('index.htm', name=None, alert_content="请先登录")


@app.route('/car')
def carpage():
    if 'user' in session:
        return render_template('car.htm', name=session['user'])
    else:
        return render_template('index.htm', name=None, alert_content="请先登录")


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80)
