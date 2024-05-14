import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

tx, ty = [[int(v) for v in x.split("=")[1].split("..")] for x in lines[0].split(": ")[1].split(",")]

def f(dx, dy):
  x = y = 0

  while x <= tx[1] and y >= ty[1] or x <= tx[1] and dx:
    x += dx
    y += dy

    if tx[0] <= x <= tx[1] and ty[0] <= y <= ty[1]:
      return True

    if dx > 0:
      dx -= 1
    elif dx < 0:
      dx += 1

    dy -= 1

  return False

res = 0

for dx in range(1000):
  for dy in range(-1000, 1000):
    if f(dx, dy):
      res += 1

print(res)
