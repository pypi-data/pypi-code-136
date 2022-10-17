import cv2

#img = cv2.imread("starfive_logo.jpg")
img = cv2.imread("./picture/starfive_logo.jpg")

cv2.imshow("demo", img)

k = cv2.waitKey(0)
if k == 27: 
    cv2.destroyAllWindows()

