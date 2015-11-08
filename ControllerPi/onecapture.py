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

from PIL import Image

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

    im = Image.open('my_img.jpg')
    pixels = list(im.getdata())
    width, height = im.size
    print('image width: '+str(width))
    print('image height: '+str(height))
    pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
    red_points = []
    for y in range(10,height-10, 2):
        for x in range(10, width-10, 2):
            if(pixels[y][x][0] > (pixels[y][x][1]+pixels[y][x][2])/0.7) and pixels[y][x][0] > 100:
                print('red found at x:'+str(x)+' y:'+str(y))
                print(pixels[y][x])
                red_points.append({
                    'x':x,
                    'y':y
                })

    data = {
        'analysis_data': {
            'red points':'red_points',
            'average_x':10,
            'average_y':110,
        }
    }
    resp = requests.post(upload_url,files=files, data=data)
    print(resp)

turn_and_capture(counter)
