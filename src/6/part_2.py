import sys, collections

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

res = 0

for v in lines[0].split(","):
  v = int(v)
  days = collections.defaultdict(int)

  days[v] = 1
  res += 1

  for i in range(256):
    amount = days[i]

    days[i + 7] += amount
    days[i + 9] += amount
    res += amount

print(res)
