import datetime
import requests

import picamera

import serial

import time

camera = picamera.PiCamera()
camera.resolution = (1900, 1200)
camera.awb_mode = 'fluorescent'
camera.framerate = 0.5
# Wait for the automatic gain control to settle
time.sleep(2)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g


def capture(session_name, state):
    r = requests.get('http://digitalfoodone.appspot.com/macrocontrolrequest')
    data = r.json()
    upload_url = data['upload_url']

    camera.capture('my_img.jpg')
    time.sleep(1)
    files = {'file':open('my_img.jpg','rb')}
    resp = requests.post(upload_url, files=files, data={'session_name':session_name,'state':state})
    return resp
