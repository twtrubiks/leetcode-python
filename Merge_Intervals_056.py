
'''
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        result = []
        intervals.sort()

        for i in range(len(intervals)):
            if result and result[-1][1] >= intervals[i][0]:
                if result[-1][1] < intervals[i][1]:
                    result[-1][1] = intervals[i][1]
                continue
            result.append(intervals[i])
        return result