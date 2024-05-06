import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines = [int(x) for x in lines]
res = 0

for i in range(1, len(lines)):
  if lines[i] > lines[i - 1]:
    res += 1

print(res)
