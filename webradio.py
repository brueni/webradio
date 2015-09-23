#!/usr/bin/env python
 
import os
from time import sleep
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
 
while True:
    if (GPIO.input(23) == False):
        os.system('./play.sh &')
# 	os.spawnl(os.P_NOWAIT, './play.sh &')

    if (GPIO.input(24) == False):
        os.system('./stop.sh &')
 
#    if (GPIO.input(25)== False):
#        os.system('mpg123 -q 3.mp3 &')
 
    sleep(0.5);
