# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        U:
        Input: 
        Head of a linked list head
        An integer n
        
        P:
        Three pointer approach: prev, curr, next
        
        """

        # if head and n == 1:
        #     return 0
            
        curr = head
        nodes = 0
        while(curr):
            nodes += 1
            curr = curr.next

        
        remove = nodes - n
        if remove == 0:
            return head.next

        prev = None
        curr = head
        i = 0
        while(i < remove):
            prev = curr
            curr = curr.next
            i += 1

        prev.next = curr.next
        return head
        
