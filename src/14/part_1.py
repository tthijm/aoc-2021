import sys, collections

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

template = lines[0]
rules = dict(tuple(x.split(" -> ")) for x in lines[2:])

for _ in range(10):
  new_template = ""

  for i in range(len(template) - 1):
    pair = template[i:i+2]

    new_template += template[i]
    new_template += rules[pair]
  
  new_template += template[-1]
  
  template = new_template

c = collections.Counter(template)
values = c.values()

print(max(values) - min(values))
