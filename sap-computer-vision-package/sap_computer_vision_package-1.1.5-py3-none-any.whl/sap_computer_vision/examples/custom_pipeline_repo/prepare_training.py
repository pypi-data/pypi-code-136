import glob
import json
import os
import pathlib
import random
import shutil
from zipfile import ZipFile
from PIL import Image

from metaflow import FlowSpec, step, argo, Parameter, JSONType
import numpy as np


DATA_OUTPUT_DIR = pathlib.Path('/tmp/dataout')
DATA_INPUT_DIR = pathlib.Path('/tmp/datain')
PVC_DIR = pathlib.Path('/mnt/')


def cache_background_images(path, w=500, h=500):
    files = [f for f in os.listdir(path) if f[-3:] in ['jpg', 'png']]
    images = [(f[:-4], Image.open(path / f).convert('RGBA').resize((w, h), Image.BICUBIC)) for f in files]
    return images


def synthesize(fg_path, bg_cache, n=5, w=500, h=500, quality=False):
    sampling = Image.BICUBIC if quality else Image.NEAREST

    def augment(fg, bg, transparency, rotation):
        thresh = 255. * transparency
        fg = np.array(fg)
        fg[:, :, 3] = (255 * (fg[:, :, :3] < thresh).any(axis=2)).astype(np.uint8)
        fg = Image.fromarray(fg)
        fg = fg.rotate(rotation, resample=sampling, expand=False, fillcolor=(255, 255, 255, 0))
        fg = fg.resize((w, h), sampling)
        bg = bg.copy()
        bg.paste(fg, (0, 0), fg)
        return bg

    fg = Image.open(fg_path).convert('RGBA')

    results = []
    for i in range(n):
        transparency = random.uniform(0.85, 0.95)
        rotation = random.uniform(-30., 30.)
        bg_name, bg = random.choice(bg_cache)
        filename = "{}_{}_t{}_r{}.jpg".format(fg_path.stem, bg_name, transparency, rotation)
        augmented = augment(fg, bg, transparency=transparency, rotation=rotation).convert('RGB')
        results.append((filename, augmented))

    return results


class ImageSynthesis(FlowSpec):
    catalog_zip_path = Parameter("catalog_images")
    background_zip_path = Parameter("background_images")
    image_target_size = Parameter("image_size", help="Target image size", type=JSONType, default=json.dumps([500, 500]))
    n_augmentations = Parameter("n_augmentations", help="Number of augmentations to apply to each catalog image",
                                default=5)
    quality = Parameter("quality", help="Uses bicubic interpolation instead of nearest neighbor if True",
                        default=False)
    preprocess_catalog = Parameter("preprocess_catalog", help="Initial catalog preprocessing performed if True",
                                   default=True)
    seed = Parameter("seed", help="Random seed", default=1337)

    def _unzip_data(self):
        catalog_path = self.catalog_new_path
        catalog_target = PVC_DIR / "catalog"
        os.mkdir(catalog_target)
        background_path = self.background_new_path
        background_target = PVC_DIR / "background"
        os.mkdir(background_target)
        with ZipFile(catalog_path, "r") as f:
            f.extractall(catalog_target)
        os.unlink(catalog_path)
        with ZipFile(background_path, "r") as f:
            f.extractall(background_target)
        os.unlink(background_path)
        return catalog_target, background_target

    @argo(output_artifacts=[{'name': 'prepareddata',
                             'globalName': 'prepareddata',
                             'path': str(DATA_OUTPUT_DIR),
                             'archive': {'none': {}}}],
          input_artifacts=[{'name': 'datain',
                            'path': str(DATA_INPUT_DIR)}],
          labels={'ai.sap.com/resourcePlan': 'basic.8x'},
          mount_pvc="/mnt")
    @step
    def start(self):
        random.seed(self.seed)
        self.catalog_new_path = PVC_DIR / "catalog.zip"
        self.background_new_path = PVC_DIR / "backgrounds.zip"
        shutil.move(self.catalog_zip_path, self.catalog_new_path)
        shutil.move(self.background_zip_path, self.background_new_path)
        print("Unzipping catalog and background images...")
        catalog_path, background_path = self._unzip_data()
        print("  done!")
        if self.preprocess_catalog:
            print("Preprocessing catalog...")
            catalog_processed_path = PVC_DIR / "catalog_processed"
            os.system("python prepare_raw_data.py --raw_dataset_path {} --save_path {} --img_size 512".format(
                catalog_path, catalog_processed_path))
            print("  done!")
            os.chdir(catalog_processed_path)
            print("Zipping preprocessed catalog...")
            os.system("zip -r catalog_processed.zip * > /dev/null 2>&1")
            shutil.move(catalog_processed_path / "catalog_processed.zip", DATA_OUTPUT_DIR / "catalog_processed.zip")
            print("  done!")
            catalog_path = catalog_processed_path
        print("Caching background images...")
        bg_cache = cache_background_images(background_path)
        print("  done! ({} images cached)".format(len(bg_cache)))
        os.chdir(catalog_path)
        print("Starting to augment images...")
        if self.quality:
            print("Using bicubic interpolation")
        else:
            print("Using nearest neighbor sampling")
        fg_image_paths = glob.glob("*/*.jpg", recursive=True)
        print("{} images detected in catalog".format(len(fg_image_paths)))
        percentages = set([int(n) for n in np.linspace(1, len(fg_image_paths), 21)][1:])  # print progress every 5%
        cur_progress = 0
        work_dir = PVC_DIR / "augmented"
        os.mkdir(work_dir)
        for i, path in enumerate(fg_image_paths):
            path = pathlib.Path(path)
            target_path = work_dir / path.parents[0]
            target_path.mkdir(exist_ok=True)
            augments = synthesize(
                path, bg_cache, n=self.n_augmentations, w=self.image_target_size[0], h=self.image_target_size[1],
                quality=self.quality
            )
            for fname, img in augments:
                target = target_path / fname
                img.save(target)
            if i+1 in percentages:
                cur_progress += 5
                print("{}% done ({} images processed)".format(
                    cur_progress, int(len(fg_image_paths) / 100. * cur_progress))
                )
        print("Zipping augmented images...")
        os.chdir(work_dir)
        os.system("zip -r train_augmented.zip * > /dev/null 2>&1")
        shutil.move(work_dir / "train_augmented.zip", DATA_OUTPUT_DIR / "train_augmented.zip")
        print("  done!")
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == '__main__':
    ImageSynthesis()
