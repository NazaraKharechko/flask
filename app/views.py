from flask import render_template, request

from app import app
from posts import posts
from some import User, dikts
from users import users

for user in users:
    user['posts'] = []
    for post in posts:
        if user['id'] == post['userId']:
            user['posts'].append(post)


@app.route('/')
def hello_dev():
    return render_template('hello.html')


@app.route('/age')
def ages():
    user = User
    d = dikts
    return render_template('age.html', user=user, d=d)


@app.route('/mail')
def mails():
    user1 = User
    us = users
    return render_template('mail.html', user=user1, us=us)


@app.route('/<ids>')
def id_user(ids):
    us = users
    return render_template('id_user.html', us=us, ids=int(ids))


@app.route('/city/<city>')
def users_by_city(city):
    return render_template('id_user.html', users=list(filter(lambda item: item['address']['city'] == city, users)))


@app.route('/search/', methods=['POST', 'GET'])
def search():
    result = ''
    if request.method == 'POST':
        result = request.form['search']
    return render_template('search.html', search=result)
