import os
import shutil
import fire
import yaml
import pickle
import numpy as np
from collections import defaultdict

def rotate_pixel(pixel_pos, tile_orientation):
    return pixel_pos[0]*tile_orientation[2], pixel_pos[1]*tile_orientation[1]

def multi_layout_to_dict(geom_repo, geom_name):

    yaml_path = os.path.join(geom_repo, geom_name + ".yaml")
    with open(yaml_path) as infile:
        geometry_yaml = yaml.load(infile, Loader=yaml.FullLoader)

    pixel_pitch = geometry_yaml['pixel_pitch']
    chip_channel_to_position = geometry_yaml['chip_channel_to_position']
    tile_orientations = geometry_yaml['tile_orientations']
    tile_positions = geometry_yaml['tile_positions']
    tpc_centers = geometry_yaml['tpc_centers']
    tile_indeces = geometry_yaml['tile_indeces']
    xs = np.array(list(chip_channel_to_position.values()))[:, 0] * pixel_pitch
    ys = np.array(list(chip_channel_to_position.values()))[:, 1] * pixel_pitch
    x_size = max(xs) - min(xs) + pixel_pitch
    y_size = max(ys) - min(ys) + pixel_pitch

    geometry = defaultdict(dict)

    for tile in geometry_yaml['tile_chip_to_io']:
        tile_orientation = tile_orientations[tile]
        for chip in geometry_yaml['tile_chip_to_io'][tile]:
            io_group_io_channel = geometry_yaml['tile_chip_to_io'][tile][chip]
            io_group = io_group_io_channel // 1000
            io_channel = io_group_io_channel % 1000

        for chip_channel in geometry_yaml['chip_channel_to_position']:
            chip = chip_channel // 1000
            channel = chip_channel % 1000
            try:
                io_group_io_channel = geometry_yaml['tile_chip_to_io'][tile][chip]
            except KeyError:
                continue

            io_group = io_group_io_channel // 1000
            io_channel = io_group_io_channel % 1000
            x = chip_channel_to_position[chip_channel][0] * \
                pixel_pitch + pixel_pitch / 2 - x_size / 2
            y = chip_channel_to_position[chip_channel][1] * \
                pixel_pitch + pixel_pitch / 2 - y_size / 2

            x, y = rotate_pixel((x, y), tile_orientation)
            # from multi_tile_layout-2.3.16 onwards, use tile_indeces[tile][0]
            # for multi_tile_layout-2.2.16 and prior versions, use tile_indeces[tile][1]
            x += tile_positions[tile][2] + \
                tpc_centers[tile_indeces[tile][0]][0]
            y += tile_positions[tile][1] + \
                tpc_centers[tile_indeces[tile][0]][1]

            z = tile_positions[tile][0] + \
                tpc_centers[tile_indeces[tile][0]][2]
            direction = tile_orientations[tile][0]

            geometry[(io_group, io_channel, chip, channel)] = np.array([x, y, z, direction])

    # need to figure out what to do in case one doesn't have writting rights
    dict_path = os.path.join(geom_repo, "dict_repo")
    if not os.path.exists(dict_path):
        os.makedirs(dict_path)
    geom_dict_pkl_name = os.path.join(dict_path, geom_name + ".pkl")

    with open(geom_dict_pkl_name, 'wb') as outfile:
        pickle.dump(dict(geometry), outfile, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    fire.Fire(multi_layout_to_dict)
