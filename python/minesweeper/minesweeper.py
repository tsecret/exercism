from typing import List

def annotate(minefield: List[str]):

  board = [list(row) for row in minefield]

  for i in range(len(board)):
      if len(board[i]) != len(board[min(i+1, len(board)-1)]):
        raise ValueError("The board is invalid with current input.")

      for j in range(len(board[i])):

        if board[i][j] != '*' and board[i][j] != ' ':
          raise ValueError("The board is invalid with current input.")

        if board[i][j] == '*':
            continue

        mines = 0

        for k in range(max(0, i-1), min(i+2, len(board))):
            for l in range(max(0, j-1), min(j+2, len(board[i]))):


                if board[k][l] == '*':
                    mines += 1

        if mines > 0:
            board[i][j] = str(mines)


  board = ["".join(row) for row in board]

  return board
