import datetime
import requests

import picamera

import serial

import time



def capture(session_name, state):
    r = requests.get('http://digitalfoodone.appspot.com/controlrequest')
    data = r.json()
    upload_url = data['upload_url']
    camera = picamera.PiCamera()
    camera.resolution = (1900, 1200)
    camera.awb_mode = 'off'
    camera.awb_gains = (2.1,2.3)
    time.sleep(1)
    camera.capture('my_img.jpg')
    camera.close()
    time.sleep(1)
    files = {'file':open('my_img.jpg','rb')}
    resp = requests.post(upload_url, files=files, data={'session_name':session_name,'state':state})
    return resp
