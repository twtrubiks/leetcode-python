import unittest
from Nim_Game_292 import Solution

"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

Example 1:

Input: n = 4
Output: false

Example 2:

Input: n = 1
Output: true

Example 3:

Input: n = 2
Output: true
"""


class Test_Case(unittest.TestCase):
    def test_answer_01(self):
        n = 4
        result = False
        self.assertEqual(Solution().canWinNim(n), result)

    def test_answer_02(self):
        n = 1
        result = True
        self.assertEqual(Solution().canWinNim(n), result)

    def test_answer_03(self):
        n = 2
        result = True
        self.assertEqual(Solution().canWinNim(n), result)


if __name__ == "__main__":
    unittest.main()
