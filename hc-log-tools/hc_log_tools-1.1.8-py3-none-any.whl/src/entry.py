import src.pack_log
import src.v_t_chart
import argparse
import fcntl
import sys

def entry():
    # only can run one process at a time
    lock_file = open("/tmp/log-tool-lock", "w")
    try:
        fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        print("another process is running, exit")
        sys.exit(-1)


    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.set_defaults(func=lambda args: parser.print_help())

    subparsers = parser.add_subparsers(title='subcommands', dest='command', help='sub-command help')

    subparsers_pack = subparsers.add_parser("pack", help='pack help')
    src.pack_log.init_input_args(subparsers_pack)
    subparsers_pack.set_defaults(func=src.pack_log.pack_log)

    subparsers_chart = subparsers.add_parser("chart", help='chart help')
    src.v_t_chart.init_input_args(subparsers_chart)
    subparsers_chart.set_defaults(func=src.v_t_chart.generate_chart)

    # parse the args and call whatever function was selected
    args = parser.parse_args()
    args.func(args)


if __name__=="__main__":
    sys.exit(entry())