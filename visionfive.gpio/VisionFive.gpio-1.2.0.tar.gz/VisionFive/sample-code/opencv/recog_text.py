
import cv2
import pytesseract
from PIL import Image
import time

#img1 = cv2.imread("text_image.png")
#img2 = cv2.imread("text_chinese_image.jpg")
#tessdata_dir_config = r'--tessdata-dir "/usr/local/share/tessdata"'
t1 = time.time()
#text = pytesseract.image_to_string(Image.open("text_image.png"))
xx = cv2.imread('./picture/text_image.png')
text = pytesseract.image_to_string(xx)

t2 = time.time()
print("The resolve time: {}".format((t2-t1)))
text1 = pytesseract.image_to_string(Image.open("./picture/text_chinese_image.jpg"), lang='chi_sim')
print(text)
print(text1)




