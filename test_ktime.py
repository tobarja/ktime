#!/usr/bin/env python

"""Tests for ktime"""

import unittest

import ktime.time as ktime

class KtimeTestCase(unittest.TestCase):

    def test_gmtime_epoch(self):
        self.assertEqual(ktime.gmtime(0), (1970, 1, 1, 0, 0, 0, 3, 1, 0))

    def test_gmtime_midnight_the_first_day(self):
        self.assertEqual(ktime.gmtime(1370304000), (2013, 6, 4, 0, 0, 0, 1, 155, 0))

    def test_gmtime_leap_years(self):
        self.assertEqual(ktime.gmtime(949378899), (2000, 2, 1, 4, 21, 39, 1, 32, 0))
        self.assertEqual(ktime.gmtime(951847262), (2000, 2, 29, 18, 1, 2, 1, 60, 0))
        self.assertEqual(ktime.gmtime(951880205), (2000, 3, 1, 3, 10, 5, 2, 61, 0))

    def test_gmtime_before_epoch(self):
        self.assertEqual(ktime.gmtime(-1), (1969, 12, 31, 23, 59, 59, 2, 365, 0))
        self.assertEqual(ktime.gmtime(-86400), (1969, 12, 31, 0, 0, 0, 2, 365, 0))
        self.assertEqual(ktime.gmtime(-15715382400), (1472, 1, 1, 0, 0, 0, 0, 1, 0))
        self.assertEqual(ktime.gmtime(-15709437204), (1472, 3, 9, 19, 26, 36, 5, 69, 0))

if __name__ == '__main__':
    unittest.main()
