from typing import List, Optional

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = deque([root])
        left_to_right = True
        while q:
            len_q = len(q)
            curr_lvl = deque()
            for _ in range(len_q):
                node = q.popleft()
                if left_to_right:
                    curr_lvl.append(node.val)
                else:
                    curr_lvl.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(list(curr_lvl))
            left_to_right = not left_to_right
        return res
        