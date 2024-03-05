# Problem: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Examples:
# 1. Input: s = "abcabcbb"
#    Output: 3
#    Explanation: The answer is "abc", with the length of 3.
# 2. Input: s = "bbbbb"
#    Output: 1
#    Explanation: The answer is "b", with the length of 1.
# 3. Input: s = "pwwkew"
#    Output: 3
#    Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0  
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
