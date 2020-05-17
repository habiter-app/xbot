"""xbot entrypoint"""
import argparse

def parse_commandline_args():
    parser = argparse.ArgumentParser(description='xbot translates your bot code from one messaging platform to another')
    parser.add_argument('sourcecode_filename', metavar='N', type=str, nargs=1,
                        help='name of the file to translate')
    parser.add_argument('--from', type=str,
                        default="python-telegram-bot",
                        help='library in which the source code is written in')
    parser.add_argument('--to', type=str,
                        default="discord.py",
                        help='library to translate the cod  into')
    args = parser.parse_args()

def parse_source_code(filename, library=None):
    pass

def generate_destination_code(params):
    pass

if __name__ == "__main__":
    args = parse_commandline_args()
    parse_source_code(args.sourcecode_filename)
