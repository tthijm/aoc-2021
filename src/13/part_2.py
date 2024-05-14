import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

middle = lines.index("")
points = set([tuple(int(x) for x in p.split(",")) for p in lines[:middle]])

for fold in lines[middle+1:]:
  fold = fold.split(" ")[2].split("=")
  fold = (fold[0], int(fold[1]))
  new_points = set()

  if fold[0] == "x":
    for x, y in points:
      assert x != fold[1]

      if x < fold[1]:
        new_points.add((x, y))
      else:
        new_points.add((fold[1] - (x - fold[1]), y))
  else:
    assert fold[0] == "y"

    for x, y in points:
      assert y != fold[1]

      if y < fold[1]:
        new_points.add((x, y))
      else:
        new_points.add((x, fold[1] - (y - fold[1])))

  points = new_points

max_x = max(x[0] for x in points)
max_y = max(x[1] for x in points)

for y in range(max_y + 1):
  for x in range(max_x + 1):
    if (x, y) in points:
      print("#", end="")
    else:
      print(".", end="")

  print("")
