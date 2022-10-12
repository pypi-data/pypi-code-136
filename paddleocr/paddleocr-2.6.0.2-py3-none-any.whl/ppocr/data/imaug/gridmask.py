# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This code is based on https://github.com/akuxcw/GridMask
# reference: https://arxiv.org/abs/2001.04086.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from PIL import Image, ImageEnhance, ImageOps
import numpy as np
import random
import six
import os
import cv2


# curr
CURR_EPOCH = 0
# epoch for the prob to be the upper limit
NUM_EPOCHS = 240


class RawGridMask(object):
    def __init__(self, d1=8, d2=32, rotate=1, ratio=0.5, mode=0, prob=1., **kwargs):
        self.d1 = d1
        self.d2 = d2
        self.rotate = rotate
        self.ratio = ratio
        self.mode = mode
        # self.st_prob = prob
        self.prob = prob
        # self.last_prob = -1

    # def set_prob(self):
    #     global CURR_EPOCH
    #     global NUM_EPOCHS
    #     self.prob = self.st_prob * min(1, 1.0 * CURR_EPOCH / NUM_EPOCHS)

    def __call__(self, img):
        # self.set_prob()
        # if abs(self.last_prob - self.prob) > 1e-10:
        #     global CURR_EPOCH
        #     global NUM_EPOCHS
        #     print(
        #         "self.prob is updated, self.prob={}, CURR_EPOCH: {}, NUM_EPOCHS: {}".
        #         format(self.prob, CURR_EPOCH, NUM_EPOCHS))
        #     self.last_prob = self.prob
        # print("CURR_EPOCH: {}, NUM_EPOCHS: {}, self.prob is set as: {}".format(CURR_EPOCH, NUM_EPOCHS, self.prob) )
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


class GridMask(RawGridMask):
    """ GridMask wrapper to auto fit different img types """

    def __init__(self, prob=0.25, *args, **kwargs):
        self.prob = prob
        if six.PY2:
            super(GridMask, self).__init__(prob=prob, *args, **kwargs)
        else:
            super().__init__(prob=prob, *args, **kwargs)
        print('using GridMask')
        self.save_img = True
        if self.save_img:
            self.save_img_dir = '/paddle/data/ch_26w/gridmask/images'
            self.save_label_dir = '/paddle/data/ch_26w/gridmask/labels'
            os.makedirs(self.save_img_dir, exist_ok=True)
            os.makedirs(self.save_label_dir, exist_ok=True)

    def __call__(self, data):
        if np.random.rand() > self.prob:
            return data
        img = data['image']
        # if not isinstance(img, Image.Image):
        #     img = np.ascontiguousarray(img)
        #     img = Image.fromarray(img)
        img = img.transpose((2, 0, 1)) # HWC2CHW
        if six.PY2:
            img = super(RandomErasing, self).__call__(img)
        else:
            img = super().__call__(img)
        img = img.transpose((1, 2, 0)) # CHW2HWC
        data['image'] = img
        if self.save_img:
            img_path = os.path.join(self.save_img_dir, data['img_path'].split('/')[-1])
            if not os.path.exists(img_path):
                cv2.imwrite(img_path, data['image'])
                label_path = os.path.join(self.save_label_dir, 'gridmask.txt')
                with open(label_path, 'a+') as f:
                    f.write(img_path.replace('/paddle/data/ch_26w/', '') + '\t' + data['label'] + '\n')
        return data