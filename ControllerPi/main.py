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
camera.resolution = (1900, 1200)
camera.awb_mode = 'fluorescent'


print("testing")

counter = 0

def turn_and_capture(counter):
    r = requests.get('http://digitalfoodone.appspot.com/controlrequest')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    data = r.json()
    print(data)
    upload_url = data['upload_url']

    camera.capture('my_img.jpg')

    files = {'file':open('my_img.jpg','rb')}
    data = {
        'green points':'abc',
    }
    resp = requests.post(upload_url,files=files, data=data)
    print(resp)
    ser.write(chr(5))
    counter = counter+1
    if(counter < 100):
        turn_and_capture(counter)

turn_and_capture(counter)
