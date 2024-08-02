import time
import sys
sys.path.append('/home/pi/MasterPi/')
import HiwonderSDK.Board as Board

Board.setPWMServoPulse(1, 1500, 500)
Board.setPWMServoPulse(3, 500, 1000)
Board.setPWMServoPulse(4, 2500, 1000)
Board.setPWMServoPulse(5, 1000, 1000)
Board.setPWMServoPulse(6, 1500, 1000)
