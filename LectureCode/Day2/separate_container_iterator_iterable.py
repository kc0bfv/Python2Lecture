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
    """ The container class - returns an iterator cur_prime """
    def __init__(self, stop_pt):
        self.start = 1
        self.stop_pt = stop_pt

    def __iter__(self):
        return cur_prime(self.start, self.stop_pt)


class cur_prime(object):
    """ The iterator class - returns a new prime on each next """
    def __init__(self, start, stop_pt):
        self.stop_pt = stop_pt
        self.cur = find_next_prime(start, self.stop_pt)

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
    
