import pathlib

import pandas as pd

import wmb

palette_dir = pathlib.Path(wmb.__path__[0]) / 'files/palette'


def read_palette(palette_path):
    return pd.read_csv(palette_path, index_col=0, header=None).squeeze().to_dict()


PALETTES = {
    p.stem: read_palette(p)
    for p in palette_dir.glob('*.csv')
}
