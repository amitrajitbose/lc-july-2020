class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n <= -(2**31):
            return 0 if abs(x) != 1 else 1
        if n < 0:
            return 1/(x ** abs(n))
        return x ** n

