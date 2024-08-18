import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lengths = set([2, 4, 3, 7])
res = 0

for line in lines:
  line = line.split("|")
  output = line[1]

  for v in output.split():
    if len(v) in lengths:
      res += 1

print(res)
