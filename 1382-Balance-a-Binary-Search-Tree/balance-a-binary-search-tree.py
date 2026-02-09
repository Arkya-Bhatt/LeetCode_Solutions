from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        def build_balancedBST(lo: int, hi: int) -> TreeNode:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])
            node.left = build_balancedBST(lo, mid - 1)
            node.right = build_balancedBST(mid + 1, hi)
            return node
        nums = inorder(root)
        return build_balancedBST(0, len(nums) - 1)
        