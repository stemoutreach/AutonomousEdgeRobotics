# **1 Desktop Pi Image** 

1. **Create a fresh Raspberry Pi OS**
  Use Raspberry Pi Imager to create a fresh Raspberry Pi OS (64-bit) SD card
   - https://www.raspberrypi.com/software/
   - current imager version 1.8.5
   - Original Pi OS Released: 2024-03-15
   - Current Pi OS Released: 2024-07-04
  
3. **Boot the Raspberry Pi with the new card**

1. **change defaul password for pi**

   Note: pi default password is raspberry

   run the passwd command in a teminal window and follow instructions
   
    ~~~
    passwd
    ~~~
    
1. **Enable interface:** ssh and vnc

    ~~~
    sudo raspi-config
    ~~~
    Optional - change Hostname: raspi-config / 1. system options / S4 Hostname 

1. **Update OS to current patch level**

    ~~~
    sudo apt-get update && sudo apt-get upgrade -y
    ~~~
    
1. **Remove installed packages that are no longer required**

    ~~~
    sudo apt autoremove -y
    ~~~
    
    1. **Remove update block**

    ~~~
    sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
    ~~~
    
1. **Install tensorflow lite and OpenVC**

    ~~~
    pip3 install opencv-contrib-python
    ~~~

1. **View OpenCV version that was installed (4.10.0)**

    ~~~
    python3 -c "import cv2; print(cv2.__version__)"
    ~~~
    OpenCV version = 4.10.0

1. **Install RealVNC Viewer**

    - Download from https://www.realvnc.com/en/connect/download/combined/
    - Select ARM64
    - Download
    - Extract
    - run this file VNC-Connect-Installer-2.2.1-Linux-ARM64

 1. **Install Juptyer Notebook**

  ~~~
  pip3 install jupyter
  ~~~
