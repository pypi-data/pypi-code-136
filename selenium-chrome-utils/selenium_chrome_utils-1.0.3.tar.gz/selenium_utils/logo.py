import os
from PIL import Image
import numpy as np
from selenium_utils.colors import Logger
from selenium_utils.image_bytes import get_image_bytes
log=Logger()
def my_logo():
    log.info("thank you for using")
def print_love():
    myData = "540667132"
    for char in myData.split():
        allChar = []
        for y in range(12, -12, -1):
            lst = []
            lst_con = ''
            for x in range(-30, 30):
                formula = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
                if formula <= 0:
                    lst_con += char[(x) % len(char)]
                else:
                    lst_con += ' '
            lst.append(lst_con)
            allChar += lst
        log.error('\n'.join(allChar))

def print_photo(photo_file='logo.ico', width=50, k=1.0, reverse=False, outfile=None):
    imageByte = get_image_bytes()[0]
    with open(photo_file, 'wb') as f:
        f.write(imageByte)
    """打印照片，默认120个字符宽度"""
    im = Image.open(photo_file).convert('L')  # 打开图片文件，转为灰度格式
    os.remove('logo.ico')
    height = int(k * width * im.size[1] / im.size[0])  # 打印图像高度，k为矫正系数，用于矫正不同终端环境像素宽高比
    arr = np.array(im.resize((width, height)))  # 转为NumPy数组
    if reverse:  # 反色处理
        arr = 255 - arr
    chs = np.array([' ', '.', '-', '+', '=', '*', '#', '@'])  # 灰度-字符映射表
    arr = chs[(arr / 32).astype(np.uint8)]  # 灰度转为对应字符
    if outfile:
        with open(outfile, 'w') as fp:
            for row in arr.tolist():
                fp.write(''.join(row))
                fp.write('\n')
    else:
        for i in range(6,arr.shape[0]-6):  # 逐像素打印
            for j in range(arr.shape[1]):
                print(arr[i, j], end=' ')
            print()
if __name__ == '__main__':
    print_photo()
