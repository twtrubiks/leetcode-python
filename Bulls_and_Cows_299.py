'''
Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

Example 3:

Input: secret = "1", guess = "0"
Output: "0A0B"

Example 4:

Input: secret = "1", guess = "1"
Output: "1A0B"

'''
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        result_A = 0
        result_B = 0
        A = []
        B = []

        for i in range(len(secret)):
          if secret[i] == guess[i]:
            result_A += 1
          else:
            A.append(secret[i])
            B.append(guess[i])

        if result_A == 0 :
          A = [i for i in secret]
          B = [i for i in guess]

        for i in range(len(A)):
          if A[i] in B:
            result_B += 1
            B.remove(A[i])

        return '{}A{}B'.format(result_A, result_B)


