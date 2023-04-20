#!/usr/bin/env python3

from ev3dev2.motor import *

lm = LargeMotor(OUTPUT_A)

def moveForwards():
	lm.on(SpeedDPS(90), True)

moveForwards()
