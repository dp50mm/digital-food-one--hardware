import datetime
import requests

import picamera

import serial

import time

camera = picamera.PiCamera()
camera.resolution = (1900, 1200)
camera.awb_mode = 'fluorescent'

def capture(session_name, state):
    r = requests.get('http://digitalfoodone.appspot.com/controlrequest')
    print('turn and capture function start')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    data = r.json()
    print(data)
    upload_url = data['upload_url']

    camera.capture('my_img.jpg')
    print('image captured')
    time.sleep(1)
    files = {'file':open('my_img.jpg','rb')}
    resp = requests.post(upload_url, files=files, data={'session_name':session_name,'state':state})
    headers = {'Content-Type':'application/json'}
    print(resp)
    return resp.json()
