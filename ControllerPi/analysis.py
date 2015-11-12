import datetime
import requests
import json

from PIL import Image

import time

analysis_post_error_counter = 0

def red_spot(session_name):
    im = Image.open('my_img.jpg')
    pixels = list(im.getdata())
    width, height = im.size
    print('image width: '+str(width))
    print('image height: '+str(height))
    pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
    points = []
    average_x = 0
    average_y = 0
    for y in range(10,height-10, 8):
        for x in range(10, width-10, 8):
            if (pixels[y][x][0] > 180) and (pixels[y][x][1] < 110) and (pixels[y][x][2] > 120):
                print('red pixel!')
                print(pixels[y][x])
                average_x += x
                average_y += y
                points.append({
                    'point_type':'red point',
                    'result':'found',
                    'red':pixels[y][x][0],
                    'green':pixels[y][x][1],
                    'blue':pixels[y][x][2],
                    'x':x,
                    'y':y
                })
    print('Found -'+str(len(points))+'- red points!')
    if len(points) > 1:
        average_x = average_x/len(points)
        average_y = average_y/len(points)



    points.append({
        'point_type':'average',
        'result':'calculated',
        'x':average_x,
        'y':average_y
    })

    print('average x: '+str(average_x)+' average y: '+str(average_y))
    json_dump = json.dumps({
        'points':points,
        'session_name':session_name
    })
    print('dump length: '+str(len(json_dump)))
    headers = {'Content-Type':'application/json'}

    analysis_post_successful = False
    while True:
        try:
            data_resp = requests.post('http://digitalfoodone.appspot.com/post_analysis', headers=headers, data=json_dump)
            return data_resp
        except requests.exceptions.Timeout:
            print("analysis post: request timeout")
        except requests.exceptions.TooManyRedirects:
            print('analysis post: too many redirects')
        except requests.exceptions.RequestException as e:
            print('analysis post: request exception:')
            print e
        print('analysis post failed - trying again in 10 sec')
        analysis_post_error_counter += 1
        print('analysis post error count: '+analysis_post_error_counter)
        time.sleep(10)
