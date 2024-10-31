# Flood Fill
# Changing the color of a cell and its connected cells (like in paint bucket tools).

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    originalColor = image[sr][sc]
    if originalColor == newColor:
        return image

    def dfs(row: int, col: int):
        if (row < 0 or row >= len(image) or 
            col < 0 or col >= len(image[0]) or 
            image[row][col] != originalColor):
            return
        
        image[row][col] = newColor  # Change color
        # Explore neighbors
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    dfs(sr, sc)  # Start from the given cell
    return image
