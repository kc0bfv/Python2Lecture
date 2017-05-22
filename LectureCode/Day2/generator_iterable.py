#!/usr/bin/env python

def is_prime(val):
    for i in range(2, val):
        if val % i == 0:
            return False
    return True

def find_next_prime(val, stop_pt):
    if is_prime(val):
        return val
    else:
        for i in range(val+1, stop_pt):
            if is_prime(i):
                return i
        return None


def yield_primes(stop_pt):
    cur = 1
    while cur < stop_pt:
        cur = find_next_prime(cur + 1, stop_pt)
        if cur is None:
            return
        yield str(cur)


if __name__ == "__main__":
    print [prime for prime in yield_primes(1000)]
    
