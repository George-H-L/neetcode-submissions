# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #use recursion for sure, can replicate logic at each node. we need to check essentialy if the current value
        # of the root node is equal, and then if the node.left and node.right values are equal, this can the be called recursively.
        if not p and not q:
            return True
        
        
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
        else:
            return False
        


            