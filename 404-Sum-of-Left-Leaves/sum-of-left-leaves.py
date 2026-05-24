from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def is_leaf(node):
            return not node.left and not node.right
        
        total = 0
        
        if root.left:
            if is_leaf(root.left):
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)
        
        if root.right:
            total += self.sumOfLeftLeaves(root.right)
        
        return total
        