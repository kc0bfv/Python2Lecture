#!/usr/bin/env python

from __future__ import print_function

# Print out a sober hello world
print("Hello, world.")

def diag_print(msg):
    """Print a message on a diagonal

    :param str msg: The message to print
    """
    for ind, char in enumerate(msg):
        print(" " * ind + char)

if __name__ == '__main__':
    diag_print("SUP WORLD?!?!")
