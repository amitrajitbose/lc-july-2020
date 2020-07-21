class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            if i == 0 and digits[i] == 9:
                digits.insert(0,1)
                digits[i+1] = 0
                return digits
            else:
                digits[i] = 0
                i -= 1
        return digits

