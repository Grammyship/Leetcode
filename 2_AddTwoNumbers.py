"""
2. Add Two Numbers
Time Submitted: 07/25/2021 00:40
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans_tail = ans
        temp = 0
        
        while l1 or l2 or temp:
            val1 = ( l1.val if l1 else 0 )
            val2 = ( l2.val if l2 else 0 )
            ( temp , rem ) = divmod( val1 + val2 + temp , 10 )
            
            ans_tail.next = ListNode( rem )
            ans_tail = ans_tail.next
            
            l1 = ( l1.next if l1 else None )
            l2 = ( l2.next if l2 else None )
            
        return ans.next