# Controls the rotating platform
#
# The servo rotates the platform through a friction wheel.
# This wheel can slip when it is blocked in any way as a protection.
#
# A connected webcam looks down on the platform to control position.
import datetime
import requests

print("testing")

r = requests.get('controlrequest')
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()
