def checkDirection(n, g):
    l = (g * (g+1))//2
    m = ((g+1) * (g+2))//2
    if l <= n and m > n:
        return 0
    elif l <= n:
        return 1
    return 2

class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            x = checkDirection(n, mid)
            if x == 0:
                return mid
            if x == 1:
                low = mid + 1
            else:
                high = mid - 1
        return low


"""
Time = O(log(n))
Space = O(1)
"""

