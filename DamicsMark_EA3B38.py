import cv2
import numpy as np
draw = True
a,b = -1,-1
radius = 10
red = 255
green = 0
blue = 0

def draw_circle(event,x,y,flags,param):
    global a,b,draw,radius,red,green,blue
    if(event == cv2.EVENT_LBUTTONDOWN):
        draw = True
        a,b = x,y
    elif (event == cv2.EVENT_MOUSEMOVE):
        if draw == True:
            cv2.circle(img,(x,y),radius,(blue,green,red),-1)
    elif(event == cv2.EVENT_LBUTTONUP):
        draw = False
        #cv2.circle(img,(x,y),radius,(blue,green,red),-1)

img = np.ndarray((480,640,3), np.uint8)
img.fill(255)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if(k == 27 or k == ord('q')):
        break
    elif k == ord('s'):
        cv2.imwrite('DamicsMark_EA3B38.png', img)
    elif k == ord('t'):
        img.fill(255)
    elif k == ord('+'):
        radius += 5
        if radius > 100:
            radius = 100
    elif k == ord('-'):
        radius -= 5
        if radius < 5:
            radius = 5
    elif k == ord('r'):
        red = 255
        blue = 0
        green = 0
    elif k == ord('g'):
        red = 0
        blue = 0
        green = 255
    elif k == ord('b'):
        red = 0
        blue = 255
        green = 0
    elif k == ord('k'):
        red = 0
        blue = 0
        green = 0
    elif k == ord('w'):
        red = 255
        blue = 255
        green = 255

cv2.destroyAllWindows()