import sys, collections

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

crabs = [int(x) for x in lines[0].split(",")]
q = collections.deque([sum(crabs) // len(crabs)])
res = 2**32

while q:
  v = q.popleft()
  fuel = 0

  for crab in crabs:
    fuel += abs(v - crab)

  if fuel < res:
    res = fuel
    q.append(v - 1)
    q.append(v + 1)

print(res)
