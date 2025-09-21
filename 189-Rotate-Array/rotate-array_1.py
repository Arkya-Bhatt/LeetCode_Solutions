from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        rotated_arr = [0] * n
        rotated_arr[:k] = nums[n-k:]
        rotated_arr[k:] = nums[:n-k]
        nums[:] = rotated_arr
