#Xinyi HE 300072163
#External source code1: https://blog.csdn.net/xiao__run/article/details/80572523
#External source code2: https://github.com/fletchto99/CSI4133/blob/master/project/project.py

from collections import  deque
import numpy as np
import cv2


cap = cv2.VideoCapture('video1.avi')
# cap = cv2.VideoCapture('video2.avi')
# cap = cv2.VideoCapture('video3.avi')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = cap.get(5)
w = cap.get(3)
l = cap.get(4)
print(fps,w,l)

out = cv2.VideoWriter('output1.avi',fourcc, 30, (480,360))
# out = cv2.VideoWriter('output2.avi',fourcc, 30, (480,360))
# out = cv2.VideoWriter('output3.avi',fourcc, 30, (480,360))


colors = [
	[(40, 80, 0), (65, 255, 255), 'Green'], # Green
	[(0, 100, 140), (25, 255, 255), 'Yellow'], # Yellow
	[(80, 5, 5), (126, 255, 255), 'Blue'], # Blue
	[(0, 170, 65), (25, 255, 255), 'Red'] # Red
]


mybuffer = 2048
ptsY = deque(maxlen=mybuffer)
ptsG = deque(maxlen=mybuffer)
ptsB = deque(maxlen=mybuffer)
ptsB1 = deque(maxlen=mybuffer)
ptsB2 = deque(maxlen=mybuffer)
ptsR = deque(maxlen=mybuffer)
ptsR1 = deque(maxlen=mybuffer)
ptsR2 = deque(maxlen=mybuffer)

def draw(pts,linecolor):
    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue
        thickness = 2
        cv2.line(frame, pts[i - 1], pts[i], linecolor, thickness)

def points(c,pts):
    (_, radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    # for video 1: radius >10
    if radius > 10:
        pts.appendleft(center)
    # for video 2 and 3: pts.appendleft(center) directly
    # pts.appendleft(center)
    return pts

while(cap.isOpened()):

    ret, frame = cap.read()
    cv2.imshow('image', frame)
    k = cv2.waitKey(1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color in colors:
        mask = cv2.inRange(hsv, color[0], color[1])
        mask = cv2.erode(mask, None, iterations=4)
        mask = cv2.dilate(mask, None, iterations=4)
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        for contour in contours:
            if color == colors[0]:
                points(contour,ptsG)
                draw(ptsG, (0, 255, 0))
            if color == colors[1]:
                points(contour,ptsY)
                draw(ptsY, (0, 255, 255))
            if color == colors[2]:
                points(contour, ptsB)
                (_,b) = ptsB[0]
                if b > 150:
                    points(contour, ptsB1)
                    draw(ptsB1, (255, 0, 0))
                else:
                    points(contour, ptsB2)
                    draw(ptsB2, (255, 255, 0))
            if color == colors[3]:
                points(contour, ptsR)
                (a, _) = ptsR[0]
                if a > 200:
                    points(contour, ptsR1)
                    draw(ptsR1, (255, 0, 255))
                else:
                    points(contour, ptsR2)
                    draw(ptsR2, (0, 0, 255))

            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 255, 0), 2)
            epsilon = 0.03 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            corners = len(approx)
            shape_type = ""
            if corners < 6:
                shape_type = "rectangle"
            if corners >= 6:
                shape_type = "circle"
            cv2.putText(frame, color[2] + str(' ' + shape_type), (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0),
                        2)

    out.write(frame)
    cv2.imshow('Frame', frame)


cap.release()
cv2.destroyAllWindows()

