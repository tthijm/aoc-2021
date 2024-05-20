import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

cubes = []

def f(a, b):
  if not (a[1] <= b[2] and a[2] >= b[1] and a[3] <= b[4] and a[4] >= b[3] and a[5] <= b[6] and a[6] >= b[5]):
    return None

  return (not b[0], max(a[1], b[1]), min(a[2], b[2]), max(a[3], b[3]), min(a[4], b[4]), max(a[5], b[5]), min(a[6], b[6]))

for line in lines:
  on = line.split()[0] == "on"
  x, y, z = [[int(x) for x in l[2:].split("..")] for l in line.split()[1].split(",")]
  line = (on, x[0], x[1], y[0], y[1], z[0], z[1])

  intersections = []

  for cube in cubes:
    intersection = f(line, cube)

    if intersection:
      intersections.append(intersection)

  if on:
    intersections.append(line)

  cubes += intersections

res = 0

for cube in cubes:
  v = (cube[2] - cube[1] + 1) * (cube[4] - cube[3] + 1) * (cube[6] - cube[5] + 1)

  if cube[0]:
    res += v
  else:
    res -= v

print(res)
