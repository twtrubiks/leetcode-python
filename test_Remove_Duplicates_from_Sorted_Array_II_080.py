import unittest
from Remove_Duplicates_from_Sorted_Array_II_080 import *

class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        nums = [1,1,1,2,2,3]
        result = 5
        self.assertEqual(Solution().removeDuplicates(nums), result)

    def test_answer_02(self):
        nums = [0,0,1,1,1,1,2,3,3]
        result = 7
        self.assertEqual(Solution().removeDuplicates(nums), result)
