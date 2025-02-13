# Copyright (c) 2018 luozhouyang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unittest

from .weighted_levenshtein import WeightedLevenshtein


class TestWeightedLevenshtein(unittest.TestCase):

    def test_weighted_levenshtein(self):
        a = WeightedLevenshtein()
        s0 = ""
        s1 = ""
        s2 = "上海"
        s3 = "上海市"
        distance_format = "distance: {:.4}\t between {} and {}"
        print(distance_format.format(str(a.distance(s0, s1)), s0, s1))
        print(distance_format.format(str(a.distance(s0, s2)), s0, s2))
        print(distance_format.format(str(a.distance(s0, s3)), s0, s3))
        print(distance_format.format(str(a.distance(s1, s2)), s1, s2))
        print(distance_format.format(str(a.distance(s1, s3)), s1, s3))
        print(distance_format.format(str(a.distance(s2, s3)), s2, s3))

    def test_weighted_levenshtein_func(self):
        def isnum(x):
            return '0' <= x <= '9'

        def pr(a, s1):
            s0 = "SB012345"
            distance_format = "distance: {:.4}\t between {} and {}"
            print(distance_format.format(str(a.distance(s0, s1)), s0, s1))

        a = WeightedLevenshtein()

        def deletion_cost(char, pos, l):
            if pos < 3 and not isnum(char):
                return 0.3
            if pos == (l - 1) and isnum(char):
                return 0.3
            return 1.0

        a.deletion_cost_fn = deletion_cost

        def insertion_cost(char, pos):
            if pos < 3:
                return 0.3
            return 1.0

        a.insertion_cost_fn = insertion_cost

        def subs_cost(ch1, ch2, pos):
            if pos > 3 and isnum(ch1) and isnum(ch2):
                return .4
            return 1.0

        a.substitution_cost_fn = subs_cost
        pr(a, "SB012345")
        pr(a, "012345")
        pr(a, "SB01234")
        pr(a, "SB01134")
        pr(a, "SB0123456")


if __name__ == "__main__":
    unittest.main()
