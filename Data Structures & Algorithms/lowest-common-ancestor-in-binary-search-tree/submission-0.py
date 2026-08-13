# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Understand:
        Input: A binary search tree given by root. Two nodes from the 
        tree p and q. p will not be equal to q. 
        Output: The lowest common ancestor of the two nodes p and q. The 
        lowest common ancestor can be p or q itself.

        Plan:
        BFS approach:
        Once p and q are both in visited, we check the lowest
        common ancestor using the visited array

        Problem: How can we recognize the true lowest common ancestor
        based on the visited array? I.e. how can I cover the case of
        the lowest ancestor being either p or q
        """
        # def bfs(root, p, q):
        #     if not root:
        #         return []

        #     visited = []
        #     q = deque([root])  

        #     while q or (p in visited and q in visited):
        #         current_node = q.popleft()  
        #         visited.append(current_node.val)  

        #         if current_node.left:
        #             q.append(current_node.left)

        #         if current_node.right:
        #             q.append(current_node.right)

        #     return visited

        # arr = bfs(root, p, q)
        # idx = arr.index(p.val)

        # lowest = float('inf')
        # for i in range(idx+1):
        #     if arr[i] < lowest:
        #         lowest = arr[i]

        # return TreeNode(lowest)
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr


        
