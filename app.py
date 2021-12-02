import os
from flask import Flask, request, session, redirect, render_template
from flask import send_file, make_response
from models import db, Plant_sensor
from datetime import datetime
from insert_db import Insert_DB # 센서 값을 읽어와 DB에 저장하는 함수
from create_graph import show_graph # DB의 정보들로 그래프를 그리는 함수
from apscheduler.schedulers.background import BackgroundScheduler # scheduler

sched = BackgroundScheduler()
sched.add_job(Insert_DB, 'interval', minutes = 30) # insert_db 함수 30분마다 실행 스케쥴러 정의

app=Flask(__name__, static_url_path='/static',)

@app.route('/show_condition_graph')
def show_condition_graph():
    show_graph()

    return render_template("show_graph.html", width=400, height=300)

@app.route('/show_condition_table')
def show_condition():
    show_condition = db.session.query(Plant_sensor.time, Plant_sensor.tem, Plant_sensor.hum,
								Plant_sensor.lum, Plant_sensor.moi).all()

    return render_template('show_tem_h.html', condition = show_condition, count = len(show_condition))

# html을 컨트롤러에서 만들어서 View로 전달하는데 컨트롤러와 View를 분리
# /127.0.0.1 '/'
@app.route('/')
def hello():

    return render_template('hello.html')

basedir=os.path.abspath(os.path.dirname(__file__))
print('basedir:{}'.format(basedir))
dbfile=os.path.join(basedir,'Plant_DB')
print('file:{}'.format(dbfile))

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)
db.app = app
db.create_all()
sched.start() # scheduler 시작
app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
