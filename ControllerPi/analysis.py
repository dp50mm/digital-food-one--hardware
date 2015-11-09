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
    counter = 50
    for y in range(10,height-10, 4):
        for x in range(10, width-10, 4):
            if(pixels[y][x][0] > (pixels[y][x][1]+pixels[y][x][2])/0.7) and pixels[y][x][0] > 100:
                print('red found at x:'+str(x)+' y:'+str(y))
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
                counter -= 1
            if(counter == 0):
                break
        if(counter == 0):
            break
    print(len(points))
    average_x = average_x/len(points)
    average_y = average_y/len(points)


    print('average x: '+str(average_x))
    print('average y: '+str(average_y))
    json_dump = json.dumps({
        'points':points,
        'session_name':session_name
    })
    print('dump length: '+str(len(json_dump)))
    headers = {'Content-Type':'application/json'}
    data_resp = requests.post('http://digitalfoodone.appspot.com/post_analysis', headers=headers, data=json_dump)
