# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        U:
        Input: The head of a singly linked list
        P:
        Slow and fast ptr to identify midpoint of linked list
        Iterate over left half
        Reverse right half
        Iterate over both of them, adding left node, then right node
        until we run out of nodes in both halves
        """
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        
