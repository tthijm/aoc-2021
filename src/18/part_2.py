import sys, math, json

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

res = None

def add(x):
  global res

  res = f"[{res},{x}]"

def increase_left(x, v):
  global res

  start = None

  for i in range(x - 1, -1, -1):
    c = res[i]

    if c.isdigit():
      if not start:
        start = i
    else:
      if start:
        res = f"{res[:i+1]}{int(res[i+1:start+1]) + v}{res[start+1:]}"
        break

def increase_right(x, v):
  global res

  start = None

  for i in range(x, len(res)):
    c = res[i]

    if c.isdigit():
      if not start:
        start = i
    else:
      if start:
        res = f"{res[:start]}{int(res[start:i]) + v}{res[i:]}"
        break

def explode():
  global res

  depth = 0

  for i, c in enumerate(res):
    if c == "[":
      depth += 1

      if depth == 5:
        j = i

        while res[j] != "]":
          j += 1

        left, right = [int(x) for x in res[i+1:j].split(",")]
        length = len(res)
        res = f"{res[:i]}0{res[j+1:]}"

        j = j - length + len(res) + 1
        length = len(res)

        increase_left(i, left)

        j = j - length + len(res)

        increase_right(j, right)

        return True
    elif c == "]":
      depth -= 1

  return False

def split():
  global res

  start, current = -1, ""

  for i, c in enumerate(res):
    if c.isdigit():
      current += c
    else:
      if current:
        v = int(current)

        if v >= 10:
          left, right = math.floor(v / 2), math.ceil(v / 2)

          res = f"{res[:start+1]}[{left},{right}]{res[i:]}"

          return True

      start, current = i, ""

def reduce():
  done = False

  while not done:
    while explode():
      continue

    done = not split()

def get_magnitude(x):
  if isinstance(x, int):
    return x

  return 3 * get_magnitude(x[0]) + 2 * get_magnitude(x[1])

best = 0

for a in lines:
  for b in lines:
    if a == b:
      continue

    res = a
    add(b)
    reduce()
    best = max(best, get_magnitude(json.loads(res)))

print(best)
