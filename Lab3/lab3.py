# Xinyi HE
# 300072163

import cv2

cap = cv2.VideoCapture('park.avi')
flag = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = cap.get(5)
w = cap.get(3)
l = cap.get(4)
print(fps,w,l)
print(cap.get(7))
out = cv2.VideoWriter('new.avi',fourcc, 30, (320,240),0)


def th(image1, image2):
  imgGL1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
  imgGL2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
  img = cv2.subtract(imgGL1, imgGL2)
  ret,thresh = cv2.threshold(img, 25, 255, cv2.THRESH_BINARY)
  return thresh


while flag < (cap.get(7) - 1):
  cap.set(cv2.CAP_PROP_POS_FRAMES, flag)
  ret1, img1 = cap.read()
  cap.set(cv2.CAP_PROP_POS_FRAMES, flag+1)
  ret2, img2 = cap.read()

  newimg = th(img1,img2)
  out.write(newimg)
  # cv2.imshow("newimg", newimg)
  flag = flag + 1




cap.release()
out.release()
cv2.destroyAllWindows()


