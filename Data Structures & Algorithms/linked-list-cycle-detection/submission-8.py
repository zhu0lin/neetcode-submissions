# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        U:
        Input: The head of a linked list, in which the list might 
        have a cycle
        P:
        Two ptr approach: slow and fast ptr
        Slow ptr starts at head, fast ptr starts at head.next.next
        Keep cycling until either slow = fast or
        fast is None
        """

        slow = head
        fast = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            

        return False