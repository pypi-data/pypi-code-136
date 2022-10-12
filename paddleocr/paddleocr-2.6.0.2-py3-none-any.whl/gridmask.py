from PIL import Image, ImageEnhance, ImageOps
import numpy as np
import random
import six
import os
import cv2


class RawGridMask(object):
    def __init__(self, d1=32, d2=100, rotate=1, ratio=0.1, mode=0, prob=1., **kwargs):
        self.d1 = d1
        self.d2 = d2
        self.rotate = rotate
        self.ratio = ratio
        self.mode = mode
        # self.st_prob = prob
        self.prob = prob
        # self.last_prob = -1


    def __call__(self, img):
        if np.random.rand() > self.prob:
            return img
        _, h, w = img.shape
        hh = int(1.5 * h)
        ww = int(1.5 * w)
        d = np.random.randint(self.d1, self.d2)
        #d = self.d
        self.l = int(d * self.ratio + 0.5)
        mask = np.ones((hh, ww), np.float32)
        st_h = np.random.randint(d)
        st_w = np.random.randint(d)
        for i in range(-1, hh // d + 1):
            s = d * i + st_h
            t = s + self.l
            s = max(min(s, hh), 0)
            t = max(min(t, hh), 0)
            mask[s:t, :] *= 0
        for i in range(-1, ww // d + 1):
            s = d * i + st_w
            t = s + self.l
            s = max(min(s, ww), 0)
            t = max(min(t, ww), 0)
            mask[:, s:t] *= 0
        r = np.random.randint(self.rotate)
        mask = Image.fromarray(np.uint8(mask))
        mask = mask.rotate(r)
        mask = np.asarray(mask)
        mask = mask[(hh - h) // 2:(hh - h) // 2 + h, (ww - w) // 2:(ww - w) //
                    2 + w]

        if self.mode == 1:
            mask = 1 - mask

        mask = np.expand_dims(mask, axis=0)
        img = (img * mask).astype(img.dtype)

        return img


class RawGridMaskOCR(object):
    def __init__(self, r1=4, r2=1, ratio=0.25, mode=0, prob=1., **kwargs):
        self.r1 = r1
        self.r2 = r2
        self.ratio = ratio
        self.mode = mode
        self.prob = prob


    def __call__(self, img):
        if np.random.rand() > self.prob:
            return img
        _, h, w = img.shape
        d = np.random.randint(h // self.r1, h // self.r2)
        self.l = int(d * self.ratio + 0.5)
        mask = np.ones((h, w), np.float32)
        st = np.random.randint(d)
        for i in range(-1, w // d + 1, 2):
            sw = d * i + st
            tw = sw + self.l 
            sw = max(min(sw, w), 0)
            tw = max(min(tw, w), 0)
            j = np.random.randint(h // d)
            sh = d * j + st
            th = sh + self.l
            sh = max(min(sh, h), 0)
            th = max(min(th, h), 0)
            mask[sh:th, sw:tw] *= 0
        
        if self.mode == 1:
            mask = 1 - mask

        mask = np.expand_dims(mask, axis=0)
        img = (img * mask).astype(img.dtype)

        return img


data_dir = '/paddle/data/ch_26w/real_data'
label_file = '/paddle/data/ch_26w/real_data/train_list.txt'
save_img_dir = '/paddle/data/ch_26w/gridmask/images'
save_label_dir = '/paddle/data/ch_26w/gridmask/labels'
os.makedirs(save_img_dir, exist_ok=True)
os.makedirs(save_label_dir, exist_ok=True)

gridmask = RawGridMaskOCR()
with open(label_file, "r") as f:
    lines = f.readlines()
    length = len(lines)
    for idx, data_line in enumerate(lines):
        # origin image
        substr = data_line.strip("\n").split('\t')
        file_name = substr[0]
        label = substr[1]
        img_path = os.path.join(data_dir, file_name)
        img = cv2.imread(img_path)
        img_input = img.transpose((2, 0, 1)) # HWC2CHW
        # gridmask
        img_res = gridmask.__call__(img_input)
        img_res = img_res.transpose((1, 2, 0)) # CHW2HWC
        # save res
        save_img_path = os.path.join(save_img_dir, img_path.split('/')[-1])
        if not os.path.exists(save_img_path):
            cv2.imwrite(save_img_path, img_res)
            label_path = os.path.join(save_label_dir, 'gridmask.txt')
            with open(label_path, 'a+') as f:
                f.write(save_img_path.replace('/paddle/data/ch_26w/', '') + '\t' + label + '\n')
        if (idx + 1) % 10000 == 0:
            print('process num : ', idx + 1)
    print('finished!')
        # img_vis = np.vstack((img, img_res))
        # cv2.imwrite('test.jpg', img_vis)
        # if idx == 5:
        #     import pdb
        #     pdb.set_trace()
        #     print()