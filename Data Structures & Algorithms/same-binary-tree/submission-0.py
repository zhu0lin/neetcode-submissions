# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Understand:
        Input: Roots of two binary trees p and q
        Output: True if the trees are equivalent, otherwise False
        Two trees are equivalent if they have the exact same structure
        and the nodes have the same values.

        Plan:
        DFS approach:

        """
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return True if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) else False
        