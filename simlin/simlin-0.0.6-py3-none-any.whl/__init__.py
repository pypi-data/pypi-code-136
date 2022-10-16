#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals


import sys
import argparse
from simlin import image_resize


__license__ = 'MIT License'
__version__ = 'Simlin (Simple Image Manipulator for Linux) v0.0.6'

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
                        help='The new horizontal pixel size of the file. Will auto-calculate the vertical size.',
                        required=False
                        )

    parser.add_argument('-q',
                        '--quality',
                        type=int,
                        help='Quality of image.  95 is best.  Default is 75. The higher the quality the larger the file.',
                        required=False,
                        default=75
                        )

    parser.add_argument('-v',
                        '--version',
                        help='Display the current version.',
                        action="store_true"
                        )

    args = parser.parse_args()
    # file = args.file
    # dir = args.dir
    new_size = args.resize
    new_quality = args.quality
    latest_version = args.version

    return new_size, new_quality, latest_version

def batch(new_size, new_quality):
    '''send parameters and process images'''
    image_resize.batch_main(size=new_size, quality=new_quality)

def main():
    '''Main function directs process to batch or interactive mode'''
    
    new_size, new_quality, latest_version = get_args()
    if latest_version == True:
        print(__version__)
        exit(0)

    if len(sys.argv) > 1:
        print(len(sys.argv))
        batch(new_size, new_quality)

    else:
        image_resize.interactive()
