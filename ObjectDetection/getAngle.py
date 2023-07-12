#!/usr/bin/env python3

from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import *
from ev3dev2.sensor import INPUT_1, INPUT_2

us = UltrasonicSensor()
lm = LargeMotor(OUTPUT_C)

#returns the angle of the next outer edge (0 degrees = direction of travel).
def getAngle():
	lm.position=0
	distanceOld = us.value()/10
	positionR = 90
	positionL = -90

	while lm.position < 90:
		distance = us.value()/10
		lm.on(SpeedDPS(45), True)
		
		if (distance - distanceOld) >= 10:
			lm.off()
			positionR = lm.position
			break
		else:
			distanceOld = distance

	lm.on_for_degrees(speed=SpeedDPS(90), degrees=(lm.position)*-1, brake=True, block=True)
	distanceOld = us.value()/10

	while lm.position > -90:
		distance = us.value()/10
		lm.on(SpeedDPS(-45), True)

		if (distance - distanceOld) >= 10:
			lm.off()
			positionL = lm.position
			break
		else: 
			distanceOld = distance
	
	lm.off()
	lm.on_for_degrees(speed=SpeedDPS(90), degrees=(positionL*-1), brake=True, block=True)

	if positionR < (positionL * -1):
		return positionR
	elif positionR > (positionL * -1):
		return positionL
	else:
		return 0


