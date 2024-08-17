import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

valid = set(i for i in range(len(lines)))

for i in range(len(lines[0])):
  ones = set()
  zeros = set()

  for j in valid:
    if lines[j][i] == "1":
      ones.add(j)
    else:
      zeros.add(j)

  if len(ones) >= len(zeros):
    valid -= zeros
  else:
    valid -= ones

  if len(valid) == 1:
    break

oxygen = lines[valid.pop()]

valid = set(i for i in range(len(lines)))

for i in range(len(lines[0])):
  ones = set()
  zeros = set()

  for j in valid:
    if lines[j][i] == "1":
      ones.add(j)
    else:
      zeros.add(j)

  if len(ones) >= len(zeros):
    valid -= ones
  else:
    valid -= zeros

  if len(valid) == 1:
    break

co2 = lines[valid.pop()]

print(int(oxygen, base=2) * int(co2, base=2))
