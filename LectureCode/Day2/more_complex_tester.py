#!/usr/bin/env python

import unittest

from to_test import multiply, add, subtract

TYPES = {"raises": 0, "equals": 1}

class skip_this:
    class mult_add_sub_tester(unittest.TestCase):
        def run_test(self, assert_type, result, func):
            if assert_type == TYPES["raises"]:
                self.assertRaises(result, func, self.one, self.two)
            elif assert_type == TYPES["equals"]:
                self.assertEquals(result, func(self.one, self.two))
            else:
                raise RuntimeError("Unknown assert_type")

        def test_multiply(self):
            self.run_test(self.mult_assert, self.mult_result, multiply)

        def test_add(self):
            self.run_test(self.add_assert, self.add_result, add)

        def test_subtract(self):
            self.run_test(self.sub_assert, self.sub_result, subtract)

class test_list(skip_this.mult_add_sub_tester):
    one = [1,2,3]
    two = [4,5,6]
    mult_assert, mult_result = TYPES["raises"], TypeError
    add_assert, add_result = TYPES["equals"], [1,2,3,4,5,6]
    sub_assert, sub_result = TYPES["raises"], TypeError

class test_str(skip_this.mult_add_sub_tester):
    one = "First "
    two = "second"
    mult_assert, mult_result = TYPES["raises"], TypeError
    add_assert, add_result = TYPES["equals"], "First second"
    sub_assert, sub_result = TYPES["raises"], TypeError

class test_int(skip_this.mult_add_sub_tester):
    one = 1
    two = 2
    mult_assert, mult_result = TYPES["equals"], 2
    add_assert, add_result = TYPES["equals"], 3
    sub_assert, sub_result = TYPES["equals"], -1

class test_set(skip_this.mult_add_sub_tester):
    one = {1,2,3,4,5}
    two = {4,5,6,7,8}
    mult_assert, mult_result = TYPES["raises"], TypeError
    add_assert, add_result = TYPES["raises"], TypeError
    sub_assert, sub_result = TYPES["equals"], {1,2,3}

if __name__ == "__main__":
    unittest.main()
