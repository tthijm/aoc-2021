import sys

with open(sys.argv[1]) as f: lines = [l.strip() for l in f.readlines()]

horizontal = 0
depth = 0
aim = 0

for line in lines:
  line = line.split()
  command = line[0]
  n = int(line[1])

  if command.startswith("f"):
    horizontal += n
    depth += n * aim
  elif command.startswith("d"):
    aim += n
  else:
    aim -= n

print(horizontal * depth)
