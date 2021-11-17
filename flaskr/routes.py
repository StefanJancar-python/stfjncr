from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, make_response
)
from hashlib import md5

bp = Blueprint('routes', __name__)

@bp.route('/')
@bp.route('/domov')
def domov():
	return render_template('domov/domov.html', title="Úvod")


@bp.route('/dna')
def dna():
	return render_template('domov/clanky/dna.html', title="Biohacker")

@bp.route('/blog')
def sanity_blog():
	return render_template('domov/clanky/sanity.html', title="Sanity blog")


@bp.route('/stroj')
def stroj():
	return render_template('domov/clanky/stroj.html', title="Človek vs stroj")

@bp.route('/odkazy')
def odkazy():
	return render_template('domov/odkazy/odkazy.html', title="Flask odkazy")


@bp.route('/cnctutorial')
def cnctutorial():
	return render_template('domov/cnc_tutorial/cnc.html', title="Cnc tutoriál")

@bp.route('/cv')
def cv():                                                           
	return render_template('domov/cv.html', title="CV")

@bp.route('/kurzy')
def kurzy():
                                                           
	return render_template('domov/kurzy.html', title="KURZY")








    
         