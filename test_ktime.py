#!/usr/bin/env python

"""Tests for ktime"""

import unittest

import ktime.time as ktime

class KtimeTestCase(unittest.TestCase):

    def test_gmtime_epoch(self):
        r = ktime.gmtime(0)
        self.assertEqual(ktime.gmtime(0), (1970, 1, 1, 0, 0, 0, 3, 1, 0))
        self.assertEqual(ktime.gmtime(0), (1970, 1, 1, 0, 0, 0, 3, 1, 0))
        self.assertEqual(ktime.gmtime(1370304000), (2013, 6, 4, 0, 0, 0, 1, 155, 0))
        self.assertEqual(ktime.gmtime(949378899), (2000, 2, 1, 4, 21, 39, 1, 32, 0))

if __name__ == '__main__':
    unittest.main()