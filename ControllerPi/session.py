import sys

import requests

import schedule
import time

print('session name: '+sys.argv[1])

def job():
    print('do the work')
    r = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', params={'session_name':sys.argv[1]})
    data = r.json()
    message = data['message']

schedule.every(15).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
