import sys
from collections import deque

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines = [[int(x) for x in line] for line in lines]
DS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
lows = set()

for y in range(len(lines)):
  for x in range(len(lines[0])):
    for dx, dy in DS:
      nx = x + dx
      ny = y + dy

      if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines) and lines[ny][nx] <= lines[y][x]:
        break
    else:
      lows.add((x, y))

def f(_x, _y):
  q = deque([(_x, _y)])
  values = set()

  while q:
    x, y = q.popleft()

    if lines[y][x] == 9:
      continue

    for dx, dy in DS:
      nx = x + dx
      ny = y + dy

      if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines) and lines[ny][nx] < lines[y][x] and (nx, ny) not in values:
        break
    else:
      values.add((x, y))

      for dx, dy, in DS:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines) and (nx, ny) not in values:
          q.append((nx, ny))

  return len(values)

a = sorted((f(*x) for x in lows), reverse=True)

print(a[0] * a[1] * a[2])
