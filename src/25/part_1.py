import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

east, west = set(), set()

for y in range(len(lines)):
  for x in range(len(lines[0])):
    if lines[y][x] == ">":
      east.add((x, y))
    elif lines[y][x] == "v":
      west.add((x, y))

for i in range(10**10):
  new_east, new_west = set(), set()
  moved = False

  for x, y in east:
    nx, ny = (x + 1) % len(lines[0]), y

    if (nx, ny) in east or (nx, ny) in west:
      new_east.add((x, y))
    else:
      new_east.add((nx, ny))
      moved = True

  east = new_east

  for x, y in west:
    nx, ny = x, (y + 1) % len(lines)

    if (nx, ny) in east or (nx, ny) in west:
      new_west.add((x, y))
    else:
      new_west.add((nx, ny))
      moved = True

  west = new_west

  if not moved:
    break

print(i + 1)