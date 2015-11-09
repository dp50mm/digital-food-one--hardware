import imaging

print('starting macrosession')

session_name = raw_input('Input session name: ')
print('starting session: '+session_name)

counter = 0
def looping():
    req = requests.get('http://digitalfoodone.appspot.com/controllersessionstatus', params={'session_name':session_name})
    print(str(req.status_code))
    data = req.json()
    print(data['state'])
    counter += 1
    if data['state'] == 'play_two':
        imaging.capture(session_name,'capturing')
    else:
        print('waiting...'+str(counter))
