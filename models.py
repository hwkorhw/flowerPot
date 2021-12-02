from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant_sensor(db.Model):
    __tablename__ = 'Plant_sensor'
    time = db.Column(db.String(50), primary_key=True)
    tem = db.Column(db.Float, unique = False)
    hum = db.Column(db.Float, unique = False)
    lum = db.Column(db.Integer, unique = False)
    moi = db.Column(db.Integer, unique = False)
