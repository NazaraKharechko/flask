from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevConf

app = Flask(__name__)
# app.config['DEBUG'] = True  # 1
# app.config.update(DEBUG=True)  # 2
# app.config.from_json('..\config.json') # 3
app.config.from_object(DevConf)

db = SQLAlchemy(app)
from .posts.views import posts
app.register_blueprint(posts, url_prefix='/posts')

from app import views
