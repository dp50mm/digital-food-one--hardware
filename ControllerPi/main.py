# Controls the rotating platform
#
# The servo rotates the platform through a friction wheel.
# This wheel can slip when it is blocked in any way as a protection.
#
# A connected webcam looks down on the platform to control position.
import datetime
import requests

print("testing")

r = requests.get('http://digitalfoodone.appspot.com/controlrequest')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
data = r.json()
print(r.json())
print(data)
