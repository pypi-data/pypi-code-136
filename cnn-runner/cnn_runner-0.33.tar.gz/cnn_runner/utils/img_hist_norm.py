import numpy as np
from imageio import imsave
from imageio import imread
import sys, os
# import pyvips
import cv2

def get_histogram(img):
    '''
    calculate the normalized histogram of an image
    '''
    height, width = img.shape
    hist = [0.0] * 256
    for i in range(height):
        for j in range(width):
            hist[img[i, j]]+=1
    return np.array(hist)/(height*width)

def get_cumulative_sums(hist):
    '''
    find the cumulative sum of a numpy array
    '''
    return [sum(hist[:i+1]) for i in range(len(hist))]

def normalize_histogram(img):
    # calculate the image histogram
    hist = get_histogram(img)
    # get the cumulative distribution function
    cdf = np.array(get_cumulative_sums(hist))
    # determine the normalization values for each unit of the cdf
    sk = np.uint8(255 * cdf)
    # normalize the normalization values
    height, width = img.shape
    Y = np.zeros_like(img)
    for i in range(0, height):
        for j in range(0, width):
            Y[i, j] = sk[img[i, j]]
    # optionally, get the new histogram for comparison
    new_hist = get_histogram(Y)
    # return the transformed image
    return Y

def get_base_img_name(name_with_dir):
    img_name = os.path.basename(name_with_dir)
    return img_name.split('.')[0]

def read_process_and_save(img_name, img_path):
    # img = imread(img_load)
    # normalized = normalize_histogram(img)
    # imsave(get_base_img_name(img_load) + '-normalized.jpg', normalized)

    # x = pyvips.Image.new_from_file(img_load)
    # x = x.hist_equal()
    # x.write_to_file(get_base_img_name(img_load) + '-normalized.jpg')

    # read image

    img_name_full = os.path.join(img_path, img_name)
    img = cv2.imread(img_name_full, cv2.IMREAD_COLOR)

    # normalize float versions
    norm_img1 = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    norm_img2 = cv2.normalize(img, None, alpha=0, beta=1.2, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    # scale to uint8
    norm_img1 = (255 * norm_img1).astype(np.uint8)
    norm_img2 = np.clip(norm_img2, 0, 1)
    norm_img2 = (255 * norm_img2).astype(np.uint8)

    # write normalized output images
    cv2.imwrite(os.path.join(img_path, get_base_img_name(img_name)) + '-normalized1.jpg', norm_img1)
    cv2.imwrite(os.path.join(img_path, get_base_img_name(img_name)) + '-normalized2.jpg', norm_img2)

