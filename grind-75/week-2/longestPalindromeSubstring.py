"""Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters. """

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> str:
        char_counts = Counter(s)
        length = 0
        odd_found = False
        
        for count in char_counts.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1  # Use all but one of the character
                odd_found = True
        
        # If any character has an odd count, we can place exactly one in the middle
        if odd_found:
            length += 1
        
        return length