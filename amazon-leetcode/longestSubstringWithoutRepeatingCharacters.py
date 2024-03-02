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
        result = 0
        left = 0

        for right in range(len(s)):
            if s[right] in s[left:right]:
                left = s.index(s[right],left)+1

            result = max(result, right -left +1)

        return result
       


# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
