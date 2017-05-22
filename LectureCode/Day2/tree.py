#!/usr/bin/env python

from __future__ import print_function

import json

def input_branch(depth=0):
    possible_selections = ["B","L","N"]
    branch = list()
        
    keep_going = True
    while keep_going:
        selection = ""
        while selection not in possible_selections:
            selection = raw_input(
                    "Depth: {} - Add a (B)ranch, (L)eaf or "\
                            "(N)either? ".format(depth)
                    ).upper()[:1]
        if selection == "B":
            branch.append(input_branch(depth+1))
        elif selection == "L":
            branch.append(raw_input("Input leaf contents: "))
        elif selection == "N":
            return branch
        else:
            print("I don't know how you did that man, but I'm done!")
            return branch
            
def print_branch(branch, indent=0):
    for item in branch:
        if type(item) is str or type(item) is unicode:
            print(" "*indent + item)
        else:
            print("-" * (indent+1))
            print_branch(item, indent+1)

def file_output(branch, filename="/tmp/outfile"):
    with open(filename, "w") as f:
        json.dump(branch, f)

def file_input(filename="/tmp/outfile"):
    with open(filename, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    root = input_branch()
    print_branch(root)
    file_output(root)

    read_new = file_input()
    print_branch(read_new)
