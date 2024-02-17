# Link : https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited_cells = set()
        rows, cols = len(board), len(board[0])

        if len(word) > rows * cols:
            return False

        def depth_first_search(row, col, index):
            if index == len(word):
                return True
            if (row < 0 or row >= rows or col < 0 or col >= cols or 
                board[row][col] != word[index] or (row, col) in visited_cells):
                return False
            visited_cells.add((row, col))
            for new_row, new_col in ((row + 1, col), (row, col + 1), 
                                     (row - 1, col), (row, col - 1)):
                if depth_first_search(new_row, new_col, index + 1):
                    return True
            visited_cells.remove((row, col))
            return False

        for row in range(rows):
            for col in range(cols):
                if depth_first_search(row, col, 0):
                    return True
        return False
