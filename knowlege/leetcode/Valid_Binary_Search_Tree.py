'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

(1)The left subtree of a node contains only nodes with keys less than the node's key.
(2)The right subtree of a node contains only nodes with keys greater than the node's key.
(3)Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            res = True
            if root.left and root.left.val >= root.val:
                res = False
            if root.right and root.right.val <= root.val:
                res = False
            res = res and self.isValidBST(root.left) and self.isValidBST(root.right)
            return res
            
