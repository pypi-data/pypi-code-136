
import cv2
import numpy as np
import time

img1 = cv2.imread("./picture/horizontal_fuzzy_text_image.png")

norm_img = np.zeros((img1.shape[0], img1.shape[1]))

img_norm = cv2.normalize(img1, norm_img, 0, 255, cv2.NORM_MINMAX)
img_gray = cv2.cvtColor(img_norm, cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(img_gray,5)
img_lamp = cv2.Laplacian(img_blur, cv2.CV_8U, ksize=5)
img_equ  = cv2.equalizeHist(img_lamp)

cv2.imshow("original", img1)
cv2.imshow("img_improved", img_equ)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

