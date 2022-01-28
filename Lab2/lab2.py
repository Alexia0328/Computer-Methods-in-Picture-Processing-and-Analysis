import cv2

# video1: Load two frames from the same video.

# Park
# img1RGB = cv2.imread("park466.bmp",1)
# img2RGB = cv2.imread("park467.bmp",1)
# img1GL = cv2.imread("park466.bmp",0)
# img2GL = cv2.imread("park467.bmp",0)

img1RGB = cv2.imread("Img02_0076.bmp",1)
img2RGB = cv2.imread("Img02_0077.bmp",1)
img1GL = cv2.imread("Img02_0076.bmp",0)
img2GL = cv2.imread("Img02_0077.bmp",0)

cv2.imshow("img1RGB", img1RGB)
cv2.imshow("img2RGB", img2RGB)
cv2.imshow("img1GL", img1GL)
cv2.imshow("img2GL", img2GL)

# Calculate the pixel intensity difference
car = cv2.subtract(img1GL, img2GL)

# perform thresholding on the difference image to get areas of movement in binary format

# Trackbar
def onChange(a):
    threshold = cv2.getTrackbarPos("threshold", "image")
    ret, threshCar = cv2.threshold(car, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow("image", threshCar)
    print(threshold)

cv2.namedWindow("image")
cv2.imshow("image", car)

cv2.createTrackbar('threshold', 'image', 0, 255, onChange)


cv2.waitKey(0)
cv2.destroyAllWindows()
