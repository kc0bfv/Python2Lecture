#!/usr/bin/env python

from __future__ import print_function

def try_x(x):
    all_strs = [(i,j,k) for i in range(26) for j in range(26) 
            for k in range(26)]
    all_sums = [(sum(vals), vals) for vals in all_strs]
    div_strs = [vals for (v_sum, vals) in all_sums if v_sum % x == 0]
    as_letrs = [(chr(v+ord("a")) for v in vals) for vals in div_strs]
    for_prnt = ["".join(vals) for vals in as_letrs]
    return for_prnt


print(try_x(73))

print([try_x(i) for i in range(10,100,10)])

print([i for i in range(1,100) if len(try_x(i)) < 10])

print([len(try_x(i)) for i in range(1,100)])
