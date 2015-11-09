
print('starting macrosession')

session_name = raw_input('Input session name: ')
print('starting session: '+session_name)


def capture(counter):
    imaging.capture(session_name,'capturing')
