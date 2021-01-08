from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, make_response
)

bp = Blueprint('routes', __name__)

@bp.route('/')
def uvod():
                                                           
	return render_template('uvod/uvod.html')

@bp.route('/dna')
def dna():
	return render_template('clanky/dna.html')

@bp.route('/stroj')
def stroj():
	return render_template('clanky/stroj.html')



    
         