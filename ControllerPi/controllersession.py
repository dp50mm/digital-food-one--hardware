import sys

import requests

import time

print('starting controllersession')
session_name = raw_input('Input session name: ')
print('starting session: '+session_name)


def job():
    print('::job::')
    r = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', params={'session_name':session_name})
    data = r.json()
    state = data['state']
    action = data['action']
    print(state)
    print(action)



abc = True
my_counter = 0
while abc:
    job()
    time.sleep(2)
    my_counter += 1
    if my_counter > 5:
        abc = False
