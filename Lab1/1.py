import cv2
import numpy as np

# part A

# cv2.IMREAD_COLOR / 1
img1 = cv2.imread("field.jpg",1)
cv2.imshow("field1", img1)

# cv2.waitKey(0)
# cv2.waitKey(8000)
cv2.waitKey(8)
cv2.destroyAllWindows()

# cv2.IMREAD_GRAYSCALE/0
img2 = cv2.imread("field.jpg",0)
cv2.imshow("field2", img2)

# cv2.waitKey(0)
# cv2.waitKey(8000)
cv2.waitKey(8)
cv2.destroyAllWindows()

# cv2.IMREAD_UNCHANGED/-1
img3 = cv2.imread("field.jpg",-1)
cv2.imshow("field3", img3)

# cv2.waitKey(0)
# cv2.waitKey(8000)
cv2.waitKey(8)
cv2.destroyAllWindows()


# Part B

# Down-sample
imgdown = cv2.pyrDown(img1)
cv2.imshow('field4', imgdown)
cv2.waitKey(100)
cv2.destroyAllWindows()
# Up-sample
imgup = cv2.pyrUp(imgdown)
cv2.imshow('field5', imgup)
cv2.waitKey(100)
cv2.destroyAllWindows()

# Part C
img = cv2.imread("field.jpg")
height, width = img.shape[0], img.shape[1]
new_img = np.zeros((height, width, 3), np.uint8)
# 32
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 8:
                gray = 0
            elif img[i, j][k] < 16:
                gray = 8
            elif img[i, j][k] < 24:
                gray = 16
            elif img[i, j][k] < 32:
                gray = 24
            elif img[i, j][k] < 40:
                gray = 32
            elif img[i, j][k] < 48:
                gray = 40
            elif img[i, j][k] < 56:
                gray = 48
            elif img[i, j][k] < 64:
                gray = 56
            elif img[i, j][k] < 72:
                gray = 64
            elif img[i, j][k] < 80:
                gray = 72
            elif img[i, j][k] < 88:
                gray = 80
            elif img[i, j][k] < 96:
                gray = 88
            elif img[i, j][k] < 104:
                gray = 96
            elif img[i, j][k] < 112:
                gray = 104
            elif img[i, j][k] < 120:
                gray = 112
            elif img[i, j][k] < 128:
                gray = 120
            elif img[i, j][k] < 136:
                gray = 128
            elif img[i, j][k] < 144:
                gray = 136
            elif img[i, j][k] < 152:
                gray = 144
            elif img[i, j][k] < 160:
                gray = 152
            elif img[i, j][k] < 168:
                gray = 160
            elif img[i, j][k] < 176:
                gray = 168
            elif img[i, j][k] < 184:
                gray = 176
            elif img[i, j][k] < 192:
                gray = 184
            elif img[i, j][k] < 200:
                gray = 192
            elif img[i, j][k] < 208:
                gray = 200
            elif img[i, j][k] < 216:
                gray = 208
            elif img[i, j][k] < 224:
                gray = 216
            elif img[i, j][k] < 232:
                gray = 224
            elif img[i, j][k] < 240:
                gray = 232
            elif img[i, j][k] < 248:
                gray = 240
            else:
                gray = 248
            new_img[i, j][k] = np.uint8(gray)

cv2.imshow('filed6', img)


cv2.imshow('newFiled', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




