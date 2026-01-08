from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    col_vals = [[] for _ in range(9)]
    square_vals = [[] for _ in range(9)]
    for r, row in enumerate(board):
      row_vals = []
      row_vals_set = set()
      for c, cell in enumerate(row):
        if cell != ".": 
          row_vals.append(cell)
          col_vals[c].append(cell)
          square_index = (r/3)*3
          square_vals[]
        row_vals_set = set(row_vals)

        
      if len(row_vals_set) != len(row_vals): return False

    for cols in col_vals:
      cols_set = set(cols)
      if len(cols_set) != len(cols): return False



    return True
      
if __name__ == "__main__":
  s= Solution()
  board = [["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]
  print(s.isValidSudoku(board))