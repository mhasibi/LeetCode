class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > -1:
            length = len((num_str := str(x)))
            reversed_num = ''
            for i in range(1,length+1):
                reversed_num += num_str[-i]
            return True if reversed_num == num_str else False
        return False
