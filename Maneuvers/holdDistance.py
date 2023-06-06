#!/usr/bin/env python3

from ev3dev2.motor import *
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1

us = UltrasonicSensor(INPUT_1)
drive = LargeMotor(OUTPUT_A)
steering = LargeMotor(OUTPUT_B)
usMotor = LargeMotor(OUTPUT_C)

def holdDistance(event):
#move the us sensor to -80 degree
	usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=-80, brake=True, block=True)

	while True:

		if us.value()/10 > 21:
			steering.on_for_degrees(speed=SpeedDPS(90), degrees=65, brake=True, block=True)
			while us.value()/10 > 20:
				#print(str(us.value()/10))

				if event.is_set():
					print("distance event is set")
					usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=80, brake=True, block=True)
					steering.on_for_degrees(speed=SpeedDPS(90), degrees=-70, brake=True, block=True)
					break

			steering.on_for_degrees(speed=SpeedDPS(90), degrees=-70, brake=True, block=True)

		if us.value()/10 < 19:
			steering.on_for_degrees(speed=SpeedDPS(90), degrees=-65, brake=True, block=True)
			while us.value()/10 < 20:
				#print(str(us.value()/10))
				drive.on(speed=SpeedDPS(90))
			steering.on_for_degrees(speed=SpeedDPS(90), degrees=70, brake=True, block=True)
		
		if event.is_set():
			print("distance event is set")
			usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=80, brake=True, block=True)
			break
