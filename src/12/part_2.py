import sys, collections

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

edges = collections.defaultdict(list)
res = 0

for line in lines:
  start, end = line.split("-")

  edges[start].append(end)
  edges[end].append(start)

remaining = set(k for k in edges.keys() if k.lower() == k and k != "start")
twice = False

def f(x):
  global res, twice

  if x == "end":
    res += 1
    return

  for out in edges[x]:
    if out.lower() == out:
      if out in remaining:
        remaining.remove(out)
        f(out)
        remaining.add(out)
      else:
        if not twice and out != "start":
          twice = True
          f(out)
          twice = False
    else:
      f(out)

f("start")
print(res)
