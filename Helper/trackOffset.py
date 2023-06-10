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
#calculates the relative distance to the route and returns True, if its time to drive to the route
def returnToRoute(offset, angle):
	a = offset/(math.cos(math.radians(90 + angle)))
	if a <= 25 and angle < 0:
		return True
	else:
		return False

def offsetThread(event):
	offset = 0
	oldAngle = gyro.angle
	newAngle = oldAngle
	while True:

		if returnToRoute(offset, newAngle):
			event.set()

		drive.position = 0

		while newAngle == oldAngle:
			newAngle = gyro.angle
			#print("drive.position = " + str(drive.position))

		offset = offset + calculateOffset(newAngle)
		oldAngle = newAngle
		#print("old angle: " + str(oldAngle) + ", offset: " + str(offset))

