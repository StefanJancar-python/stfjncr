import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
SECRET_KEY = os.environ.get('SECRET_KEY') or b'\nN\xff{\x9d\x11S\xd5\x82=)\x14\x93\xe2Dv'
LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
UPLOAD_FOLDER = app.static_folder + "/uploads/"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024