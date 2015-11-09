
import sys

print('starting rotation test session')

session_name = raw_input('Input session name: ')
print('starting session: '+session_name)

import analysis
import imaging
import serial

counter = 0

ser = serial.Serial(sys.argv[1],9600)

def turn_and_capture(counter):
    imaging.capture('rotationtest')
    analysis.red_spot('rotationtest')
    ser.write(chr(5))
    counter = counter+1
    if(counter < 100):
        turn_and_capture(counter)

turn_and_capture(counter)
