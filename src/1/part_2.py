import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines = [int(x) for x in lines]
prev = sum(lines[0:3])
res = 0

for i in range(1, len(lines) - 2):
  window = sum(lines[i:i+3])

  if window > prev:
    res += 1

  prev = window

print(res)
