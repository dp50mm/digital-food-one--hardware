import datetime
import requests
import json

from PIL import Image


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
    max_points = 500
    for y in range(10,height-10, 10):
        for x in range(10, width-10, 10):
            if(pixels[y][x][0] > (pixels[y][x][1]+pixels[y][x][2]/1.3)/1.1) and pixels[y][x][0] > 100:
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
            max_points -= 1
            if max_points < 1:
                break
        if max_points < 1:
            break
    print('Found -'+str(len(points))+'- red points!')
    if len(points) > 1
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
    data_resp = requests.post('http://digitalfoodone.appspot.com/post_analysis', headers=headers, data=json_dump)
    return data_resp
