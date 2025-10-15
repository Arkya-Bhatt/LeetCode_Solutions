from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stk = [(root, float("-inf"), float("inf"))]
        while stk:
            node, min_val, max_val = stk.pop()
            if node.val <= min_val or node.val >= max_val:
                return False
            else:
                if node.left:
                    stk.append((node.left, min_val, node.val))
                if node.right:
                    stk.append((node.right, node.val, max_val))
        return True
