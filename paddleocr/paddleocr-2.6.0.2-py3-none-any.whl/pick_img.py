import os 
import random
import shutil

# img_dir = '/paddle/data/ch_26w/mixup/images'
# imgs = os.listdir(img_dir)
# res = random.sample(imgs, 20)
# save_dir = './mixup_imgs'
# os.makedirs(save_dir, exist_ok=True)
# for r in res:
#     shutil.copyfile(os.path.join(img_dir, r), os.path.join(save_dir, r))

label_file = '/paddle/data/ch_26w/mixup/labels/mixup.txt'

cnt = 0
with open(label_file, 'r') as f:
    lines = f.readlines()
    valid_lines = []
    for idx, line in enumerate(lines):
        l = line.strip().split('\t')

        if len(l) >=2:
            valid_lines.append(line)
        else:
            cnt += 1
with open(os.path.join('/paddle/data/ch_26w/valid_label', label_file.split('/')[-1]), 'a+') as fd:
    fd.writelines(valid_lines)
print(cnt)
print('valid', len(valid_lines))
print('total', len(lines))