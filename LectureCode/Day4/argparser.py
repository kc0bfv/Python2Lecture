#!/usr/bin/env python
"""
Try: ./argparser.py -bs 3 -t 2 -c in -r -d 4 argparser_test.txt
"""


import argparse
import itertools as it
import sys

def process_line(line, contain, duplicate, reverse):
    """
    :param line str:
    :param contain str:
    :param duplicate int:
    :param reverse bool:
    """
    if contain not in line:
        return
    for _ in range(duplicate):
        yield line[::-1] if reverse else line


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Just a demo")
    parser.add_argument("infile", nargs="?", type=argparse.FileType("r"),
            default=sys.stdin, help="The input filename, default to stdin")
    parser.add_argument("outfile", nargs="?", type=argparse.FileType("w"),
            default=sys.stdout, help="The input filename, default to stdout")
    parser.add_argument("-bs", "--beginning-skip", type=int, default=0,
            help="The number of input lines to skip (default - 0)")
    parser.add_argument("-t", "--take", type=int, default=None,
            help="The number of lines to take (default - all)")
    parser.add_argument("-c", "--contain", type=str, default="",
            help="Only take lines that contain this")
    parser.add_argument("-d", "--duplicate", type=int, default=1,
            help="The number of times to duplicate each taken line")
    parser.add_argument("-r", "--reverse", action="store_true",
            help="Set this to reverse each input")

    args = parser.parse_args()

    for line in it.islice(args.infile, args.beginning_skip,
            None if args.take is None else args.take + args.beginning_skip):
        for outline in process_line(line, args.contain,
                args.duplicate, args.reverse):
            args.outfile.write(outline)
