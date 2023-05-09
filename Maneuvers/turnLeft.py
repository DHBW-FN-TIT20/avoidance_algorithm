#!/usr/bin/env python3

from ev3dev2.motor import *
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_2

gyro = GyroSensor(INPUT_2)
drive = LargeMotor(OUTPUT_A)
steering = LargeMotor(OUTPUT_B)

def turnLeft(gyroPos):
	steering.on_for_degrees(speed=SpeedDPS(90), degrees=65, brake=True, block=True)
	while gyro.angle >= (gyroPos-90):
		#print(str(gyro.angle))
		drive.on(speed=SpeedDPS(90))
	drive.off()

	steering.on_for_degrees(speed=SpeedDPS(90), degrees=-65, brake=True, block=True)

