import sys, collections

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

res = 0

for line in lines:
  line = [x.split() for x in line.split("|")]
  input, output = line

  lengths = collections.defaultdict(list)
  mapping = {}

  for v in input:
    lengths[len(v)].append(set(v))

  mapping[frozenset(lengths[2][0])] = 1
  mapping[frozenset(lengths[4][0])] = 4
  mapping[frozenset(lengths[3][0])] = 7
  mapping[frozenset(lengths[7][0])] = 8

  for v in lengths[6]:
    if len(v.intersection(lengths[2][0])) == 1:
      mapping[frozenset(v)] = 6
    elif len(v.intersection(lengths[4][0])) == 4:
      mapping[frozenset(v)] = 9
    else:
      mapping[frozenset(v)] = 0

  for v in lengths[5]:
    if len(v.intersection(lengths[2][0])) == 2:
      mapping[frozenset(v)] = 3
    elif len(v.intersection(lengths[4][0])) == 2:
      mapping[frozenset(v)] = 2
    else:
      mapping[frozenset(v)] = 5

  digits = ""

  for o in output:
    o = set(o)

    for k, v in mapping.items():
      if len(k) == len(o) and not k - o:
        digits += str(v)
        break
  
  res += int(digits)

print(res)
