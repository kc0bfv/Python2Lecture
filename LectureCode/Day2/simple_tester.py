#!/usr/bin/env python

import unittest

from to_test import add, multiply, subtract

class try_tests(unittest.TestCase):
    def test_uno(self):
        self.assertEquals(multiply(4,3), 12)
        self.assertEquals(multiply(9,15), 135)
        self.assertEquals(multiply("asdf", 4), "asdfasdfasdfasdf")

    def test_dos(self):
        self.assertAlmostEqual(multiply(5.0, 3.1394), 15.697, 6)
        self.assertEqual(add(5.1, 3.1394), 8.2394)

if __name__ == "__main__":
    unittest.main()
