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
        os.system('mpg123 -q 1.mp3 &')
 
    if (GPIO.input(24) == False):
        os.system('mpg321 http://stream.srg-ssr.ch/m/drs3/mp3_128 &')
 
    if (GPIO.input(25)== False):
        os.system('mpg123 -q 3.mp3 &')
 
    sleep(0.1);
