import os 
import cv2
import numpy as np

data_dir = '/paddle/data/ch_26w/real_data'
label_file = '/paddle/data/ch_26w/real_data/train_list.txt'
alpha = 0.2
save_img_dir = '/paddle/data/ch_26w/mixup/images'
save_label_dir = '/paddle/data/ch_26w/mixup/labels'
os.makedirs(save_img_dir, exist_ok=True)
os.makedirs(save_label_dir, exist_ok=True)


def get_idx(i, n):
    j = np.random.randint(n)
    while i == j:
        j = np.random.randint(n)
    return j


def reshape_same(img1, img2):
    h1, w1, _ = img1.shape
    h2, w2, _ = img2.shape
    img_res = cv2.resize(img2, (w1, h1))
    return img_res


with open(label_file, "r") as f:
    lines = f.readlines()
    length = len(lines)
    for idx, data_line in enumerate(lines):
        # origin image
        substr_ori = data_line.strip("\n").split('\t')
        file_name_ori = substr_ori[0]
        label_ori = substr_ori[1]
        img_path_ori = os.path.join(data_dir, file_name_ori)
        img_ori = cv2.imread(img_path_ori)
        # mix image
        mix_idx = get_idx(idx, length)
        substr_mix = lines[mix_idx].strip("\n").split('\t')
        file_name_mix = substr_mix[0]
        img_path_mix = os.path.join(data_dir, file_name_mix)
        img_mix = cv2.imread(img_path_mix)
        # mixup
        lam = np.random.beta(alpha, alpha)
        img_mix_sameshape = reshape_same(img_ori, img_mix)
        img_mixed = lam * img_ori + (1 - lam) * img_mix_sameshape
        # save res
        save_img_path = os.path.join(save_img_dir, img_path_ori.split('/')[-1])
        if not os.path.exists(save_img_path):
            cv2.imwrite(save_img_path, img_mixed)
            label_path = os.path.join(save_label_dir, 'mixup.txt')
            with open(label_path, 'a+') as f:
                f.write(save_img_path.replace('/paddle/data/ch_26w/', '') + '\t' + label_ori + '\n')

        if (idx + 1) % 10000 == 0:
            print('process num : ', idx + 1)
    print('finished!')