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
positive = None

# calculates the distance of the "opposite side" with sinus
def calculateOffset(angle):
	# the distance per degree of the turn radius
	distance = 0.683
	offset = math.sin(math.radians(angle)) * distance
	return offset

drive.on(SpeedDPS(90), True)
while True:
	newAngle = gyro.angle

	if newAngle == 90:
		drive.position = 0
		while gyro.angle == 90:
			print(gyro.angle)
		print("---------------- offset: " + str(offset))
		offset = offset + (drive.position / 27.4)
		print("---------------- new offset: " + str(offset))

	if newAngle == -90:
                drive.position = 0
                while gyro.angle == -90:
                        print(gyro.angle) 
                offset = offset - (drive.position / 27.4)

	if newAngle != oldAngle:
		offset = offset + calculateOffset(newAngle)
		oldAngle = newAngle
	print("old angle: " + str(oldAngle) + ", offset: " + str(offset))

