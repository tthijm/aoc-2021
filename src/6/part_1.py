import sys, collections

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

fishes = collections.deque(int(x) for x in lines[0].split(","))

for _ in range(80):
  for _ in range(len(fishes)):
    v = fishes.popleft()

    if v > 0:
      fishes.append(v - 1)
    else:
      fishes.append(6)
      fishes.append(8)
  
print(len(fishes))
