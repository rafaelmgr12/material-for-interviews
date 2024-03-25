class Solution(object):
    def isMatch(self, text, pattern):
        """
        Given an input string (text) and a pattern, implement regular expression matching with support for '.' and '*'.
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).
        
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]

# Exemplos de uso
if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch("aa", "a"))  # Deve retornar False
    print(solution.isMatch("aa", "a*"))  # Deve retornar True
    print(solution.isMatch("ab", ".*"))  # Deve retornar True