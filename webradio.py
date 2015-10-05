#!/usr/bin/env python
 
import os
from time import sleep
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
 
while True:
    if (GPIO.input(24) == False):
        os.system('./play.sh &')

    if (GPIO.input(25) == False):
        os.system('./stop.sh &')
 
    if (GPIO.input(23)== False):
        os.system('./next.sh &')
 
    sleep(0.5);
