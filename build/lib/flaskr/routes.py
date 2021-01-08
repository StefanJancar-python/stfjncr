from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('routes', __name__)

@bp.route('/')

def uvod():
	return render_template('uvod/uvod.html')


                                                  



	     

    
         