import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

img1 = cv2.imread('./picture/riscv.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread('./picture/starfive_logo.jpg')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img3 = cv2.imread('./picture/sun2sea.jpg')
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

img4 = cv2.imread('./picture/Lena.png')
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)

titles = ['RISC-V', 'Starfive_Logo', 'Sun2Sea', 'Lena']

images = [img1, img2, img3, img4]

for i in range(4):
	plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])

out_img_name = "4to1.png_{}.png".format(time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time())))
img_path = './picture/{}'.format(out_img_name)
plt.savefig(img_path)
plt.show()

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

