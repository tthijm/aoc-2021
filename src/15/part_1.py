import sys, heapq, collections

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

lines = [[int(x) for x in l] for l in lines]
edges = collections.defaultdict(list)
heap = []
distances = {}

distances[(0, 0)] = 0
heapq.heappush(heap, (0, 0, 0))

for y in range(len(lines)):
  for x in range(len(lines[0])):
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
      nx, ny = x + dx, y + dy

      if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines):
        edges[(x, y)].append((nx, ny))

    if (x, y) != (0, 0):
      distances[(x, y)] = 2**32
      heapq.heappush(heap, (2**32, x, y))

while heap:
  risk, x, y = heapq.heappop(heap)

  for edge in edges[(x, y)]:
    alt = distances[(x, y)] + lines[edge[1]][edge[0]]

    if alt < distances[edge]:
      distances[edge] = alt
      heapq.heappush(heap, (alt, *edge))

print(distances[(len(lines) - 1, len(lines) - 1)])
