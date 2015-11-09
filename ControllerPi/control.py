
import sys
import requests

import imaging
import analysis

import serial
import time

ser = serial.Serial(sys.argv[2], 9600)

session_name = sys.argv[1]
print('Sending photo to session: -'+session_name+'-')

def looping():
    req = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', params={'session_name':session_name})
    print(str(req.status_code))
    data = req.json()
    print(data['state'])

    def imagestuff():
        resp = imaging.capture(session_name,'capturing')
        print('Received http status code: '+str(resp.status_code))
        data = resp.json()
        print('Status: '+data['status'])
        analysis_resp = analysis.red_spot(session_name)
        print('Received http status code: '+str(analysis_resp.status_code))
        analysis_data = analysis_resp.json()
        print('Analysis status: '+analysis_data['status'])


    if data['state'] == 'rewind':
        ser.write(chr(1))
        ser.write(chr(1))
        ser.write(chr(1))
        ser.write(chr(1))
        ser.write(chr(1))
        ser.write(chr(1))
        imagestuff()
    if data['state'] == 'play_one':
        ser.write(chr(70))
        imagestuff()
    if data['state'] == 'play_two':
        print('waiting')


while True:
    looping()
    time.sleep(8)
