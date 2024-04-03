"""
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        # Pre-check for letter availability
        board_letters = {}
        for row in board:
            for letter in row:
                board_letters[letter] = board_letters.get(letter, 0) + 1
        
        word_letters = {}
        for letter in word:
            word_letters[letter] = word_letters.get(letter, 0) + 1
            if word_letters[letter] > board_letters.get(letter, 0):
                return False

        def dfs(i, j, word_index):
            if word_index == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[word_index]:
                return False

            temp, board[i][j] = board[i][j], '#'  # Mark as visited
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Explore all directions
                if dfs(i + dx, j + dy, word_index + 1):
                    return True
            board[i][j] = temp  # Restore the original letter

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
    
    def existNaive(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, word):
            if not word:
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            ans = dfs(i+1, j, word[1:]) or dfs(i-1, j, word[1:]) or dfs(i, j+1, word[1:]) or dfs(i, j-1, word[1:])
            board[i][j] = temp
            
            return ans
        
        ans = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ans = ans or dfs(i, j, word)
                    
        return ans