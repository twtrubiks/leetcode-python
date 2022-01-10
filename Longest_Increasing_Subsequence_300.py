from typing import List

"""
Input: nums = [10,9,2,5,3,7,101,18]
[2,3,7,101]
Output: 4

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""


class Solution_DP:
    # 忘記可參考 https://www.youtube.com/watch?v=l2rCz7skAlk
    # DP = 動態規劃
    # 複雜度爲O(n*n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class Solution_BinarySearch:
    # 忘記可參考 https://www.youtube.com/watch?v=l2rCz7skAlk
    # DP + BinarySearch

    # 步驟
    # 將第1個數字加入解集；

    # 依次讀取後面的數字，如果此數字比解集中最後一個數字大，則將此數字追加到解集後，
    # 否則，用這個數字替換解集中第一個比此數字大的數，解集是有序的，因此查找可以用二分法，
    # 複雜度O(log n)；

    # 最後的答案是解集的長度（而解集中保存的並不一定是合法解）。

    # 複雜度爲O(n*n)
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0
        rst = [nums[0]]
        for i in range(1, n):
            if nums[i] > rst[-1]:
                rst.append(nums[i])
            else:
                index = self.binarySearch(rst, nums[i])
                rst[index] = nums[i]
        return len(rst)

    def binarySearch(self, seqs, target):
        left = 0
        right = len(seqs) - 1
        while left <= right:
            m = (left + right) // 2

            if seqs[m] > target:
                right = m - 1
            elif seqs[m] < target:
                left = m + 1
            else:
                return m
        return left


import bisect


class Solution_bisect:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        rst = []
        for x in nums:
            i = bisect.bisect_left(rst, x)
            if i == len(rst):
                rst.append(x)
            else:
                rst[i] = x
        return len(rst)
