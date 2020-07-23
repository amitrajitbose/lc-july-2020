class Solution:
    def xorAll(self, arr):
        res = arr[0]
        for i in range(1, len(arr)):
            res ^= arr[i]
        return res
    def singleNumber(self, nums: List[int]) -> List[int]:
        # first traversal - get differing bit
        xor = self.xorAll(nums)
        pos = 1
        while xor & pos == 0:
            pos <<= 1
        # splitting into two buckets
        a, b = 0, 0
        for i in nums:
            if i & pos == 0:
                a ^= i
            else:
                b ^= i
        return [a, b]

"""
Runtime : Linear (Two traversals)
Space: Constant
"""

