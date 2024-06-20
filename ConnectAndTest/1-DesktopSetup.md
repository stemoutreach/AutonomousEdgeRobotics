# **1 Pi Desktop Setup**


## Prerequisites:

1. SD card is in the Raspberry Pi 5
1. Robot Pi is connected to monitor and keyboard
1. Power is connected and Pi desktop is running

<img src="https://github.com/stemoutreach/AutonomousEdgeRobotics/blob/main/GettingStarted/zzimages/PiDesktop.jpg" width="500" > 

## Steps:

1. **Change defaul password and hostname**

   Open the Configuation tool at **Pi -> Preferences -> Raspberry Pi Configuation** and follow instructions. Make the hostname unique. Maybe use your team name or initials.   
   
   <img src="https://github.com/stemoutreach/AutonomousEdgeRobotics/blob/main/zzimages/OpenTerminal2.jpg" width="500" > 


1. **Connect to WiFi**

   Check the network icon in the top right side of the Taskbar. If the network icon looks like the image below, click the new=twork icon and select the correct network to connect to. 

   <img src="https://github.com/stemoutreach/AutonomousEdgeRobotics/blob/main/zzimages/wifisetup-01.jpg" width="200" > 
   
1. **Open a Terminal window**

   Throughout this workshop, you will be asked to open a Terminal window when there is a commend to enter. You can open a terminal window by using the menu bar at the top of the screen (see image below) or use and use Ctrl+alt+t. 

   <img src="https://github.com/stemoutreach/AutonomousEdgeRobotics/blob/main/zzimages/OpenTerminal2.jpg" width="500" > 
   

1. **Run Camera test**

   Open a terminal window and run the following.

    ~~~
    python CameraTest.py
    ~~~

1. **Jupyter Lab Connection** 
  
   ~~~
   cd /home/pi/Desktop
   jupyter notebook --ip='*' --port=8888 
   ~~~

   First time login - create a password
   - Copy the token from the terminal window 
   - Open a browser and connect to http://XXX.XXX.XXX.XXX:8888
   - Use the token copied from the terminal window and paste it in the section **Setup a Password** then add your own password 
