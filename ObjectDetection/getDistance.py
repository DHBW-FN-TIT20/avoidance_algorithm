#!/usr/bin/env python3

from ev3dev2.sensor.lego import UltrasonicSensor

us = UltrasonicSensor()

def getDistance():
	return us.value()/10
