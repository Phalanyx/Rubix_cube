import cv2
from PIL import Image
import numpy as np
import time
colors = {'blue': [255,0,0], 'green': [0,255,0], 'red': [[0,100, 100],[1,255,255]],
          'yellow': [0,255,255], 'orange': [0,165,255], 'white': [255,255,255]}
def draw_box(frame, x, y):
    circle = cv2.circle(frame, (x,y), 15, colors['blue'], 5)
    square = cv2.rectangle(frame, (x-50, y-50), (x+50, y+50), colors['blue'], 10)
    return square

def color_mask(color):
    tmp = np.uint8([[color]])
    hsv_color = cv2.cvtColor(tmp, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([hsv_color[0][0][0] - 5, 100, 100])
    upper_bound = np.array([hsv_color[0][0][0] + 5, 255, 255])
    return lower_bound, upper_bound    


capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_red = np.array(colors['red'][0])
    high_red = np.array(colors['red'][1])
    mask = cv2.inRange(hsvImage, low_red, high_red)

    res = Image.fromarray(mask)
    bbox = res.getbbox()
    if bbox:
        print(bbox)
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0,255,0), 2)
        
    x = 1000
    y = 500 
    grid = []
    for nums in range(3):
        x = 900
        for num in range(3):
            cv2.imshow('frame', draw_box(frame, x,y))
            x+=100
        y+=100
    cv2.imshow('frame', frame)
 



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()