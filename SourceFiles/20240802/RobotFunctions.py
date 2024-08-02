import time
import sys
sys.path.append('/home/pi/MasterPi/')
import HiwonderSDK.Board as Board
import HiwonderSDK.Sonar as Sonar
HWSONAR = Sonar.Sonar() #ultrasonic sensor


def Buzzer1():
    Board.setBuzzer(0)
    Board.setBuzzer(1)
    time.sleep(.1)
    Board.setBuzzer(0)


def MotorStop(): # stop all motors 
    Board.setMotor(1, 0) 
    Board.setMotor(2, 0)
    Board.setMotor(3, 0)
    Board.setMotor(4, 0)

def Forward(speed):
    Board.setMotor(1, speed) 
    Board.setMotor(2, speed)
    Board.setMotor(3, speed)
    Board.setMotor(4, speed)

def Reverse(speed):
    Board.setMotor(1, -speed) 
    Board.setMotor(2, -speed)
    Board.setMotor(3, -speed)
    Board.setMotor(4, -speed)

def TurnRight(speed):
    Board.setMotor(1, speed) 
    Board.setMotor(2, -speed)
    Board.setMotor(3, speed)
    Board.setMotor(4, -speed)

def TurnLeft(speed):
    Board.setMotor(1, -speed) 
    Board.setMotor(2, speed)
    Board.setMotor(3, -speed)
    Board.setMotor(4, speed)

def StrafeRight(speed):
    Board.setMotor(1, speed) 
    Board.setMotor(2, -speed)
    Board.setMotor(3, -speed)
    Board.setMotor(4, speed)

def StrafeLeft(speed):
    Board.setMotor(1, -speed) 
    Board.setMotor(2, speed)
    Board.setMotor(3, speed)
    Board.setMotor(4, -speed)
    
def PickupBlock():
    Board.setPWMServoPulse(1, 2500, 2000)
    Board.setPWMServoPulse(4, 1900, 2000)
    Board.setPWMServoPulse(5, 2500, 2000)
    time.sleep(2)

    Board.setPWMServoPulse(1, 1600, 1000)
    time.sleep(1)

    Board.setPWMServoPulse(3, 500, 1000)
    Board.setPWMServoPulse(4, 2500, 1000)
    Board.setPWMServoPulse(5, 1000, 1000)
    Board.setPWMServoPulse(6, 1500, 1000)
    time.sleep(1)
    
def DropBlock():
    Board.setPWMServoPulse(1, 2000, 500)
    
def LookDown():
    Board.setPWMServoPulse(5, 1600, 500)
    
def Initialize():
    
    MotorStop()
    Board.setPWMServoPulse(1, 1500, 500)
    Board.setPWMServoPulse(3, 500, 1000)
    Board.setPWMServoPulse(4, 2500, 1000)
    Board.setPWMServoPulse(5, 1000, 1000)
    Board.setPWMServoPulse(6, 1500, 1000)
    time.sleep(1)
    HWSONAR.setRGBMode(0)
    HWSONAR.setPixelColor(0, Board.PixelColor(0,0,0))
    HWSONAR.setPixelColor(1, Board.PixelColor(0,0,0))    
    HWSONAR.show()


def DelieverBlock():

    PickupBlock()
    TurnLeft(40)
    time.sleep(1.4)
    MotorStop()
    Forward(50)
    time.sleep(2)
    DropBlock()
    MotorStop()
    TurnRight(40)
    time.sleep(1.4)
    MotorStop()
    Initialize()
