from flask import render_template, Blueprint
from flaskr.db import get_db

bp = Blueprint('errors', __name__)

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    db = get_db()
    return render_template('errors/500.html'), 500