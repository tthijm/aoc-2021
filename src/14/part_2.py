import sys, collections

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

template = lines[0]
rules = dict(tuple(x.split(" -> ")) for x in lines[2:])

counter = collections.Counter(template[i:i+2] for i in range(len(template) - 1))

for i in range(40):
  new_counter = collections.Counter()

  for k, v in counter.items():
    third = rules[k]
    new_counter[k[0] + third] += v
    new_counter[third + k[1]] += v

  counter = new_counter

c = collections.Counter()

for k, v in counter.items():
  c[k[0]] += v
  c[k[1]] += v

values = c.values()

print(max(values) // 2 - min(values) // 2 + 1)
