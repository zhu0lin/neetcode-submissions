# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Understand:
        Input: The root of a binary tree
        Output: The amount of "good nodes" in the binary tree.
        A good node is defined to a node such that there is no node from 
        the root of the tree to the good node that has a larger value than
        that good node. 
        i.e. the path to that node doesnt have a node that has val greater
        The root itself counts as a good node b/c it doesnt have any
        nodes before it 

        Plan:
        DFS approach
        """
        res = 0

        def dfs(root, tracker):
            nonlocal res
            if not root: 
                return 

            if root.val >= tracker:
                res += 1
                tracker = root.val

            if root.left:
                dfs(root.left, tracker)

            if root.right:
                dfs(root.right, tracker)

        dfs(root, float('-inf'))
        return res

