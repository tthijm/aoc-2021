import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

MATCHES = { ")": "(", "]": "[", "}": "{", ">" : "<" }
POINTS = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
res = 0

for line in lines:
  stack = []

  for c in line:
    if c in "[({<":
      stack.append(c)
    else:
      last = stack.pop()

      if last != MATCHES[c]:
        res += POINTS[c]
        break

print(res)
