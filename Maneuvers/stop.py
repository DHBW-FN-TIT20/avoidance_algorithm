#!/usr/bin/env python3

from ev3dev2.motor import *

lm = LargeMotor(OUTPUT_A)

def stop():
	lm.off()

stop()
