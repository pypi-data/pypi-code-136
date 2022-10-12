import argparse
from .file.base import split_train_eval_files

def split_files(args):
    split_train_eval_files(
        data_dir = args.d,
        eval_size = args.e,
        save_dir = args.s,
        shuffle = args.r,
        seed = args.seed,
        valid_ext = args.v,
        remain_data = args.remain_data
    )



def run_cli():
    parser = argparse.ArgumentParser(description='mlpreprocessor command line interface')
    subparser = parser.add_subparsers(help='subcommand help')
    split_files_parser = subparser.add_parser('split-files', help='split data into train and eval')
    split_files_parser.add_argument('-d', '--data_dir', type=str, default='.', help='dataset to be splitted')
    split_files_parser.add_argument('-e', '--eval_size', type=float, default=0.1, help='proportion of eval dataset')
    split_files_parser.add_argument('-s', '--save_dir', type=str, default=None, help='directory to save splitted dataset')
    split_files_parser.add_argument('-r', '--random', action='store_true', help='if shuffle dataset')
    split_files_parser.add_argument('--seed', type=int, default=1000, help='random seed')
    split_files_parser.add_argument('-v', '--valid_ext', type=str, default=[], help='valid extension in the dataset')
    split_files_parser.add_argument('--remain_data', action='store_true', help='if remain original dataset')
    split_files.set_defaults(split_files)

if __name__=='__main__':
    run_cli()


