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
        charIndexMap = {}  
        maxLength = 0  
        left = 0  
        
        for right, char in enumerate(s):
           
            if char in charIndexMap and charIndexMap[char] >= left:
                left = charIndexMap[char] + 1
            
            charIndexMap[char] = right  
            maxLength = max(maxLength, right - left + 1)  
        
        return maxLength

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
