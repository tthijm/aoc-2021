import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

algorithm = lines[0]
image = lines[2:]
lit = set()

for y in range(len(image)):
  for x in range(len(image)):
    if image[y][x] == "#":
      lit.add((x, y))

def f(on):
  global lit

  new_lit = set()
  min_x = min_y = 2**32
  max_x = max_y = -2**32

  for x, y in lit:
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

  for y in range(min_y - 1, max_y + 2):
    for x in range(min_x - 1, max_x + 2):
      value = ""

      for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
          nx, ny = x + dx, y + dy

          if ((nx, ny) in lit) == on:
            value += "1"
          else:
            value += "0"

      value = int(value, base=2)

      if (algorithm[value] == "#") != on:
        new_lit.add((x, y))

  lit = new_lit

for i in range(2):
  f(i % 2 == 0)

print(len(lit))
