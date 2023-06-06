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
newAngle = oldAngle

# calculates the distance of the "opposite side" with sinus
def calculateOffset(angle):
	distance = drive.position
	# translate the degrees of the motor in cm (1cm = 27,4 degree)
	distance = distance / 27.4
	offset = math.sin(math.radians(angle)) * distance
	return offset

drive.on(SpeedDPS(90), True)
while True:

	while newAngle == oldAngle:
		newAngle = gyro.angle
		print("drive.position = " + str(drive.position))
	offset = offset + calculateOffset(newAngle)
	oldAngle = newAngle
	drive.position = 0
	print("old angle: " + str(oldAngle) + ", offset: " + str(offset))

