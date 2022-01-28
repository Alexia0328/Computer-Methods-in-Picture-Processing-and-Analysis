import cv2
import numpy as np


def nothing(x):
    pass

# use track bar to perfectly define (1/2)
# the lower and upper values for HSV color space(2/2)

window = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('Processed Hue')
cv2.createTrackbar("Hue",'Processed Hue',0,180,nothing)

while True:
    frame = cv2.imread('Picture3.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_v = cv2.getTrackbarPos("Hue", "Processed Hue")

    l_g = np.array([h_v, 0, 0])  # lower green value
    u_g = np.array([h_v, 255, 255])

    mask = cv2.inRange(hsv, l_g, u_g)

    res = cv2.bitwise_and(frame, frame, mask=mask)  # src1,src2
    H_v = cv2.getTrackbarPos("Hue", "Processed Hue")
    print(H_v)
    cv2.imshow("frame", frame)
    cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    # cv2.imshow("Processed Hue", res)
    # rgb = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
    cv2.imshow("Processed Hue", res)
    key = cv2.waitKey(1)
    if key == 27:  # Esc
        break

cv2.destroyAllWindows()
