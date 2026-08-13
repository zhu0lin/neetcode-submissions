# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Understand:
        Input: The root of a binary tree
        Output: A list of the right node values in each subtree

        Plan:
        BFS approach
        At each level of BFS, append the last element (it will be the
        right most node)
        """
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)

            for i in range(level_size):
                popped = q.popleft()
                if i+1 == level_size:
                    res.append(popped.val)

                if popped.left:
                    q.append(popped.left)
                        
                if popped.right:
                    q.append(popped.right)

        return res