# -*- coding: UTF-8 -*-
# Xinyi He 300072163

import cv2
import numpy as np
# partA
img = cv2.imread('circles_target.jpg',1)
img = cv2.medianBlur(img,5)
result = img.copy()
cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,20,param1=100,param2=30,minRadius=35,maxRadius=80)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(result,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(result,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('img', img)
cv2.imshow('result',result)

#PartB
img = cv2.imread('lines_target.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (3, 3), 0)
gray = cv2.medianBlur(gray,5)

edges = cv2.Canny(gray, 200, 400)
cv2.imshow("edges", edges)

lines = cv2.HoughLines(edges, 0.75, np.pi / 73, 45)
print("Len of lines:", len(lines))

for line in range(len(lines)):
    rho, theta = lines[line][0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    if x1 == x2: #x=x1
        k1 = 999
        b1 = 999
    elif y1 == y2:
        k12 = 0
        b12 = y1
    else:
        k1 = (y1-y2)/(x1-x2)
        b1 = (x1*y2-x2*y1)/(x1-x2)
    print('1'+' '+str(k1)+' '+str(b1))
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
    for line2 in range(line,len(lines)):
        rho2, theta2 = lines[line2][0]
        a2 = np.cos(theta2)
        b2 = np.sin(theta2)
        x02 = a2 * rho2
        y02 = b2 * rho2
        x12 = int(x02 + 1000 * (-b2))
        y12 = int(y02 + 1000 * (a2))
        x22 = int(x02 - 1000 * (-b2))
        y22 = int(y02 - 1000 * (a2))
        if x12 == x22: # x=x12
            k12 = 999
            b12 = 999
        elif y12 == y22:
            k12 = 0
            b12 = y12
        else:
            k12 = (y12 - y22) / (x12 - x22)
            b12 = (x12*y22-x22*y12)/(x12-x22)
        print('2' +' '+str(k12) + ' ' + str(b12))
        if (k1 != k12)&(k1 < 999)&(k12 < 999):
            x = (b12 - b1)/(k1 - k12)
            y = (k1*b12 - k12*b1)/(k1 - k12)
            print('3' + ' ' + str(x) + ' ' + str(y))
            cv2.circle(img,(int(x),int(y)),4,(0,0,255),-1)
        if (int(k1) == 0 and int(k12) >= 999):
            cv2.circle(img, (int(x02), int(b1)), 4, (0, 0, 255), -1)
        if (int(k12) == 0 and int(k1) >= 999):
            cv2.circle(img, (int(x0), int(b12)), 4, (0, 0, 255), -1)



cv2.imshow("lines_target", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
