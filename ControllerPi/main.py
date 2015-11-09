# Controls the rotating platform
#
# The servo rotates the platform through a friction wheel.
# This wheel can slip when it is blocked in any way as a protection.
#
# A connected webcam looks down on the platform to control position.
import datetime
import requests

import serial

import time

import sys

ser = serial.Serial(sys.argv[1],9600)

import imaging

counter = 0

def turn_and_capture(counter):
    imaging.capture('no session')
    ser.write(chr(5))
    counter = counter+1
    if(counter < 100):
        turn_and_capture(counter)

turn_and_capture(counter)
