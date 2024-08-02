import time
import sys
sys.path.append('/home/pi/MasterPi/')
import HiwonderSDK.Board as Board

# Board.setMotor(Motor#, Speed) 
# 1 - front left
# 2 - front right
# 3 - back left
# 4 - back right
# this will stop each motor
Board.setMotor(1, 0) 
Board.setMotor(2, 0)
Board.setMotor(3, 0)
Board.setMotor(4, 0)

# this will run motor 1 at 30% power
Board.setMotor(1, 30)
#time.sleep(1)
# this will stop motor1
Board.setMotor(1, 0)