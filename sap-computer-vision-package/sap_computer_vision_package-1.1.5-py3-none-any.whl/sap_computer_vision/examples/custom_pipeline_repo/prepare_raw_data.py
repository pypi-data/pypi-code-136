from os.path import join, basename
import os
import glob
import argparse
from PIL import Image, ImageFile, ImageFilter, PngImagePlugin
import numpy as np

import multiprocessing
import subprocess

import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


LARGE_ENOUGH_NUMBER = 1000000
PngImagePlugin.MAX_TEXT_CHUNK = LARGE_ENOUGH_NUMBER * (1024**2)  # avoid PIL error due to large metadata


def get_id_from_filename(filename):
    return os.path.basename(filename).split('_')[0].rsplit('.')[0]


def list_files_in_subdir(root_path, suffix=['jpg', 'jpeg', 'png']):
    """
    This function list all the files with specified suffix in the root_path and its subdirectories
    :param root_path: root path that contains all files you want to list
    :param suffix: list of file format in LOWER case. e.g ['jpg','png']
    :return: list of relative path of files in root path
    """
    img_file_list = []
    for x in os.walk(root_path):
        for file in x[-1]:
            relative_path = x[0].strip(root_path).strip('/')
            if file.split('.')[-1].lower() in suffix:
                img_file_list.append(os.path.join(relative_path, file))
    return img_file_list


def create_transparent_background_png(raw_jpg_folder, dst_folder,
                                      background_color='white',
                                      fuzz=15):
    if not os.path.exists(dst_folder):
        os.mkdir(dst_folder)
    all_images = list_files_in_subdir(raw_jpg_folder)
    for img in all_images:
        img_path = os.path.join(raw_jpg_folder, img)
        dst_img = os.path.join(dst_folder, basename(img).split('.')[0] + '.png')

        subprocess.call("convert {} -define png:color-type=6 -transparent {} -fuzz {}% {}".format(img_path, background_color, fuzz, dst_img),
                        shell=True)


def crop_object_naive(img):
    mask = np.array(img.split()[-1])

    x = np.sum(mask != 0, axis=0)
    y = np.sum(mask != 0, axis=1)

    x1 = min(np.where(x > 0)[0])
    x2 = max(np.where(x > 0)[0])
    y1 = min(np.where(y > 0)[0])
    y2 = max(np.where(y > 0)[0])

    obj = img.crop((x1, y1, x2, y2))
    return obj


def crop_object_transparent_background(img, A_threshold=100, kernel_size=5):
    img_array = np.array(img)
    channelA = img_array[:, :, -1]

    a = Image.fromarray(channelA * (channelA >= A_threshold), 'L')

    erode = a.filter(ImageFilter.MinFilter(kernel_size))
    dilate = erode.filter(ImageFilter.MaxFilter(kernel_size))
    mask = np.array(dilate)

    x = np.sum(mask != 0, axis=0)
    y = np.sum(mask != 0, axis=1)

    x1 = min(np.where(x > kernel_size)[0])
    x2 = max(np.where(x > kernel_size)[0])
    y1 = min(np.where(y > kernel_size)[0])
    y2 = max(np.where(y > kernel_size)[0])

    obj = img.crop((x1, y1, x2, y2))
    return obj


def expand_to_square(obj, pad_scale=1.2):
    w, h = obj.size
    s = int(max(w, h) * pad_scale)
    img = Image.fromarray(np.zeros((s, s, 4)), 'RGBA')
    img.paste(obj, (int(0.5 * (s - w)), int(0.5 * (s - h)),
                    int(0.5 * (s + w)), int(0.5 * (s + h))), obj)
    return img


def calc_percentage(img):
    channelA = np.asarray(img)[:, :, -1]
    num_pixels = img.size[0] * img.size[1]
    percentage = np.sum(channelA != 0) / num_pixels
    return percentage


def process_img(img_path, dst_folder, material, size=512):
    try:
        img = Image.open(img_path)
        # crop the image first to avoid too small ouput image after resizing
        img = crop_object_naive(img)

        # 1st stage resize to reduce dimensionality of too big raw images
        if img.size[0] > size * 4 and img.size[1] > size * 4:
            img = img.resize((size * 4,
                              int(size * 4 * img.size[1] / img.size[0])),
                             resample=Image.BILINEAR)

        # calculate kernel for dilation and erosion based on heuristics
        # bigger kernel can handle more noise but might also remove some parts
        # of the object
        kernel_size = ((img.size[0] + img.size[1]) // 1024) * 2 + 1
        obj = crop_object_transparent_background(img, 100, kernel_size)

        percentage = calc_percentage(obj)
        if percentage < 0.2:
            obj = crop_object_transparent_background(obj, 200, kernel_size)

        new_img = expand_to_square(obj)

        if new_img.size[0] > size and new_img.size[1] > size:
            new_img = new_img.resize((size, size), resample=Image.BILINEAR)

        fname = os.path.basename(img_path)
        fname = fname[:-3] + 'jpg'

        jpg = Image.new("RGB", new_img.size, (255, 255, 255))
        jpg.paste(new_img, mask=new_img.split()[3])  # 3 is the alpha channel
        jpg.save(
            os.path.join(
                dst_folder,
                material,
                fname),
            'JPEG'
        )
        return new_img
    except Exception as e:
        print(img_path)
        print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Preprocessing')

    parser.add_argument('--raw_dataset_path', type=str,
                        default='/data/DB/raw_dataset/OriginalData/3500_complete',
                        required=True, help='raw dataset path ')
    parser.add_argument('--save_path', type=str,
                        default='/data/DB/dataset/3500_complete',
                        required=True, help='output dataset path ')
    parser.add_argument('--img_size', type=int,
                        default=512,
                        required=False, help='size of output images')

    config = parser.parse_args()

    # org_folder are organized as such:
    # ./date/split/material/imagefile
    # E.g.  ./02-01-2019/training/00728383_2/00728383_2_24.png
    org_folder = config.raw_dataset_path
    dst_folder = config.save_path
    size = config.img_size

    counter = 0
    if os.path.exists(dst_folder):
        print('Directory already exist. Please specify another location')
    else:
        os.mkdir(dst_folder)

        print("Converting images to png with transparent background")
        png_folder = org_folder + '_png'
        create_transparent_background_png(org_folder, png_folder,
                                          background_color='white',
                                          fuzz=15)
        print("Finished converting. PNG images saved in :", png_folder)
        print("Generating dataset")
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        processes = []
        for img_path in glob.glob(os.path.join(png_folder, '*.png')):
            material = get_id_from_filename(os.path.basename(img_path))
            if not os.path.exists(os.path.join(dst_folder, material)):
                os.mkdir(os.path.join(dst_folder, material))

            if counter % 1000 == 0:
                print(counter, "images processed")
            t = multiprocessing.Process(
                target=process_img, args=(
                    img_path, dst_folder, material, size,))
            t.start()
            counter += 1

        print(counter, "images processed")
