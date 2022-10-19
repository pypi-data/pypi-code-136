import sys
import os
import numpy as np
import cv2
import json
from collections import defaultdict
import unittest
import torch
import tempfile
from filecmp import dircmp

sys.path.insert(0, os.path.abspath('')) # Test files from current path rather than installed module
from pymlutil.metrics import *
from pymlutil.s3 import *

test_config = 'test.yaml'

class Test(unittest.TestCase):
   
   def test_infer_results(self):
        parameters = ReadDict(test_config)

        if 's3' not in parameters:
            raise ValueError('s3 not in {}'.format(test_config))

        s3, _, s3def = Connect(parameters['s3']['credentials'])

        iBatch=0
        images = torch.rand([4, 3, 512, 512]).permute(0, 2, 3, 1).numpy()


        labels = torch.argmax(torch.rand([4, 8, 512, 512]),dim=1).type(torch.uint8).numpy()
        segmentations = torch.argmax(torch.rand([4, 8, 512, 512]),dim=1).type(torch.uint8).numpy()


        mean = [0]*4
        stdev = [0]*4
        dt = 1e-4

        class_dict = 'cityscapes_2classes'
        class_dict_path = f'model/cityscapes/{class_dict}'
        class_dictionary = s3.GetDict(s3def['sets']['dataset']['bucket'], class_dict_path + '.json')

        results = DatasetResults(class_dictionary, batch_size=1, imStatistics=False, imgSave='test_images', imRecord=False, task='segmentation')
        cm = results.infer_results(iBatch, images, labels, segmentations, mean, stdev, dt)

if __name__ == '__main__':
    unittest.main()