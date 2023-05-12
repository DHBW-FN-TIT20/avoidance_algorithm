#!/usr/bin/env python3

from ev3dev2.motor import *
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1

us = UltrasonicSensor(INPUT_1)
drive = LargeMotor(OUTPUT_A)
steering = LargeMotor(OUTPUT_B)
usMotor = LargeMotor(OUTPUT_C)

usMotor.position = 0
steering.position = 0

usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=-80, brake=True, block=True)

def turnStraight():
        steering.on_for_degrees(speed=SpeedDPS(90), degrees=(steering.position)*-1, brake=True, block=True)

# c = 20.5
drive.on(speed=SpeedDPS(90))
while True:

	if us.value()/10 > 22:
		steering.on_for_degrees(speed=SpeedDPS(90), degrees=30, brake=True, block=True)
		while us.value()/10 > 20.5:
			print(str(us.value()/10))
		steering.on_for_degrees(speed=SpeedDPS(90), degrees=(steering.position)*-1, brake=True, block=True)

	if us.value()/10 < 19:
		steering.on_for_degrees(speed=SpeedDPS(90), degrees=-30, brake=True, block=True)
		while us.value()/10 < 20.5:
			print(str(us.value()/10))
		steering.on_for_degrees(speed=SpeedDPS(90), degrees=(steering.position)*-1, brake=True, block=True)
