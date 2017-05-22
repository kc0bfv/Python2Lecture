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


class iter_primes(object):
    """ The iterator and container class - returns a new prime on each next """
    def __init__(self, stop_pt):
        self.stop_pt = stop_pt
        self.cur = find_next_prime(1, self.stop_pt)

    def __iter__(self):
        return self

    def next(self):
        if self.cur is None:
            raise StopIteration

        self.cur = find_next_prime(self.cur + 1, self.stop_pt)

        if self.cur is None:
            raise StopIteration

        return str(self.cur)


if __name__ == "__main__":
    print [prime for prime in iter_primes(1000)]
    
