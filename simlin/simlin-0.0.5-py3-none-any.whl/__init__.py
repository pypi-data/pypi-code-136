#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals


import sys
import argparse
from simlin import image_resize


__license__ = 'MIT'


def get_args():
    '''Parse command line arguments.'''

    parser = argparse.ArgumentParser(
        description='Use argparsing to allow better scripting of image batch jobs')

    '''
    parser.add_argument('-f',
                        '--file',
                        type=str,
                        help='Enter file name to modify',
                        required=False
                        )

    parser.add_argument('-d',
                        '--dir',
                        type=str,
                        help='Enter the relative location of the directory',
                        required=False
                        )
    '''

    parser.add_argument('-r',
                        '--resize',
                        type=int,
                        help='The new size of the file. Valid Options',
                        required=False
                        )

    parser.add_argument('-q',
                        '--quality',
                        type=str,
                        help='Quality of image.  95 is best.  Default is 75)',
                        required=False,
                        default=75
                        )

    args = parser.parse_args()
    # file = args.file
    # dir = args.dir
    new_size = args.resize
    new_quality = args.quality
    # return file, dir, new_size, new_quality
    return new_size, new_quality

def batch():
    # file, dir, new_size, new_quality = get_args()
    new_size, new_quality = get_args()
    image_resize.batch_main(size=new_size, quality=new_quality)


def main():
    '''Main function directs process to batch or interactive mode'''
    # check sys.argv length
    # if greater then 1 batch()
    # of 1
    if len(sys.argv) > 1:
        batch()
    else:
        image_resize.interactive()
