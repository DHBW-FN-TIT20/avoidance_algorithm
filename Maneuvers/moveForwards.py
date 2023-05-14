#!/usr/bin/env python3

from ev3dev2.motor import *
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_2
import time

drive = LargeMotor(OUTPUT_A)
steering = LargeMotor(OUTPUT_B)
gyro = GyroSensor(INPUT_2)

gyro.calibrate()
gyro.reset()
steering.position = 0

def moveForwards(event):
	while True:
		drive.on(SpeedDPS(90), True)
		if gyro.angle < -3:
			steering.on_for_degrees(speed=SpeedDPS(90), degrees=-45, brake=True, block=False)
			while gyro.angle <= 0:
                                print(str(gyro.angle))
			steering.on_for_degrees(speed=SpeedDPS(90), degrees=((steering.position + 5)*-1), brake=True, block=False)
		if gyro.angle > 3:
			steering.on_for_degrees(speed=SpeedDPS(90), degrees=45, brake=True, block=False)
			while gyro.angle >= 0:
				print(str(gyro.angle))
			steering.on_for_degrees(speed=SpeedDPS(90), degrees=((steering.position + 5)*-1), brake=True, block=False)
		if event.is_set():
			drive.off()
			time.sleep(3)
			break
	print("moveThread closed")
