# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Understand
        Input: The root of a binary tree
        Output: True if the binary tree is valid (i.e. left children 
        has value less than curr node and right children has value greater
        than curr node), else False.

        Plan: BFS approach

        """

        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            node, lower, upper = q.popleft()
            if not (lower < node.val < upper):
                return False

            if node.left:
                q.append((node.left, lower, node.val))

            if node.right:
                q.append((node.right, node.val, upper))

        return True


        
