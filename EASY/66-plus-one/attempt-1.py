class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if (plus_one := digits[-1] + 1) > 9 :
            digits[-1] = (plus_one) // 10
            digits.append((plus_one) % 10)
        else:
            digits[-1] += 1
        return digits