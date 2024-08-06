class Solution:
    def isValid(self, s: str) -> bool:
        if not s or not len(s):
            return True

        matching_brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        input = []
        for char in s:
            print(f"char = {char}")
            if char in matching_brackets:
                top_element = input.pop() if input else '#'
                print(f"top_element = {top_element}")
                if top_element != matching_brackets[char]:
                    return False
            else:
                print(f"appending {char} to input")
                input.append(char)
        return not input

