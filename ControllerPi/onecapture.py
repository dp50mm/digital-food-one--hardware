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

import json

ser = serial.Serial(sys.argv[1],9600)

camera = picamera.PiCamera()
camera.resolution = (1900, 1200)
camera.awb_mode = 'fluorescent'

print("testing")

counter = 0

def turn_and_capture(counter):
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

    files = {'file':open('my_img.jpg','rb')}

    im = Image.open('my_img.jpg')
    pixels = list(im.getdata())
    width, height = im.size
    print('image width: '+str(width))
    print('image height: '+str(height))
    pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
    red_points = []
    average_x = 0
    average_y = 0
    for y in range(10,height-10, 4):
        for x in range(10, width-10, 4):
            if(pixels[y][x][0] > (pixels[y][x][1]+pixels[y][x][2])/0.7) and pixels[y][x][0] > 100:
                print('red found at x:'+str(x)+' y:'+str(y))
                print(pixels[y][x])
                average_x += x
                average_y += y
                red_points.append({
                    'x':x,
                    'y':y
                })
    print(len(red_points))
    data = {
        'analysis_points': red_points
    }
    average_x = average_x/len(red_points)
    average_y = average_y/len(red_points)
    print('average x: '+str(average_x))
    print('average y: '+str(average_y))
    headers = {'Content-Type':'application/json'}
    resp = requests.post(upload_url, headers=headers, files=files, data=json.dumps(data))
    print(resp)

turn_and_capture(counter)
