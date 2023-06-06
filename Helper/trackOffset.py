#!/usr/bin/env python3

import math
from ev3dev2.motor import *
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_2
from Helper.printText import writeScreen

gyro = GyroSensor(INPUT_2)
drive = LargeMotor(OUTPUT_A)
steering = LargeMotor(OUTPUT_B)

gyro.calibrate()
gyro.reset()

# calculates the distance of the "opposite side" with sinus
def calculateOffset(angle):
	distance = drive.position
	# translate the degrees of the motor in cm (1cm = 27,4 degree)
	distance = distance / 27.4
	offset = math.sin(math.radians(angle)) * distance
	return offset

def offsetThread(event):
	offset = 0
	oldAngle = gyro.angle
	newAngle = oldAngle
	print("--------------------------------")
	while True:

		if offset > 16.3 and offset < 16.7 and newAngle < 0:
			print("angle: " + str(newAngle))
			event.set()

		drive.position = 0

		while newAngle == oldAngle:
			newAngle = gyro.angle
			if event.is_set():
				break
			#print("drive.position = " + str(drive.position))

		offset = offset + calculateOffset(newAngle)
		oldAngle = newAngle
		#print("old angle: " + str(oldAngle) + ", offset: " + str(offset))
		print("offset: " + str(offset))
		if event.is_set():
			print("event is set")
			break

