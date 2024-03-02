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
        def hasRepeatingChars(sub: str) -> bool:
            """Verifica se a substring tem caracteres repetidos."""
            charSet = set()
            for char in sub:
                if char in charSet:
                    return True
                charSet.add(char)
            return False
        
        n = len(s)
        if n == 0:
            return 0
        maxLength = 1
        
        for i in range(n):
            for j in range(i+1, n+1):
                if not hasRepeatingChars(s[i:j]):
                    maxLength = max(maxLength, j-i)
                else:
                    break
        
        return maxLength

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
