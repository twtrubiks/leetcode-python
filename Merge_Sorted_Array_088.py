
'''
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1

class SolutionBubbleSort1(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = nums2[:n]
        s_len = m + n

        while s_len > 1:
            s_len -= 1
            for i in range(s_len):
                if nums1[i] > nums1[i+1]:
                    nums1[i], nums1[i+1] = nums1[i+1], nums1[i]
        return nums1

class SolutionBubbleSort2(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = nums2[:n]

        for j in range(m+n-1, 0, -1):
            for i in range(j):
                if nums1[i] > nums1[i+1]:
                    nums1[i], nums1[i+1] = nums1[i+1], nums1[i]
        return nums1