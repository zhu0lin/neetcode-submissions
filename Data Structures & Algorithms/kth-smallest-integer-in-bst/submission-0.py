# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Understand:
        Input: The root of a BST and an integer k
        Output: The kth smallest value in the BST

        Plan:
        DFS inorder traversal
        Keep a counter for the element that we're on in the inorder
        traversal. When we reach the kth element, return that element's value
        """
        count = 0
        seen = []

        def inorder(root):
            nonlocal count
            nonlocal seen

            if not root:
                return 

            if root.left:
                val = inorder(root.left)
                if val is not None:
                    return val

            if root:
                count += 1
                seen.append(root.val)
                if count == k:
                    return seen[len(seen)-1]

            if root.right:
                val = inorder(root.right)
                if val is not None:
                    return val

        return inorder(root)
                