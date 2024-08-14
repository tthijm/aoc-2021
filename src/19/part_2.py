import sys
from collections import Counter
from itertools import product, permutations

with open(sys.argv[1]) as f: lines = f.read()

scanners = {}

for section in lines.split("\n\n"):
  beacons = []

  for line in section.split("\n")[1:]:
    if line:
      x, y, z = (int(x) for x in line.split(","))
      beacons.append((x, y, z))
  
  scanners[len(scanners)] = beacons

solid = set(scanners.pop(0))

def get_orientations(beacons):
  orientations = [[] for _ in range(48)]

  for x, y, z in beacons:
    i = 0

    for pair in product([x, -x], [y, -y], [z, -z]):
      for option in permutations(pair):
        orientations[i].append(option)
        i += 1

  return orientations

def diff(a, b):
  return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def plus(a, b):
  return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def f(beacons):
  for orientation in get_orientations(beacons):
    c = Counter()

    for point_1 in solid:
      for point_2 in orientation:
        c[diff(point_1, point_2)] += 1
    
    most_common = c.most_common(1)[0]

    if most_common[1] >= 12:
      position = most_common[0]
      orientation = [plus(point, position) for point in orientation]

      return position, orientation

  return None, None

keys = scanners.keys()
positions = [(0, 0, 0)]

while keys:
  for key in list(keys):
    value = scanners[key]
    position, orientation = f(value)

    if orientation:
      solid = solid.union(set(orientation))
      positions.append(position)
      scanners.pop(key)

  keys = scanners.keys()

res = 0

for i in range(len(positions)):
  for j in range(i + 1, len(positions)):
    position_1 = positions[i]
    position_2 = positions[j]
    distance = sum(abs(position_2[x] - position_1[x]) for x in range(3))
    res = max(res, distance)

print(res)
