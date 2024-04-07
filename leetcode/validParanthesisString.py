"""
678. Valid Parenthesis String
Medium
Topics
Companies
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        open_brackets = []
        asteriks = []
        
        for i in range(len(s)):

            if s[i] == "(":
                open_brackets.append(i)
            elif s[i] == "*":
                asteriks.appen(i)
            elif s[i] ==")":
                if open_brackets:
                    open_brackets.pop()
                elif asteriks:
                    asteriks.pop()
                else:
                    return False
        
        while open_brackets and asteriks:
            if open_brackets.pop() > asteriks.pop():
                return False
            
        return not open_brackets