import sys, collections

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

vents = collections.defaultdict(int)

for line in lines:
  line = line.split("->")
  x1, y1 = (int(x) for x in line[0].split(","))
  x2, y2 = (int(x) for x in line[1].split(","))

  if x1 == x2:
    for y in range(min(y1, y2), max(y1, y2) + 1):
      vents[(x1, y)] += 1
  elif y1 == y2:
    for x in range(min(x1, x2), max(x1, x2) + 1):
      vents[(x, y1)] += 1
  else:
    if x2 > x1:
      s = 1 if y2 >= y1 else -1

      for dx in range(max(x1, x2) - min(x1, x2) + 1):
        x = x1 + dx
        y = y1 + dx * s
        vents[(x, y)] += 1
    else:
      s = 1 if y1 >= y2 else -1

      for dx in range(max(x1, x2) - min(x1, x2) + 1):
        x = x1 - dx
        y = y1 - dx * s
        vents[(x, y)] += 1

ans = 0

for v in vents.values():
  if v > 1:
    ans += 1

print(ans)
