"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Understand
        Input: The head of a linked list. Each node in the linked list
        has a val, a next pointer, and a random pointer. The random
        pointer value is the index of that node.
        Output: The head of a linked list. Each node should have it's
        value, should have a next pointer, should have a random pointer
        that points to node at random ptr index.

        Plan:
        Brute force: ???
        Initialize empty array
        Go through the linked list, adding each node's value and it's random ptr index
        as a tuple to the array.
        Go through the array, forming a linked list along the way. Adding 
        the random ptr by looking at tuple[0] for every node.
        Return head of deep copy of linked list
        """
        if not head:
            return None

        deep_copy = {}

        curr = head
        while(curr):
            deep_copy[curr] = Node(curr.val)
            curr = curr.next

        # deep_copy looks something like
        # [(1, null), (2,2), (3,2)]

        new_head = deep_copy[head] # return new_head at end
        curr = head
        while curr:
            deep_copy[curr].next = deep_copy.get(curr.next)
            deep_copy[curr].random = deep_copy.get(curr.random)
            curr = curr.next
            
        return new_head
