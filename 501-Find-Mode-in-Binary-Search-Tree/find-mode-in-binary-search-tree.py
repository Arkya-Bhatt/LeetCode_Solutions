from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = []
        prev_val = None
        curr_val = 0
        max_freq = 0

        def inorder_traversal(node: Optional[TreeNode]) -> None:
            nonlocal prev_val, curr_val, max_freq, modes
            if node is None:
                return
            inorder_traversal(node.left)
            if node.val == prev_val:
                curr_val += 1
            else:
                curr_val = 1
            if curr_val > max_freq:
                max_freq = curr_val
                modes = [node.val]
            elif curr_val == max_freq:
                modes.append(node.val)
            prev_val = node.val
            inorder_traversal(node.right)
        inorder_traversal(root)
        return modes
        