class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        equivalent_number = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
                """
                If the current letter is smaller (in value) than the next letter, subtract its value from the total 
                """
                equivalent_number -= roman_dict[s[i]]
            else:
                """
                If the current letter is bigger (in value) than the next letter, add its value from the total 
                """
                equivalent_number += roman_dict[s[i]]

        return equivalent_number
