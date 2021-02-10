'''
Reverse a singly linked list.

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pass







# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         prev = None
#         while head:
#             temp = head.next
#             head.next = prev
#             prev = head
#             head = temp
#         return prev






# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         newHead = None ;
#         while head:
#             nextNode = head.next ;
#             head.next = newHead ;
#             newHead = head ;
#             head = nextNode ;
#         return newHead ;


if __name__=="__main__":

    #print Solution().reverseList(head)
