
import sys
import requests

import imaging
import analysis

session_name = raw_input('Input session name: ')
print('Sending photo to session: -'+session_name+'-')

req = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus')
print(str(req.status_code))
data = req.json()
print(data)


# resp = imaging.capture(session_name,'capturing')
# print('Received http status code: '+str(resp.status_code))
# data = resp.json()
# print('Status: '+data['status'])
#analysis.red_spot('rotationtest')
