import unittest
from Count_and_Say_038 import *

'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

The following are the terms from n=1 to n=10 of the count-and-say sequence:
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        n = 1
        result = '1'
        self.assertEqual(Solution().countAndSay(n), result)

    def test_answer_02(self):
        n = 2
        result = '11'
        self.assertEqual(Solution().countAndSay(n), result)

    def test_answer_03(self):
        n = 3
        result = '21'
        self.assertEqual(Solution().countAndSay(n), result)

    def test_answer_04(self):
        n = 4
        result = '1211'
        self.assertEqual(Solution().countAndSay(n), result)

    def test_answer_05(self):
        n = 5
        result = '111221'
        self.assertEqual(Solution().countAndSay(n), result)

    def test_answer_06(self):
        n = 6
        result = '312211'
        self.assertEqual(Solution().countAndSay(n), result)

    def test_answer_07(self):
        n = 7
        result = '13112221'
        self.assertEqual(Solution().countAndSay(n), result)

    def test_answer_08(self):
        n = 8
        result = '1113213211'
        self.assertEqual(Solution().countAndSay(n), result)

    def test_answer_09(self):
        n = 9
        result = '31131211131221'
        self.assertEqual(Solution().countAndSay(n), result)

    def test_answer_10(self):
        n = 10
        result = '13211311123113112211'
        self.assertEqual(Solution().countAndSay(n), result)


if __name__ == '__main__':
    unittest.main()
