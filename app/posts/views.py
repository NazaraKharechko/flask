from flask import Blueprint, render_template, request

from app.forms import Vlasnik, Pet

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='static')


@posts.route('/')
def index():
    return render_template('posts/index.html')


# @posts.route('/new/', methods=['POST', 'GET'])
# def new_posts():
#     form = Posts_Form()
#     name = ''
#     mail = ''
#     if request.method == 'POST':
#         name = request.form['name']
#         mail = request.form['mail']
#     return render_template('posts/new_posts.html', name=name, mail=mail, form=form)


@posts.route('/new/', methods=['POST', 'GET'])
def new_posts():
    form = Vlasnik()
    name = ''
    age = ''
    city = ''
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']

    if name != '':
        for k, v in request.form.items():
            print('k =', k, 'v =', v)
    return render_template('posts/new_posts.html', name=name, age=age, city=city, form=form)


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
                           form_pet=form_pet, dik=dik)


# @posts.route('/typ/cet')
# def cet():
#     dik = pet_posts.dik
#     return render_template('posts/cet.html', dik=dik )
