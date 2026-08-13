# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Understand:
        Input: Roots of two binary trees root and subRoot.
        Output: True if there exists a subtree in root that is the same
        as the tree of subRoot (same structure and node values)

        Plan:
        DFS approach

        Base cases:
        if not root and not selfRoot:
            return True

        if root.val == subRoot.val:
            recursively iterate over left and right subtrees to 
            confirm there is a subtree in the root tree that has
            exact same structure and node values as subRoot tree 
        """

        def dfs(root, subRoot):

            if not root and not subRoot:
                return True

            if not root or not subRoot:
                return False

            if root.val != subRoot.val:
                return False

            return True if dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right) else False

        if not root: 
            return False
        
        if dfs(root, subRoot) == True:
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
            

