"""
9. Palindrome Number

Given an integer x, return true if x is a  palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)

        left, right = 0,len(x_string)-1

        while left < right:
            if x_string[left]!= x_string[right]:
                return False

            left += 1
            right -=1
        return True

    def isPalindrome2(self, x: int) -> bool:
        if x > 0:
            temp = x
            revert_int_elemnts = []
            while temp > 0:
                digit = temp % 10
                revert_int_elemnts.append(digit)
                temp = temp // 10
            org_int_elements = revert_int_elemnts[::-1]
            return revert_int_elemnts == org_int_elements
        elif x == 0:
            return True
        else:
            return False
