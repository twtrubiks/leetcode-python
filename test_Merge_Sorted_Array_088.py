import unittest
from Merge_Sorted_Array_088 import Solution

'''
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):

        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3

        result = [1,2,2,3,5,6]

        self.assertEqual(Solution().merge(nums1, m, nums2, n), result)


    def test_answer_02(self):

        nums1 = [2,0]
        m = 1
        nums2 = [1]
        n = 1

        result = [1,2]

        self.assertEqual(Solution().merge(nums1, m, nums2, n), result)


if __name__ == '__main__':
    unittest.main()
