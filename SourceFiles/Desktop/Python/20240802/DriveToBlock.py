# coding=utf8
import sys
sys.path.append('/home/pi/MasterPi')
import time
from RobotFunctions import *


Initialize()

Forward(30)
time.sleep(.5)
MotorStop()

PickupBlock()

TurnRight(40)
time.sleep(1.9)
MotorStop()

Forward(50)
time.sleep(1.5)
MotorStop()

DropBlock()

Buzzer1()

#StrafeRight(40)
time.sleep(.5)
MotorStop()

#Forward(50)
time.sleep(.5)
MotorStop()
