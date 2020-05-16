'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
'''

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root is None):
            return None
        if(root.val==p.val or root.val==q.val):
            #print(root.val)
            return root
        else:
            root1=root2=None
            root1=self.lowestCommonAncestor(root.right,p,q)
            root2=self.lowestCommonAncestor(root.left,p,q)
            if(root1 is None and root2 is None):
                return None
            elif(root1 is not None and root2 is not None):
                return root
            else:
                return root2 if root1 is None else root1
