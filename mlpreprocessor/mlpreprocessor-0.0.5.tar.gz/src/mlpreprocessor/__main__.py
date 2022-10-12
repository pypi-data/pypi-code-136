import argparse
from .file.base import split_train_eval_files, split_tar

def split_files(args):
    split_train_eval_files(
        data_dir = args.data_dir,
        eval_size = args.eval_size,
        save_dir = args.save_dir,
        shuffle = args.random,
        seed = args.seed,
        valid_ext = args.valid_ext,
        remain_data = args.remain_data
    )

def split_tar_files(args):
    split_tar(
        name = args.name,
        data_dir = args.data_dir,
        n = args.n,
        save_dir = args.save_dir,
        remain_data= args.remain_data
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
    split_files_parser.add_argument('--remain_data', action='store_true', help='whether remain original dataset')
    split_files_parser.set_defaults(func=split_files)

    split_tar_parser = subparser.add_parser('split-tar', help='compress data and split into n parts')
    split_tar_parser.add_argument('-m', '--name', type=str, help='tar file name')
    split_tar_parser.add_argument('-d', '--data_dir', type=str, default='.', help='dataset to be compressed')
    split_tar_parser.add_argument('-n', type=int, default=2, help='splitted into n parts')
    split_tar_parser.add_argument('-s', '--save_dir', type=str, default=None, help='directory to save splitted tar file')
    split_tar_parser.add_argument('--remain_data', action='store_true', help='wheter remain original dataset')
    split_tar_parser.set_defaults(func=split_tar_files)

    args = parser.parse_args()
    args.func(args)


if __name__=='__main__':
    run_cli()


