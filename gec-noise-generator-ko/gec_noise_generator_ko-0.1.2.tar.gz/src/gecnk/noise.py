from __future__ import absolute_import
from noise_generate import noise_generate
import argparse
import json
import sys
sys.path.append('..')
sys.path.append('.')
current_file = os.path.dirname(__file__)
sys.path.append(current_file)


def noise(data_directory, error_type, vec_directory):
    print(error_type)
    noise_generate(data_directory, error_type)
    print("Complete")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Noise to text')
    parser.add_argument('--d', metavar='data_directory',
                        help='Input the path to text data after --d ', default="src/gecnk/resources/test-tgt", type=str)
    parser.add_argument('--e', metavar='error_type',
                        help='Input the error type list after --e', nargs='+',
                        default=["polite_speech_error"])
    args = parser.parse_args()
    noise(data_directory=args.d, error_type=args.e, vec_directory=args.v)
