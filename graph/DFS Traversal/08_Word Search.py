# https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, wordLength = len(board), len(board[0]), len(word)
        visited = set()

        def dfs(row, col, index):
            if index == wordLength: return True

            if row not in range(rows) or col not in range(cols) or (row, col) in visited or board[row][col] != word[index]:
                return False
            
            visited.add((row, col))
            
            down = dfs(row + 1, col, index + 1)
            up = dfs(row - 1, col, index + 1)
            right = dfs(row, col + 1, index + 1)
            left = dfs(row, col - 1, index + 1)

            isMatched = down or up or right or left

            visited.remove((row, col))
            return isMatched


        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0): return True
        return False
