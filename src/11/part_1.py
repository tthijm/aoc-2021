import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

DS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
lines = [[int(x) for x in l] for l in lines]
res = 0

def f(x, y):
  lines[y][x] = -1

  for dx, dy in DS:
    nx, ny = x + dx, y + dy

    if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines) and lines[ny][nx] != -1:
      lines[ny][nx] += 1

      if lines[ny][nx] > 9:
        f(nx, ny)

for _ in range(100):
  lines = [[x + 1 for x in l] for l in lines]

  for y in range(len(lines)):
    for x in range(len(lines[0])):
      if lines[y][x] > 9:
        f(x, y)

  for y in range(len(lines)):
    for x in range(len(lines[0])):
      if lines[y][x] == -1:
        res += 1
        lines[y][x] = 0

print(res)
