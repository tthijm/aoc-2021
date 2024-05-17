import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

a_position, b_position = int(lines[0].split()[-1]), int(lines[1].split()[-1])
a_score = b_score = 0
die = 1
rolls = 0

while a_score < 1000 and b_score < 1000:
  move = 0

  for _ in range(3):
    move += (die) - (die - 1) // 100 * 100
    die += 1

  if rolls % 2 == 0:
    a_position += move
    a_position -= (a_position - 1) // 10 * 10
    a_score += a_position
  else:
    b_position += move
    b_position -= (b_position - 1) // 10 * 10
    b_score += b_position

  rolls += 3

print(min(a_score, b_score) * rolls)
