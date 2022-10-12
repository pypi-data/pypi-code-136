import os
import argparse
import pandas as pd
import numpy as np
import julian
import logging
import sys
from datetime import datetime


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"{path} is not a valid directory path.")


def file_path(path):
    if os.path.isfile(path):
        if not path.endswith('.csv'):
            return argparse.ArgumentTypeError(f"{path} extension is not a valid CSV file.")
        return path
    else:
        raise argparse.ArgumentTypeError(f"{path} is not a valid file path.")


def import_data(satellite_number, path_to_file, p_value):
    data = pd.read_csv(path_to_file)
    data = data.iloc[1:]

    if 'SV G' + satellite_number + ' El (L1C/A)' in data:
        df = pd.DataFrame()
        df['time'] = data['UTC'].apply(
            lambda l: julian.to_jd(datetime(int(l[19:23]), int(l[13:15]), int(l[16:18]), int(l[:2]),
                                            int(l[3:5]), int(l[6:8]))) - 2400000.5)

        df['elevation SV' + satellite_number] = data['SV G' + satellite_number + ' El (L1C/A)']

        if len(df['elevation SV' + satellite_number].unique()) > 1:
            df, period = period_selector(df, satellite_number, p_value)
            x_df = df['time'].values
            y_df = df['elevation SV' + satellite_number].values
            return x_df, y_df, period

    logging.error('No data for Satellite ' + satellite_number + ' from file ' + path_to_file + '.')
    sys.exit(1)


def period_selector(elevation_df, satellite_number, p_value):
    """

    Args:
        elevation_df:
        satellite_number:
        p_value:

    Returns:

    """
    try:
        start_zero_index = elevation_df.index[elevation_df['elevation SV' + satellite_number] == 0].tolist()[0]
        start_finder = elevation_df[start_zero_index:]
        end_zero_index = start_finder.index[start_finder['elevation SV' + satellite_number] > 0].tolist()[0]
        idx = (start_zero_index + end_zero_index) // 2
        period_start = elevation_df.iloc[idx]['time']
        period_end = elevation_df[elevation_df['time'] >= (period_start + p_value)]['time'].tolist()[0]
        period = elevation_df[(elevation_df['time'] >= period_start) & (elevation_df['time'] <= period_end)]

        return elevation_df[idx:], period

    except Exception as e:
        logging.exception(e)
        logging.exception(
            'No file is long enough to allow an Analysis. At least one file must contain 24h of continuous data.')


def split_p_val(x, y, p_value, intervals):
    x_temp = np.array(x) % p_value
    for interval in intervals:
        interval['x'] = []
        interval['y'] = []
        for i in range(len(x_temp)):
            if (x_temp[i] >= interval['x_min']) * (x_temp[i] <= interval['x_max']):
                interval['x'].append(x[i])
                interval['y'].append(y[i])

    return intervals


def split_data(x, y, results=None):
    """

    Args:
        x: [0, .. , 1] with step = 1/len(x)
        y: [0, .. ,0, N, .. , N, 0, .. 0, N, .. N, 0, .. 0, etc.]
        results: Array of tuples. Each tuple contains 2 arrays.

    Returns: results = [ ( x1, y1), (x2, y2), etc.] with length xi = length yi, yi = [N, .., N]
    with N any number and xi the sample of x that matches yi

    """
    if results is None:
        results = []
    xi = []
    yi = []
    zero = True
    i = 0
    for data_elt in y:
        if data_elt > 0:
            if zero:
                zero = not zero
            yi.append(data_elt)
            xi.append(x[i])
        elif data_elt <= 0:
            if not zero:
                results.append((xi, yi))
                return split_data(x[i:], y[i:], results)
        i += 1
    return results


def get_images(directory):
    other_images = []
    for img in os.listdir(directory):
        img_path = os.path.join(directory, img)
        if img.split('.')[-1] == 'png':
            if img.split('_')[0] == 'analysis':
                analysis_image = img_path
            elif img.split('_')[0] == 'hist':
                evaluation_image = img_path
            else:
                other_images.append(img_path)

    return analysis_image, evaluation_image, other_images


def remove_files(directory):
    for img in os.listdir(directory):
        if img.split('.')[-1] == 'png':
            os.remove(os.path.join(directory, img))


def parse_str(number):
    if number < 0:
        return '( {} )'.format(str(number))
    return str(number)
