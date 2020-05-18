"""xbot entrypoint"""
import argparse
import logging
import xbot.constants
import xbot.translate

def parse_commandline_args():
    parser = argparse.ArgumentParser(description='xbot translates your bot code from one messaging platform to another, generates a file gen__xbot.py or --output_file')
    parser.add_argument('sourcecode_filename', metavar='sourcecode_filename', type=str, nargs=1,
                        help='name of the file to translate')
    parser.add_argument('--source_library', type=str,
                        default="python-telegram-bot",
                        help='library in which the source code is written in')
    parser.add_argument('--destination_library', type=str,
                        default="discord.py",
                        help='library to translate the code into')
    parser.add_argument('--output_file', type=str,
                        default="",
                        help='name of the output filee')
    parser.add_argument('--verbose', 
                        action='store_true',
                        help='verbose logging')
    parser.add_argument('-v', 
                        action='store_true',
                        help='verbose logging')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_commandline_args()
    if args.verbose or args.v:
        logging.basicConfig(level=logging.INFO)
    xbot.translate.translate(args.sourcecode_filename[0], output_file=args.output_file)
