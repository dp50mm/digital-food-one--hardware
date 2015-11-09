import sys

import requests

import time

print('starting controllersession')
session_name = raw_input('Input session name: ')
print('starting session: '+session_name)


def job():
    print('::job::')
    r = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', data={'session_name':session_name})
    data = r.json()
    if data['state'] == 'rewind':
        print('rewind!')
    else if data['state'] == 'play_control':
        print('play control!')
    else if data['state'] == 'play_macro':
        print('macros turn')
    else:
        print('unkown state')

while True:
    job()
    time.sleep(2)
