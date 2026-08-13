# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        U:
        Input: 
        The head of two sorted linked lists, list1 and list2
        P:
        Two ptr approach
        l1 ptr points to head of list1, l2 ptr points to head of list2
        Compare l1.val and l2.val
        Move either l1 or l2 forward depending on which one is smaller
        If l1.val == l2.val, add them to the new list
        and move them both forward

        At end, iterate over l1 and l2 (to manage case where 
        l1 is longer than l2 or l2 is longer than l1)
        """
        l1 = list1
        l2 = list2
        dummy = ListNode()
        tail = dummy
        while(l1 and l2):

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        
        return dummy.next

