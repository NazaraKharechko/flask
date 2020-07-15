from wtforms import Form, StringField


class Posts_Form(Form):
    title = StringField('Title')
    text = StringField('Text')


class Vlasnik(Form):
    name = StringField('Name')
    age = StringField('Age')
    city = StringField('City')


class Pet(Form):
    name_pet = StringField('Name_pet')
    age_pet = StringField('Age_pet')
    typ_pet = StringField('Type_pet')
