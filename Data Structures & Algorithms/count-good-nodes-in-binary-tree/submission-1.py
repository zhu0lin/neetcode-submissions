# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, val):
            nonlocal res
            if not root:
                return

            if root.val >= val:
                res += 1
                val = root.val

            if root.left:
                dfs(root.left, val)

            if root.right:
                dfs(root.right, val)

        dfs(root, float('-inf'))
        return res