# Link : https://leetcode.com/problems/n-queens/

# Approach One

class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:

      def isQpresentOnLeftHorizontal(col, row, board):
          while col >= 0:
              if board[row][col] == 'Q':
                  return True
              col -= 1
          return False

      def isQpresentOnUpDiagonal(col, row, board):
          while row >= 0 and col >= 0:
              if board[row][col] == 'Q': return True
              col -= 1
              row -= 1
          return False

      def isQpresentOnDownDiagonal(col, row, board):
          while row < n and col >= 0:
              if board[row][col] == 'Q':
                  return True
              col -= 1
              row += 1
          return False

      ans = []

      def solve(col, board):
          if col == n:
              ans.append(list(board))
              return

          for row in range(n):

              if isQpresentOnLeftHorizontal(col, row, board):
                  continue

              if isQpresentOnUpDiagonal(col, row, board):
                  continue
                  
              if isQpresentOnDownDiagonal(col, row, board):
                  continue

              board[row] = board[row][:col] + 'Q' + board[row][col+1:]
              solve(col + 1, board)
              board[row] = board[row][:col] + '.' + board[row][col+1:]

      board = ['.'*n for _ in range(n)]
      solve(0, board)
      return ans
