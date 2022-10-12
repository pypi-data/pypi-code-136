from PIL import Image, ImageEnhance, ImageOps
import numpy as np
import random
import six
import os
import cv2


class RawRandEraseOCR(object):
    def __init__(self, r1=8, r2=2, ratio=0.25, mode=0, prob=1., **kwargs):
        self.r1 = r1
        self.r2 = r2
        self.ratio = ratio
        self.mode = mode
        self.prob = prob


    def __call__(self, img):
        if np.random.rand() > self.prob:
            return img
        _, h, w = img.shape
        mask_h = np.random.randint(h // 8, h // 4)
        mask_w = np.random.randint(w // self.r1, w // self.r2)
       
        mask = np.ones((h, w), np.float32)
        sw = np.random.randint(0, w - mask_w)
        sh = np.random.randint(0, h - mask_h)
        tw = sw + mask_w
        th = sh + mask_h
        mask[sh:th, sw:tw] *= 0
        
        if self.mode == 1:
            mask = 1 - mask

        mask = np.expand_dims(mask, axis=0)
        img = (img * mask).astype(img.dtype)

        return img


data_dir = '/paddle/data/ch_26w/'
label_file = '/paddle/data/ch_26w/valid_label/26w_train_list.txt'
save_img_dir = '/paddle/data/ch_26w/randerase_v2/images'
save_label_dir = '/paddle/data/ch_26w/randerase_v2/labels'
os.makedirs(save_img_dir, exist_ok=True)
os.makedirs(save_label_dir, exist_ok=True)

randerase = RawRandEraseOCR()
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
        # randerase
        img_res = randerase.__call__(img_input)
        img_res = img_res.transpose((1, 2, 0)) # CHW2HWC
        # save res
        save_img_path = os.path.join(save_img_dir, img_path.split('/')[-1])
        if not os.path.exists(save_img_path):
            cv2.imwrite(save_img_path, img_res)
            label_path = os.path.join(save_label_dir, 'randerase_v2.txt')
            with open(label_path, 'a+') as f:
                f.write(save_img_path.replace('/paddle/data/ch_26w/', '') + '\t' + label + '\n')
            # if idx == 10:
            #     break
        if (idx + 1) % 10000 == 0:
            print('process num : ', idx + 1)
    print('finished!')
        # img_vis = np.vstack((img, img_res))
        # cv2.imwrite('test.jpg', img_vis)
        # if idx == 5:
        #     import pdb
        #     pdb.set_trace()
        #     print()