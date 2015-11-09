
import sys
import requests

import imaging
import analysis

session_name = raw_input('Input session name: ')
print('starting session: '+session_name)

# r = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', data={'session_name':session_name})
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r)

resp = imaging.capture(session_name,'capturing')
print(resp.status_code)
data = resp.json()
print(data['status'])
#analysis.red_spot('rotationtest')
