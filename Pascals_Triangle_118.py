
'''
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []

        stack = [1]
        result = [stack]

        for i in range(1, numRows):
            temp = [stack[s-1] + stack[s]  for s in range(1, i)]
            stack = [1] + temp + [1]
            result.append(stack)

        return result
