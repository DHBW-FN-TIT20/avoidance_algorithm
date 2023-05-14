#!/usr/bin/env python3

from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import *
from ev3dev2.sensor import INPUT_1
import time

us = UltrasonicSensor(INPUT_1)
usMotor = LargeMotor(OUTPUT_C)

usMotor.position = 0

#returns the angle of the object related to the vehicle
# angle > 90: right side of the object is far away
# angle < 90: left side of the object is far away
def getAngleOfObject():
  angle = -90
  distanceOld = us.value()/10
  usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=-90, brake=True, block=True)
  usMotor.on(SpeedDPS(45),True)

#why does it return the last position everytime
  while usMotor.position < 90:
    distance = us.value()/10
    time.sleep(0.2)
    if distance < distanceOld:
      angle = usMotor.position
    else:
      distanceOld = distance
  usMotor.off()
  usMotor.on_for_degrees(speed=SpeedDPS(90), degrees=(usMotor.position*-1), brake=True, block=True)
  return (90 - angle)
    
print(str(getAngleOfObject()))
time.sleep(2)
  
