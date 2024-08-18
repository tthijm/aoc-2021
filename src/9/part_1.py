import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines = [[int(x) for x in line] for line in lines]
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 0

for y in range(len(lines)):
  for x in range(len(lines[0])):
    for dx, dy in ds:
      nx = x + dx
      ny = y + dy

      if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines) and lines[ny][nx] <= lines[y][x]:
        break
    else:
      res += lines[y][x] + 1

print(res)
