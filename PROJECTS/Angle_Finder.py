import math
import cv2
import numpy as np

points = []
#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('./Resources/protractor.jpg',3)
def draw(event, x,y, flags, params):

    if event==cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])
        cv2.circle(img, (x,y), 5, (255,0,0), -1)
        if (len(points)!=0) :
            cv2.arrowedLine(img, tuple(points[0]),(x,y), (255,0,0),3)
        cv2.imshow('image', img)
        print(points)
        if len(points)%3==0:
            degrees = angle()

            print(abs(degrees))


def angle():
    a = points[-2]
    b = points[-3]
    c = points[-1]

    m1 = slope(b,a)
    m2 = slope(b,c)
    angle = math.atan((m2-m1)/1+m1*m2)
    angle = round(math.degrees(angle))
    if angle<0:
        angle = 180+angle
    cv2.putText(img, str((angle)), (b[0]-40,b[1]+40), cv2.FONT_HERSHEY_DUPLEX, 2,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('image',img)
    return angle

def slope(p1,p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])

while True:
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', draw)
    if cv2.waitKey(1)&0xff==ord('r'):
        #img = np.zeros((512,512,3), np.uint8)
        img = cv2.imread('protractor.jpg', 3)
        points=[]
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', draw)
    if cv2.waitKey(1)&0xff==ord('q'):
        break
