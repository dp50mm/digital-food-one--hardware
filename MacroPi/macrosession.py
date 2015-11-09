import imaging

import requests

import time

print('starting macrosession')

session_name = raw_input('Input session name: ')
print('starting session: '+session_name)

counter = 0
def looping():
    req = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', params={'session_name':session_name})
    print(str(req.status_code))
    data = req.json()
    print(data['state'])
    if data['state'] == 'play_two':
        imaging.capture(session_name,'capturing')
    else:
        print('waiting...')

while True:
    looping()
    counter += 1
    print('counter: '+str(counter))
    time.sleep(10)
