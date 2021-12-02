import os
from flask import Flask, session
from models import db, Plant_sensor
from datetime import datetime
import dht_simpletest
import light_sensor as light_s
import adc_module

# lum -> 평상시(백열등) : 350 ~ 550 / 빛 : 150 ~ 300

def Insert_DB():
	print("----{}----sensing----".format(datetime.now()))
	plant_sensor = Plant_sensor()

	now = datetime.now()
	time = now.strftime('%Y-%m-%d %H:%M:%S')

	plant_sensor.tem, plant_sensor.hum = dht_simpletest.tem_h()
	plant_sensor.time = time

	plant_sensor.lum = light_s.rc_time(4)
	plant_sensor.moi = adc_module.get_adcvalue()

	db.session.add(plant_sensor)
	db.session.commit()
	print("----complete sensing----")
