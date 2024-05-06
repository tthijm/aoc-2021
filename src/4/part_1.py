import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

numbers = [int(x) for x in lines[0].split(",")]
boards = []

for i in range(2, len(lines), 6):
  board = {}
  values = [[int(x) for x in l.split()] for l in lines[i:i+5]]

  for y in range(len(values)):
    for x in range(len(values[0])):
      board[values[y][x]] = (x, y)

  boards.append(board)

for num in numbers:
  for board in boards:
    if num not in board:
      continue

    x, y = board[num]
    del board[num]
    values = board.values()

    for i in range(5):
      if (i, y) in values:
        break
    else:
      print(sum(board.keys()) * num)
      exit(0)

    for i in range(5):
      if (x, i) in values:
        break
    else:
      print(sum(board.keys()) * num)
      exit(0)
