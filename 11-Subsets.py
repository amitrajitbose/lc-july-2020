class Solution:
    def __init__(self):
        self.res = []
    def dfs(self, arr, i, tmp):
        if len(arr) == i:
            self.res.append(tmp)
        else:
            self.dfs(arr, i+1, tmp)
            self.dfs(arr, i+1, tmp + [arr[i]])
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums, 0, [])
        return self.res


