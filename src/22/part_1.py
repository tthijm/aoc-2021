import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

cubes = set()

for line in lines:
  on = line.split()[0] == "on"
  x, y, z = [[int(x) for x in l[2:].split("..")] for l in line.split()[1].split(",")]

  if not (-50 <= x[0] <= x[1] <= 50 and -50 <= y[0] <= y[1] <= 50 and -50 <= z[0] <= z[1] <= 50):
    continue

  for nz in range(z[0], z[1] + 1):
    for ny in range(y[0], y[1] + 1):
      for nx in range(x[0], x[1] + 1):
        if on:
          cubes.add((nx, ny, nz))
        else:
          if (nx, ny, nz) in cubes:
            cubes.remove((nx, ny, nz))

print(len(cubes))
