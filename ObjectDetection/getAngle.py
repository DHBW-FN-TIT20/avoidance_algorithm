#!/usr/bin/env python3

from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import *
import time

us = UltrasonicSensor()
lm = LargeMotor(OUTPUT_A)

#returns the angle of the next outer edge (0 degrees = direction of travel).
def getAngle():
	lm.position=0
	distanceOld = us.value()/10
	positionR = 90
	positionL = -90

	while lm.position < 90:
		distance = us.value()/10
		print(distance, "cm / " + str(lm.position) + "pos")
		lm.on(SpeedDPS(45), True)
		
		if (distance - distanceOld) >= 10:
			lm.off()
			positionR = lm.position
			break
		else:
			distanceOld = distance

	lm.on_for_degrees(speed=SpeedDPS(90), degrees=-90, brake=True, block=True)
	print("Zero Position: " + str(lm.position))
	distanceOld = us.value()/10

	while lm.position > -90:
		distance = us.value()/10
		print(distance, "cm / " + str(lm.position) + "pos")
		lm.on(SpeedDPS(-45), True)

		if (distance - distanceOld) >= 10:
			lm.off()
			positionL = lm.position
			break
		else: 
			distanceOld = distance
	
	lm.off()

	if positionR < (positionL * -1):
		return positionR
	elif positionR > (positionL * -1):
		return positionL
	else:
		return 0

print("Angle: " + str(getAngle()))

