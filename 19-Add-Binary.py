class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        res = ''
        carry = 0
        while i>=0 or j>=0:
            summ = carry
            carry = 0
            if i>=0:
                summ += int(a[i])
                i -= 1
            if j>=0:
                summ += int(b[j])
                j -= 1
            if summ > 1:
                carry = 1
                summ -= 2
            res += str(summ)
        if carry:
            res += str(carry)
        return res[::-1]
    
"""
Runtime: max(len(a), len(b))
Space: max(len(a), len(b))
"""

