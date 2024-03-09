"""
371. Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        x,y = abs(a),abs(b)
        if x < y:
            return self.getSum(b,a)
        
        sign = 1 if a > 0 else -1
        if a * b >= 0:
            while y:
                x,y = x^y, (x&y) << 1
        else:
            while y:
                x,y = x^y, ((~x)&y) << 1
                
        return x * sign