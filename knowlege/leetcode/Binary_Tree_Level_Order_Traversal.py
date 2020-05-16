'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.height = 0
        self.tree = [[]]
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        self.travesal(root,0)
        return self.tree
        
        
    def travesal(self, node, level):
        if node == None:
            return 
        else:
            if level <= self.height:
                self.tree[level].append(node.val)
                
            else:
                self.height+=1
                self.tree.append([node.val])
            self.travesal(node.left,level+1)
            self.travesal(node.right,level+1)
            
            
