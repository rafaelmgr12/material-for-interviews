"""
Zigzag Conversion Problem:

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Explanation: The string "PAYPALISHIRING" is written in 3 rows in a zigzag pattern as described above. 
When read line by line, the converted string is "PAHNAPLSIIGYIR".

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation: For numRows = 4, the zigzag pattern would be written as follows:

P     I    N
A   L S  I G
Y A   H R
P     I

Reading this pattern line by line yields "PINALSIGYAHRPI".

Example 3:
Input: s = "A", numRows = 1
Output: "A"
Explanation: With only one row, the pattern is the same as the original string.

The challenge is to implement the convert function that rearranges a string into such a zigzag pattern given the number of rows.
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        current_row, step = 0, -1

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                step = -step  # Change direction
            current_row += step

        return ''.join(rows)

