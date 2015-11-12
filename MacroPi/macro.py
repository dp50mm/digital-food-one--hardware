import imaging

import requests

import time

print('starting macrosession')

session_name = raw_input('Input session name: ')
print('starting session: '+session_name)

counter = 0

session_status_request_error_counter = 0

def looping():
    global session_status_request_error_counter
    while True:
        try:
            req = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', params={'session_name':session_name})
            print(str(req.status_code))
            data = req.json()
            print(data['state'])
            if data['state'] == 'play_two':
                respons = imaging.capture(session_name,'capturing')
                print('Image capture response: '+respons['status'])
            else:
                print('waiting...')
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
        print('number of status request errors: '+session_status_request_error_counter)
        time.sleep(10)

while True:
    looping()
    counter += 1
    print('counter: '+str(counter))
    time.sleep(10)
