# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = deque([root])
        depth = 0
        while d:
            level_size = len(d)
            for _ in range(level_size):
                node = d.popleft()
                if node.left:  d.append(node.left)
                if node.right: d.append(node.right)
            depth += 1
        return depth

                
        

        