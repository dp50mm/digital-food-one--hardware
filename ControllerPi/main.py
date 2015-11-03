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

ser = serial.Serial('/dev/tty.usbserial',9600)

camera = picamera.PiCamera()



print("testing")

def turn_and_capture():
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
    resp = requests.post(upload_url,files=files)
    print(resp)
    time.sleep(30)
    ser.write('5')
    turn_and_capture()

turn_and_capture()
