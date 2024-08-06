class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        """
            Start with the first string in the array as the initial prefix
        """
        prefix = strs[0]

        for string in strs[1:]:
            """
                Reduce the prefix length until it matches the start of the string
            """
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
            """
                If the prefix becomes empty, there is no common prefix
            """
            if not prefix:
                return ""

        return prefix
