# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Understand:
        Input: The root of a binary tree 
        Output: A nested list, where the inner lists are the nodes
        at each level of the binary tree
        
        Plan:
        BFS approach with helper function

        """
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            level = []

            for _ in range(level_size):
                popped = q.popleft()
                level.append(popped.val)

                if popped.left:
                    q.append(popped.left)
                        
                if popped.right:
                    q.append(popped.right)

            res.append(level)

        return res

            
