# Word Search
# Finding a word in a 2D board of characters using DFS.

# Variation One

def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    visited = set()

    def dfs(row: int, col: int, index: int) -> bool:
        if index == len(word):
            return True
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            (row, col) in visited or board[row][col] != word[index]):
            return False
        
        visited.add((row, col))
        
        # Define the directions as (row_change, col_change)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        found = False
        
        # Explore all 4 directions using a for loop
        for dr, dc in directions:
            if dfs(row + dr, col + dc, index + 1):
                found = True
                break

        visited.remove((row, col))  # Backtrack
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):  # Start DFS from each cell
                return True
    return False

# Example usage
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
word = "ABCCED"
print(exist(board, word))  # Output: True


# Variation Two

def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    visited = set()

    def dfs(row: int, col: int, index: int) -> bool:
        if index == len(word):
            return True
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            (row, col) in visited or board[row][col] != word[index]):
            return False
        
        visited.add((row, col))
        # Explore all 4 directions
        found = (dfs(row + 1, col, index + 1) or 
                 dfs(row - 1, col, index + 1) or 
                 dfs(row, col + 1, index + 1) or 
                 dfs(row, col - 1, index + 1))
        visited.remove((row, col))  # Backtrack
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):  # Start DFS from each cell
                return True
    return False
