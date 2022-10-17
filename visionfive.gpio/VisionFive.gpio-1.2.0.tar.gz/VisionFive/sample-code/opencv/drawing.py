import cv2
import numpy as np
import time

#create black figure, pixel(256,256), 3 means RGB
img1 = np.zeros((256, 256, 3), np.uint8)
img2 = np.zeros((256, 256, 3), np.uint8)
img3 = np.zeros((256, 256, 3), np.uint8)
img4 = np.zeros((256, 256, 3), np.uint8)
img5 = np.zeros((256, 256, 3), np.uint8)
img6 = np.zeros((256, 256, 3), np.uint8)

#drawing line, color(B, G, R)
cv2.line(img1, (0,0), (255,255), (255, 0, 0), 5)

#drawing rectangle
cv2.rectangle(img2, (100,20), (150,250), (0, 0, 255), 2)

#drawing circle
cv2.circle(img3, (100, 100), 50, (0,255,0), 4)

#drawing ellipse
cv2.ellipse(img4,(120, 100), (100, 50), 20, 0, 360, (255, 0, 255), 2)

#drawing text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img5, 'RISC-V', (50, 80), font, 1.5, (180, 105, 255), 2)
cv2.putText(img5, 'processor', (30, 140), font, 1.5, (180, 105, 255), 2)
cv2.putText(img5, 'VisionFive', (30, 200), font, 1.5, (180, 105, 255), 2)

#drawing solid circle
cv2.circle(img6, (100, 100), 50, (0, 0 ,255), -1)

##display figure
merpic1 = np.hstack((img1, img2, img3))
merpic2 = np.hstack((img4, img5, img6))
merpic = np.vstack((merpic1, merpic2))
cv2.imshow("all", merpic)

cv2.imshow("line", img1)
cv2.imshow("rectangle", img2)
cv2.imshow("circle", img3)
cv2.imshow("ellipse", img4)
cv2.imshow("text", img5)
cv2.imshow("solid cycle", img6)

out_img_name = "Shapes_{}.png".format(time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time())))
img_path = "./picture/{}".format(out_img_name)
cv2.imwrite(img_path, merpic)

##wait for displaying
cv2.waitKey(0)
cv2.destroyAllWindows()
