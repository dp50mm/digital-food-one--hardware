
import sys
import requests

import imaging
import analysis

import serial
import time

ser = serial.Serial(sys.argv[2], 9600)

session_name = sys.argv[1]
print('Sending photo to session: -'+session_name+'-')
session_status_request_error_counter = 0

def looping():
    global session_status_request_error_counter
    while True:
        try:
            req = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', params={'session_name':session_name})
            print('session status request successful')
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
                if analysis_resp.status_code == 200:
                    analysis_data = analysis_resp.json()
                    print('Analysis status: '+analysis_data['status'])
                else:
                    print('500 error on analysis post')


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
            break
        except requests.exceptions.Timeout:
            print("session status request: request timeout")
        except requests.exceptions.TooManyRedirects:
            print('session status request: too many redirects')
        except requests.exceptions.RequestException as e:
            print('session status request: request exception:')
            print e
        print('apparently not successful - trying again in 10 sec')
        session_status_request_error_counter += 1
        print('number of status request errors: '+str(session_status_request_error_counter))
        time.sleep(10)


while True:
    looping()
    time.sleep(8)
