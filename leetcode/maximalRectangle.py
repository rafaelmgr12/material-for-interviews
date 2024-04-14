"""
85. Maximal Rectangle
Hard
Topics
Companies
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        ROWS, COLS = len(matrix), len(matrix[0])
        max_area = 0
        height = [0]* (COLS+1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == "1":
                    height[c] += 1
                else:
                    height[c] = 0
            # Now find the maximum rectangle that can be formed in this histogram
            stack = []
            for i in range(COLS+1):
                while stack and height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area
 