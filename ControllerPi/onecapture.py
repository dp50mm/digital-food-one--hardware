# Controls the rotating platform
#
# The servo rotates the platform through a friction wheel.
# This wheel can slip when it is blocked in any way as a protection.
#
# A connected webcam looks down on the platform to control position.

import sys
import requests

import imaging
import analysis

print('capturing a single image')

session_name = raw_input('Input session name: ')
print('starting session: '+session_name)

print('checking session state')
r = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', data={'session_name':session_name})
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
data = r.json
print(data)

imaging.capture('rotationtest','capturing')
analysis.red_spot('rotationtest')
