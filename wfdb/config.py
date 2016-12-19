class Config(object):
    SECRET_KEY = '11bbd83a61b32c7c86a99c956ae2093ffbc5d43ba459ef01'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:dragon789@localhost/wfdb"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:dragon789@localhost/wfdb"
    DEBUG = True
