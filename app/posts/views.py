from flask import Blueprint, render_template, request

from app import db
from app.forms import Pet, Posts_Form

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='static')
from .models import Posts


@posts.route('/')
def index():
    return render_template('posts/index.html')


@posts.route('/new/', methods=['POST', 'GET'])
def new_posts():
    # db.create_all()
    form = Posts_Form()
    title = ''
    text = ''
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        post = Posts(title=title, text=text)
        db.session.add(post)
        db.session.commit()
    return render_template('posts/new_posts.html', title=title, text=text, form=form)


@posts.route('/all')
def all_posts():
    post = Posts.query.all()
    return render_template('posts/all.html', post=post)



# @posts.route('/new/', methods=['POST', 'GET'])
# def new_posts():
#     form = Vlasnik()
#     name = ''
#     age = ''
#     city = ''
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         city = request.form['city']
#     clients_list.append({'id': len(clients_list) + 1, 'name': name, 'age': age, 'city': city, 'pets': []})
#     return render_template('posts/new_posts.html', name=name, age=age, city=city, form=form)


@posts.route('/new/pet', methods=['POST', 'GET'])
def pet_posts():
    form_pet = Pet()
    name_pet = ''
    age_pet = ''
    typ_pet = ''
    if request.method == 'POST':
        name_pet = request.form['name_pet']
        age_pet = request.form['age_pet']
        typ_pet = request.form['typ_pet']
    return render_template('posts/pet_posts.html', name_pet=name_pet, age_pet=age_pet, typ_pet=typ_pet,
                           form_pet=form_pet, )

# @posts.route('/typ/cet')
# def cet():
#     dik = pet_posts.dik
#     return render_template('posts/cet.html', dik=dik )
