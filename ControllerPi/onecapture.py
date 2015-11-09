
import sys
import requests

import imaging
import analysis

import serial

ser = serial.Serial(sys.argv[1], 9600)

session_name = raw_input('Input session name: ')
print('Sending photo to session: -'+session_name+'-')

req = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', params={'session_name':session_name})
print(str(req.status_code))
data = req.json()
print(data['state'])
if data['state'] == 'rewind':
    ser.write(chr(1))
    ser.write(chr(1))
    ser.write(chr(1))
    resp = imaging.capture(session_name,'capturing')
    print('Received http status code: '+str(resp.status_code))
    data = resp.json()
    print('Status: '+data['status'])
    analysis.red_spot('rotationtest')
