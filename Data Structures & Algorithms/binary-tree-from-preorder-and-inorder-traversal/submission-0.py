# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Understand:
        Input: An array of integers preorder and an array of integers 
        inorder. These arrays are the same size, and they consist entirely
        of unique values.
        Output: The root of the binary tree built from the preorder and
        inorder traversals

        Plan:
        Note that this looks like a BST
        Observe that the inorder traversal divides the array into two 
        halves: the left part is the left subtree and the right part is 
        the right subtree. To find the index of the root node in the 
        inorder array, use inorder.index(preorder[0])

        Iterate over the preorder array, first we make the first value 
        the root of the tree. 
        After, we check if the value is on the left subtree, by checking
        if it's index is less than the index of the root node in the inorder
        array. 
        Otherwise, the value must be on the right subtree.

        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root