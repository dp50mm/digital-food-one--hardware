import datetime
import requests

import picamera

import serial

import time

camera = picamera.PiCamera()
camera.resolution = (1900, 1200)
camera.awb_mode = 'cloudy'
camera.meter_mode = 'average'
#camera.awb_gains = (1.85,1.9)
time.sleep(1)

def capture(session_name, state):
    while True:
        try:
            r = requests.get('http://digitalfoodone.appspot.com/macrocontrolrequest')
            data = r.json()
            upload_url = data['upload_url']
            camera.capture('my_img.jpg')
            time.sleep(1)
            files = {'file':open('my_img.jpg','rb')}
            while True:
                print('Try image post request -')
                try:
                    print('Image post request successful!')
                    resp = requests.post(upload_url, files=files, data={'session_name':session_name,'state':state})
                    return resp.json()
                except requests.exceptions.Timeout:
                    print("image post: request timeout")
                except requests.exceptions.TooManyRedirects:
                    print('image post: too many redirects')
                except requests.exceptions.RequestException as e:
                    print('image post: request exception: ')
                    print e
                print('apparently not successful - trying again in 10 sec')
                time.sleep(10)
            break
        except requests.exceptions.Timeout:
            print('image blobstore url request: timeout')
        except requests.exceptions.TooManyRedirects:
            print('image blobstore url request: too many redirects')
        except requests.exceptions.RequestException as e:
            print('image blobstore url request: request exception:')
            print(e)
        print('apparently not successful - trying again in 10 sec')
        time.sleep(10)
