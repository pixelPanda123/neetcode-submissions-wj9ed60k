# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def check(self, root, sub):
            if not root and not sub: 
                return True 
            if root and sub and root.val == sub.val: 
                return self.check(root.left, sub.left) and self.check(root.right, sub.right) 
            else: 
                return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: 
            return True 
        if not root: 
            return False
        if self.check(root, subRoot): 
            return True 
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) 
        

        
            