#!/usr/bin/env python

import itertools as it

def even_numbers():
    i = 0
    while True:
        i += 2
        yield i

def fib_seq():
    i, j = 0,1
    while True:
        i, j = j, i+j
        yield i

def prime_seq():
    cur = 2
    while True:
        yield cur
        cur += 1
        while not_prime(cur):
            cur += 1




def not_prime(val):
    for i in range(2,val):
        if val % i == 0:
            return True
    return False



if __name__ == "__main__":
    even_gen = even_numbers()
    fib_gen = fib_seq()
    prime_gen = prime_seq()

    first_10_evens = [i for i, _ in zip(even_gen,range(10))] 
    first_10_fibon = [next(fib_gen) for _ in range(10)]
    first_10_prime = zip(*zip(prime_seq(), range(10)))[0]

    print("First ten values of each set:")
    print("Evens: {}".format(first_10_evens))
    print("Prime: {}".format(first_10_prime))
    print("Fibon: {}".format(first_10_fibon))

    raw_input("Press ENTER to continue")

    cur_spot = 0
    while True:
        cur_spot += 10
        print("Values {} to {} of each set:".format(cur_spot, cur_spot+10))
        print("Evens: {}".format(list(it.islice(even_gen, 10))))
        print("Prime: {}".format(list(it.islice(prime_gen, 10))))
        print("Fibon: {}".format(list(it.islice(fib_gen, 10))))
