"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = deque()
        deep_copy = {node: Node(node.val)}

        q.append(node)
        
        while q:
            popped_node = q.popleft()
            
            for neighbor in popped_node.neighbors:
                if neighbor not in deep_copy:
                    deep_copy[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                deep_copy[popped_node].neighbors.append(deep_copy[neighbor])


        return deep_copy[node]