class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resp = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            seen = set([])
            j = i+1
            while j < len(nums):
                if (-nums[i]-nums[j]) in seen:
                    resp.append(sorted([nums[i], nums[j], -nums[i]-nums[j]]))
                    while j+1 < len(nums) and nums[j]==nums[j+1]:
                        j += 1
                seen.add(nums[j])
                j += 1
        return resp

"""
Time : O(n^2)
Space: O(n)
"""

