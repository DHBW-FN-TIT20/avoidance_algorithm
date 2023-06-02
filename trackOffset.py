#!/usr/bin/env python3

import math
from ev3dev2.motor import *
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_2
from Helper.printText import writeScreen

gyro = GyroSensor(INPUT_2)
drive = LargeMotor(OUTPUT_A)
steering = LargeMotor(OUTPUT_B)

drive.position = 0
steering.position = 0

gyro.calibrate()
gyro.reset()

offset = 0
oldAngle = gyro.angle

# calculates the distance of the "opposite side" with sinus
def calculateOffset(angle):
	# the distance per degree of the turn radius
	distance = 0.683
	offset = math.sin(math.radians(angle)) * distance
	return offset

while True:
	newAngle = gyro.angle

	if newAngle != oldAngle:
		offset = offset + calculateOffset(newAngle)
		oldAngle = newAngle
	print("old angle: " + str(oldAngle) + ", offset: " + str(offset))
