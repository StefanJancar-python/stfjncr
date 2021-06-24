from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, make_response
)
from hashlib import md5

bp = Blueprint('routes', __name__)

@bp.route('/')
def uvod():
                                                           
	return render_template('uvod/uvod.html', title="Úvod")

@bp.route('/blog')
def sanity_blog():
	return render_template('clanky/sanity.html', title="Sanity blog")
	


@bp.route('/dna')
def dna():
	return render_template('clanky/dna.html', title="Biohacker")

@bp.route('/stroj')
def stroj():
	return render_template('clanky/stroj.html', title="Človek vs stroj")

@bp.route('/odkazy')
def odkazy():
	return render_template('odkazy/odkazy.html', title="Flask odkazy")


@bp.route('/cnctutorial')
def cnctutorial():
	return render_template('cnc_tutorial/cnc.html', title="Cnc tutoriál")







    
         