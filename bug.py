#!/usr/bin/env python3

from ev3dev2.motor import *
from ev3dev2.sensor.lego import UltrasonicSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2
from Helper.printText import writeScreen
from Helper.trackOffset import offsetThread
from ObjectDetection.getDistance import getDistance
from ObjectDetection.getAngle import getAngle
from Maneuvers.moveForwards import moveForwards
from Maneuvers.stop import stop
from Maneuvers.turnRight import turnRight
from Maneuvers.turnLeft import turnLeft
from Maneuvers.holdDistance import holdDistance

from threading import Thread, Event

offsetEvent = Event()
calcOffsetThread = Thread(target = offsetThread, args=(offsetEvent,))
distanceEvent = Event()
distanceThread = Thread(target = holdDistance, args=(distanceEvent,))

us = UltrasonicSensor(INPUT_1)
gyro = GyroSensor(INPUT_2)
drive = LargeMotor(OUTPUT_A)
steering = LargeMotor(OUTPUT_B)
usMotor= LargeMotor(OUTPUT_C)

gyro.calibrate()
gyro.reset()

usMotor.position = 0
steering.position = 0

drive.on(SpeedDPS(90), True)

# drive to the obstacle while the distance is bigger than 33cm
while getDistance() >= 33:
	writeScreen("Distance: " + str(getDistance()))
stop()
steering.on_for_degrees(speed=SpeedDPS(90), degrees=-65, brake=True, block=True)
usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=-80, brake=True, block=True)

#start the calcOffsetThread
calcOffsetThread.start()
drive.on(SpeedDPS(90), True)

# make a right turn until the distance is smaller or equal to 25cm
while getDistance() >= 25:
	writeScreen("Distance:" + str(getDistance()))
stop()
steering.on_for_degrees(speed=SpeedDPS(90), degrees=65, brake=True, block=True)
usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=80, brake=True, block=True)

#start the distanceThread to drive around the obstacle
distanceThread.start()
drive.on(SpeedDPS(90))


#the car drives now around the obsticle until the offsetEvent is triggered
while not(offsetEvent.is_set()):
	writeScreen("degrees: " + str(gyro.angle))
distanceEvent.set()
stop()
steering.on_for_degrees(speed=SpeedDPS(90), degrees=-65, brake=True, block=True)
drive.on(SpeedDPS(90))

#the car drives now to the origin route
while gyro.angle != 0:
	writeScreen(str(gyro.angle))
stop()
steering.on_for_degrees(speed=SpeedDPS(90), degrees=65, brake=True, block=True)

