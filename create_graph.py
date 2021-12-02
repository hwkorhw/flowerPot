from flask import send_file, make_response, session
from flask import make_response
from models import db, Plant_sensor
from io import BytesIO
import numpy as np 
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

## remove cache 
from functools import wraps, update_wrapper
from datetime import datetime

def nocache(view):
  @wraps(view)
  def no_cache(*args, **kwargs):
    response = make_response(view(*args, **kwargs))
    response.headers['Last-Modified'] = datetime.now()
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response      
  return update_wrapper(no_cache, view)
###############

@nocache
def show_graph():
    t = db.session.query(Plant_sensor.time).all()
    t = list(t)
    date = list()
    for i, v in enumerate(t):
    	d[i] = v[2:].split('-')
    	s[i] = v[11:16].split(':')
    	date.append(''.join(s[i]))

    tem = db.session.query(Plant_sensor.tem).all()
    fig(4,3, date, tem, 'tem')

    hum = db.session.query(Plant_sensor.hum).all()
    fig(4,3, date, hum, 'hum')

    moi = db.session.query(Plant_sensor.moi).all()
    fig(4,3, date, moi, 'moi')

    return 'ok'

def fig(xsize, ysize, x, y, name):
    plt.figure(figsize=(xsize, ysize))
    xs = x
    ys = y
    plt.plot(xs,ys)

    img1 = BytesIO()
    plt.savefig('static/img_'+name+'.png', format='png', dpi=300)
