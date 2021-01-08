import os


class Config(object):

SECRET_KEY = b',\xcc\xab\xb4\xa38"Z"5\xed\x85SM\x0c<'
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') is True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
ADMINS = ['python89222@gmail.com']