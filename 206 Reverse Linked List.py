'''
Reverse a singly linked list.

Runtime: 44 ms
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None ;
        while head:
            nextNode = head.next ;
            head.next = newHead ;
            newHead = head ;
            head = nextNode ;
        return newHead ;

            
if __name__=="__main__":
    
    #print Solution().reverseList(head)             
