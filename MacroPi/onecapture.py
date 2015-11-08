# Controls the rotating platform
#
# The servo rotates the platform through a friction wheel.
# This wheel can slip when it is blocked in any way as a protection.
#
# A connected webcam looks down on the platform to control position.
import datetime
import requests

import picamera

import serial

import time

import sys

ser = serial.Serial(sys.argv[1],9600)

camera = picamera.PiCamera()
#camera.resolution = (2592, 1944)
#camera.shutter_speed = camera.exposure_speed
#camera.exposure_mode = 'off'
#g = camera.awb_gains
#camera.awb_mode = 'off'
#camera.awb_gains = g

print("testing")

counter = 0

def turn_and_capture(counter):
    r = requests.get('http://digitalfoodone.appspot.com/macrocontrolrequest')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    data = r.json()
    print(data)
    upload_url = data['upload_url']

    camera.capture('my_img.jpg')

    files = {'file':open('my_img.jpg','rb')}
    resp = requests.post(upload_url,files=files)
    print(resp)

turn_and_capture(counter)
