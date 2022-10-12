from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改lang参数进行切换
# 参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。
ocr = PaddleOCR(use_angle_cls=True, lang="ch", page_num=2)  # need to run only once to download and load model into memory
# img_path = 'doc/imgs/11.jpg'
img_path = 'sar_2019.pdf'
result = ocr.ocr(img_path, cls=True)

# ocr = PaddleOCR(use_angle_cls=True)  # need to run only once to download and load model into memory
# img_path = 'doc/imgs_words/ch/word_1.jpg'
# result = ocr.ocr(img_path, det=False, cls=True)

# ocr = PaddleOCR()  # need to run only once to download and load model into memory
# img_path = 'doc/imgs/11.jpg'
# result = ocr.ocr(img_path, rec=False)

# ocr = PaddleOCR()  # need to run only once to download and load model into memory
# img_path = 'doc/imgs_words/ch/word_1.jpg'
# result = ocr.ocr(img_path, det=False)

# ocr = PaddleOCR(use_angle_cls=True)  # need to run only once to download and load model into memory
# img_path = 'doc/imgs_words/ch/word_1.jpg'
# result = ocr.ocr(img_path, det=False, rec=False, cls=True)

for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)
# 显示结果
# from PIL import Image
# result = result[0]
# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='doc/fonts/simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')

import fitz
from PIL import Image
import cv2
import numpy as np
imgs = []
with fitz.open(img_path) as pdf:
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]
        mat = fitz.Matrix(2, 2)
        pm = page.getPixmap(matrix=mat, alpha=False)
        # if width or height > 2000 pixels, don't enlarge the image
        if pm.width > 2000 or pm.height > 2000:
            pm = page.getPixmap(matrix=fitz.Matrix(1, 1), alpha=False)

        img = Image.frombytes("RGB", [pm.width, pm.height], pm.samples)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        imgs.append(img)
for idx in range(len(result)):
    res = result[idx]
    image = imgs[idx]
    boxes = [line[0] for line in res]
    txts = [line[1][0] for line in res]
    scores = [line[1][1] for line in res]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='doc/fonts/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save('result_page_{}.jpg'.format(idx))

# import pdb 
# pdb.set_trace()
# print()