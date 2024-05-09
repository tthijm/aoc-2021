import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

MATCHES = { ")": "(", "]": "[", "}": "{", ">" : "<" }
POINTS = { "(": 1, "[": 2, "{": 3, "<": 4 }
scores = []

for line in lines:
  stack = []
  score = 0

  for c in line:
    if c in "[({<":
      stack.append(c)
    else:
      last = stack.pop()

      if last != MATCHES[c]:
        break
  else:
    while stack:
      score *= 5
      score += POINTS[stack.pop()]

    scores.append(score)

print(sorted(scores)[len(scores) // 2])
