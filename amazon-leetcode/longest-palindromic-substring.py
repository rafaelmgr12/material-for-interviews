"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        def expandFromMiddle(s: str, left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            len1 = expandFromMiddle(s, i, i)
            len2 = expandFromMiddle(s, i, i + 1)
            length = max(len1, len2)
            
            if length > right - left:
                left = i - (length - 1) // 2
                right = i + length // 2
                
        return s[left:right + 1]
    
    



        