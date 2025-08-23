from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        l1, l2 = len(nums1), len(nums2)
        res = []

        while i < l1 and j < l2:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 < id2:
                res.append([id1, val1])
                i += 1
            
            elif id1 > id2:
                res.append([id2, val2])
                j += 1

            else:
                res.append([id1, val1+val2])
                i += 1
                j += 1
        
        while i < l1:
            res.append(nums1[i])
            i += 1
        
        while j < l2:
            res.append(nums2[j])
            j += 1

        return res
        