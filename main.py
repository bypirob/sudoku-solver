from sys import argv

def read_sudoku(file: str):
  mask = [[1 for i in range(9)] for i in range(9)]
  sudoku = [[0 for i in range(9)] for i in range(9)]

  f = open(file, "r")
  lines = f.readlines()
  f.close()

  y = 0
  x = 0
  for l in lines:
    x = 0
    for c in l:
      if c == "x":
        mask[y][x] = 0
      elif c != "\n":
        sudoku[y][x] = int(c)
      x += 1
    y += 1

  return sudoku, mask

def print_matrix(matrix: list[list[int]]):
  y = 0
  x = 0
  for row in matrix:
    if y % 3 == 0:
      print()
    for value in row:
      if x % 3 == 0:
        print("  ", end="")
      print(value, " ", end="")
      x += 1
    y += 1
    print()

def is_valid(sudoku: list[list[int]], x: int, y: int):
  value = sudoku[y][x]

  # Row check
  n = 0
  for v in sudoku[y]:
    if v == value:
      n += 1

  if n > 1:
    return False

  # Column check
  n = 0
  for i in range(9):
    v = sudoku[i][x]
    if v == value:
      n += 1

  if n > 1:
    return False

  # Sub-matrix check
  n = 0
  sy = y // 3
  sx = x // 3
  for i in range(9):
    v = sudoku[sy*3+i//3][sx*3+i%3]
    if v == value:
      n += 1

  if n > 1:
    return False

  return True

def solve(sudoku: list[list[int]], mask: list[list[int]]):
  solution = [x.copy() for x in sudoku]

  x = 0
  y = 0
  while y < 9:
    if mask[y][x] == 0:
      if solution[y][x] == 9:
        solution[y][x] = 0
        stop = False
        while not stop:
          x -= 1
          if x == -1:
            x = 8
            y -= 1
          stop = mask[y][x] == 0
      else:
        solution[y][x] += 1
        if is_valid(solution, x, y):
          x += 1
          if x == 9:
            x = 0
            y += 1
    else:
      x += 1
      if x == 9:
        x = 0
        y += 1
  return solution

def main(file: str):
  sudoku, mask = read_sudoku(file)
  print_matrix(sudoku)
  print("\n------")
  print_matrix(mask)

  solved = solve(sudoku, mask)

  print("\n------")
  print_matrix(solved)


if __name__ == "__main__":
  if len(argv) < 2:
    print("sudoku <filename>")
    exit(1)

  main(argv[1])
