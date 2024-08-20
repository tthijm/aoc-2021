import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

line = bin(int(lines[0], base=16))[2:]

if len(line) % 4 != 0:
  line = (4 - len(line) % 4) * "0" + line

res = 0

def read_literal(i):
  value = ""
  done = False

  while not done and i < len(line):
    done, i = line[i] == "0", i + 1
    value, i = value + line[i:i+4], i + 4

  return i

def read_operator(i):
  global res

  length_type, i = line[i], i + 1

  if length_type == "0":
    length, i = int(line[i:i+15], base=2), i + 15

    i = f(i, i + length)
  else:
    size, i = int(line[i:i+11], base=2), i + 11

    for _ in range(size):
      version, i = int(line[i:i+3], base=2), i + 3
      id, i = int(line[i:i+3], base=2), i + 3

      res += version

      if id == 4:
        i = read_literal(i)
      else:
        i = read_operator(i)

  return i

def f(i = 0, end = len(line)):
  global res

  while i < end and "1" in line[i:end+1]:
    version, i = int(line[i:i+3], base=2), i + 3
    id, i = int(line[i:i+3], base=2), i + 3

    res += version

    if id == 4:
      i = read_literal(i)
    else:
      i = read_operator(i)
  
  return i

f()
print(res)
