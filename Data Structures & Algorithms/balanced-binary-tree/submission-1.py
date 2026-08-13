# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Understand:
        Input: The root of a binary tree
        Output: True if the tree is height balanced and false otherwise.
        A tree is height balanced is the heights of the left and right subtrees
        differ by no more than 1

        Plan:
        Base case: If not root, return 0
        Recursive calls: Use DFS to get height of left and right
        subtrees. 
        """
        
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            return -1 if abs(left-right) > 1 or left == -1 or right == -1 else 1 + max(left, right)

        return False if dfs(root) == -1 else True
