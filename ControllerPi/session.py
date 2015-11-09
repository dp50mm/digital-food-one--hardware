import sys

import requests

import time

print('session name: '+sys.argv[1])

def job():
    print('do the work')
    r = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', params={'session_name':sys.argv[1]})
    data = r.json()
    state = data['state']
    action = data['action']
    print(state)
    print(action)

abc = True
while abc:
    job()
    time.sleep(100)
    job()
    time.sleep(100)
    abc = False
