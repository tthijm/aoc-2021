import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

line = bin(int(lines[0], base=16))[2:]

if len(line) % 4 != 0:
  line = (4 - len(line) % 4) * "0" + line

def read_literal(i):
  value = ""
  done = False

  while not done and i < len(line):
    done, i = line[i] == "0", i + 1
    value, i = value + line[i:i+4], i + 4

  return (i, int(value, base=2))

def read_operator(i, id):
  length_type, i = line[i], i + 1

  if length_type == "0":
    length, i = int(line[i:i+15], base=2), i + 15

    i, values = f(i, i + length)
  else:
    size, i = int(line[i:i+11], base=2), i + 11
    values = []

    for _ in range(size):
      version, i = int(line[i:i+3], base=2), i + 3
      _id, i = int(line[i:i+3], base=2), i + 3

      if _id == 4:
        i, v = read_literal(i)
      else:
        i, v = read_operator(i, _id)
      
      values.append(v)
  
  match id:
    case 0:
      v = sum(values)
    case 1:
      v = 1

      for x in values:
        v *= x
    case 2:
      v = min(values)
    case 3:
      v = max(values)
    case 5:
      v = 1 if values[0] > values[1] else 0
    case 6:
      v = 1 if values[0] < values[1] else 0
    case 7:
      v = 1 if values[0] == values[1] else 0
    case _:
      assert False

  return (i, v)

def f(i = 0, end = len(line)):
  values = []

  while i < end and "1" in line[i:end+1]:
    version, i = int(line[i:i+3], base=2), i + 3
    id, i = int(line[i:i+3], base=2), i + 3

    if id == 4:
      i, v = read_literal(i)
    else:
      i, v = read_operator(i, id)
    
    values.append(v)

  return (i, values)

print(f()[1][0])
