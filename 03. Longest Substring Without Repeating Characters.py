class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = 0
        dict_substring = {}
        i = 0
        for j in range(len(s)):
            if s[j] in dict_substring:
                i = max(i, dict_substring[s[j]] + 1)
            max_substring = max(max_substring, j - i + 1)
            dict_substring[s[j]] = j
        return max_substring    