#!/usr/bin/env python3

from ev3dev2.motor import *
from ev3dev2.sensor.lego import UltrasonicSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2
from Helper.printText import writeScreen
from ObjectDetection.getDistance import getDistance
from ObjectDetection.getAngle import getAngle
from Maneuvers.moveForwards import moveForwards
from Maneuvers.stop import stop
from Maneuvers.turnRight import turnRight
from Maneuvers.turnLeft import turnLeft
import time
from threading import Thread

moveThread = Thread(target= moveForwards)

us = UltrasonicSensor(INPUT_1)
gyro = GyroSensor(INPUT_2)
drive = LargeMotor(OUTPUT_A)
steering = LargeMotor(OUTPUT_B)
usMotor= LargeMotor(OUTPUT_C)

usMotor.position = 0
steering.position = 0

gyro.calibrate()
gyro.reset()

while getDistance() >= 33:
	#drive.on(SpeedDPS(90), True)
	moveThread.start()
	writeScreen(str(getDistance()))
moveThread.join()
stop()

angle = getAngle()

if angle > 0:
	turnRight(0)
	usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=-80, brake=True, block=True)
else:
	turnLeft(0)
	usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=80, brake=True, block=True)
time.sleep(1)
drive.position = 0
#------------------------------------------------------------------------------------------
while getDistance() < 25:
	drive.on(SpeedDPS(90), True)
	writeScreen(str(getDistance()))
stop()

usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=(usMotor.position)*-1, brake=True, block=True)
offset = drive.position

if gyro.angle < 0:
	turnRight(gyro.angle)
	usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=80, brake=True, block=True)
else:
	turnLeft(gyro.angle)
	usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=-80, brake=True, block=True)

while getDistance() < 25:
        drive.on(SpeedDPS(90), True)
stop()

usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=(usMotor.position)*-1, brake=True, block=True)


if angle > 0:
	turnLeft(gyro.angle)
else:
	turnRight(gyro.angle)

#move the offset degrees
drive.on_for_degrees(speed=SpeedDPS(90), degrees=offset, brake=True, block=True)

if angle > 0:
	turnRight(gyro.angle)
else:
	turnLeft(gyro.angle)

#move 10cm
drive.on_for_degrees(speed=SpeedDPS(90), degrees=280, brake=True, block=True)

