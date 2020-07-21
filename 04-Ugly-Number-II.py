class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0]*n
        ugly[0] = 1
        p2, p3, p5 = 0, 0, 0
        cnt = 1
        while cnt < n:
            n2, n3, n5 = ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5
            minn = min(n2, n3, n5)
            if n2 == minn:
                p2 += 1
            if n3 == minn:
                p3 += 1
            if n5 == minn:
                p5 += 1
            ugly[cnt] = minn
            cnt += 1
        # print(ugly)
        return ugly[-1]

