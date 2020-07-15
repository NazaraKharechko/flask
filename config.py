class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/flask_posts'


class DevConf(Config):
    DEBUG = True


class ProdConf(Config):
    DEBUG = False