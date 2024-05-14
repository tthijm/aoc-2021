import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

tx, ty = [[int(v) for v in x.split("=")[1].split("..")] for x in lines[0].split(": ")[1].split(",")]

def f(dx, dy):
  x = y = max_y = 0

  while x <= tx[1] and y >= ty[1]:
    x += dx
    y += dy
    max_y = max(max_y, y)

    if tx[0] <= x <= tx[1] and ty[0] <= y <= ty[1]:
      return max_y

    if dx > 0:
      dx -= 1
    else:
      dx += 1

    dy -= 1

  return -1

res = 0

for dx in range(-1000, 1000):
  for dy in range(-1000, 1000):
    res = max(res, f(dx, dy))

print(res)
