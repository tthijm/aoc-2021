import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

gamma = b""
epsilon = b""

for i in range(len(lines[0])):
  values = []

  for j in range(len(lines)):
    values.append(lines[j][i])

  if values.count("0") > len(values) / 2:
    gamma += b"0"
    epsilon += b"1"
  else:
    gamma += b"1"
    epsilon += b"0"

print(int(gamma, base=2) * int(epsilon, base=2))
