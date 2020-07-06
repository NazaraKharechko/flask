from flask import Flask

from config import DevConf
from .posts.views import posts

app = Flask(__name__)
# app.config['DEBUG'] = True  # 1
# app.config.update(DEBUG=True)  # 2
# app.config.from_json('..\config.json') # 3
app.config.from_object(DevConf)

app.register_blueprint(posts, url_prefix='/posts')

from app import views
