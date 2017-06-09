#!/usr/bin/env python

from __future__ import print_function

def process_line(val):
    """Turn a line out of a file into a list of permitted character indices"""
    index = [ord(v)-ord("a") for v in val]
    return [val for val in index if 0 <= val < 26]

def try_x(x):
    with open("/usr/share/dict/words") as f:
        dict_vals = [line for line in f]
    all_strs = [process_line(val) for val in dict_vals]
    all_sums = [(sum(vals), vals) for vals in all_strs]
    div_strs = [vals for (v_sum, vals) in all_sums if v_sum % x == 0]
    as_letrs = [(chr(v+ord("a")) for v in vals) for vals in div_strs]
    for_prnt = ["".join(vals) for vals in as_letrs]
    return for_prnt


#print(try_x(73))

#print([try_x(i) for i in range(10,100,10)])

#print([i for i in range(1,100) if len(try_x(i)) < 10])

print([len(try_x(i)) for i in range(1,100)])
