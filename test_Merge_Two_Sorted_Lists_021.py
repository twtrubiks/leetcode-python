import unittest
from Merge_Two_Sorted_Lists_021 import ListNode, Solution

'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


class Test_Case(unittest.TestCase):

    def test_answer_01(self):
        #  L1 = 1 -> 2 -> 4
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)
        #  L2 = 1 -> 3 -> 4
        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)
        actual = Solution().mergeTwoLists(l1, l2)

        # expected result  1->1->2->3->4->4
        expected = ListNode(1)
        expected.next = ListNode(1)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(3)
        expected.next.next.next.next = ListNode(4)
        expected.next.next.next.next.next = ListNode(4)

        self.assertEqual(actual.val, expected.val)
        self.assertEqual(actual.next.val, expected.next.val)
        self.assertEqual(actual.next.next.val, expected.next.next.val)
        self.assertEqual(actual.next.next.next.val, expected.next.next.next.val)
        self.assertEqual(actual.next.next.next.next.val, expected.next.next.next.next.val)
        self.assertEqual(actual.next.next.next.next.next.val, expected.next.next.next.next.next.val)
        self.assertEqual(actual.next.next.next.next.next.next, expected.next.next.next.next.next.next)


if __name__ == '__main__':
    unittest.main()
