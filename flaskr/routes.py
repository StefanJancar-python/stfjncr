from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, make_response
)
from hashlib import md5

bp = Blueprint('routes', __name__)

@bp.route('/')
def uvod():
                                                           
	return render_template('uvod/uvod.html', name="Úvod")

@bp.route('/blog')
def sanity_blog():
	return render_template('clanky/sanity.html', name="Blog")
	


@bp.route('/dna')
def dna():
	return render_template('clanky/dna.html', name="Dna")

@bp.route('/stroj')
def stroj():
	return render_template('clanky/stroj.html', name="Stroj")





    
         