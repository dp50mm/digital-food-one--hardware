# Controls the rotating platform
#
# The servo rotates the platform through a friction wheel.
# This wheel can slip when it is blocked in any way as a protection.
#
# A connected webcam looks down on the platform to control position.
import datetime
import requests

import picamera

camera = picamera.PiCamera()



print("testing")

r = requests.get('http://digitalfoodone.appspot.com/controlrequest')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
data = r.json()
print(data)
upload_url = data['upload_url']

my_file = open('my_image.jpg','wb')
camera.capture(my_file)

print my_file
