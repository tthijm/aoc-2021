import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

a, b = int(lines[0].split()[-1]), int(lines[1].split()[-1])
dp = {}

def f(a_position, a_score, b_position, b_score):
  key = (a_position, a_score, b_position, b_score)
  value = (0, 0)

  if key in dp:
    return dp[key]

  if a_score >= 21:
    return (1, 0)

  if b_score >= 21:
    return (0, 1)

  for die1 in [1, 2, 3]:
    for die2 in [1, 2, 3]:
      for die3 in [1, 2, 3]:
        na_position = (a_position + die1 + die2 + die3) % 10
        na_score = a_score + na_position + 1

        b_win, a_win = f(b_position, b_score, na_position, na_score)

        value = (value[0] + a_win, value[1] + b_win)

  dp[key] = value

  return value

print(max(f(a - 1, 0, b - 1, 0)))
