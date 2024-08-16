import sys
from heapq import heappush, heappop

with open(sys.argv[1]) as f: lines = [l for l in f.readlines()]

ROOM = [(3, 2), (5, 2), (7, 2), (9, 2)]
ENERGY = [1, 10, 100, 1000]
FORBIDDEN = [3, 5, 7, 9]

amphipods = [("D", (3, 3)), ("D", (3, 4)), ("C", (5, 3)), ("B", (5, 4)), ("B", (7, 3)), ("A", (7, 4)), ("A", (9, 3)), ("C", (9, 4))]

for y in range(2, 4):
  for x in range(3, 11, 2):
    if y == 3:
      amphipods.append((lines[y][x], (x, 5)))
    else:
      amphipods.append((lines[y][x], (x, y)))

initial_state = (0,) + tuple(x[1] for x in sorted(amphipods))
seen = set([initial_state])
heap = [initial_state]

def is_done(state):
  for i in range(1, len(state), 4):
    goal = ROOM[(i - 1) // 4]

    if any(state[j][0] != goal[0] or not 2 <= state[j][1] <= 5 for j in range(i, i + 4)):
      return False

  return True

def is_correct(state, index):
  point = state[index]
  goal = ROOM[(index - 1) // 4]

  if point[0] != goal[0]:
    return False

  for y in range(point[1] + 1, 6):
    check_point = (point[0], y)

    if ROOM[(state.index(check_point) - 1) // 4] != goal:
      return False

  return True

def get_goal(state, index):
  goal = ROOM[(index - 1) // 4]

  for y in range(goal[1], goal[1] + 4):
    check_goal = (goal[0], y)

    if check_goal in state:
      break

    goal = check_goal

  return goal

def get_next_states(state):
  for index in range(1, len(state)):
    point = state[index]
    original_goal = ROOM[(index - 1) // 4]

    above_point = (point[0], point[1] - 1)

    if above_point in state:
      continue

    if is_correct(state, index):
      continue

    goal = get_goal(state, index)
    min_x = min(point[0], goal[0])
    max_x = max(point[0], goal[0])

    if not any(j != index and state[j][1] == 1 and min_x <= state[j][0] <= max_x for j in range(1, len(state))):
      if not any(j != index and state[j][0] == goal[0] and ROOM[(j - 1) // 4] != original_goal for j in range(1, len(state))):
        steps = (point[1] - 1) + abs(min_x - max_x) + (goal[1] - 1)
        energy = steps * ENERGY[(index - 1) // 4]

        yield (state[0] + energy,) + state[1:index] + (goal,) + state[index+1:]
        continue

    if point[1] == 1:
      continue

    for new_x in range(point[0] - 1, 0, -1):
      if new_x not in FORBIDDEN:
        goal = (new_x, 1)

        if goal in state:
          break

        steps = (point[1] - 1) + abs(point[0] - goal[0])
        energy = steps * ENERGY[(index - 1) // 4]

        yield (state[0] + energy,) + state[1:index] + (goal,) + state[index+1:]

    for new_x in range(point[0] + 1, 12):
      if new_x not in FORBIDDEN:
        goal = (new_x, 1)

        if goal in state:
          break

        steps = (point[1] - 1) + abs(point[0] - goal[0])
        energy = steps * ENERGY[(index - 1) // 4]

        yield (state[0] + energy,) + state[1:index] + (goal,) + state[index+1:]

while heap:
  state = heappop(heap)

  if is_done(state):
    print(state[0])
    break

  for next_state in get_next_states(state):
    if next_state not in seen:
      heappush(heap, next_state)
      seen.add(next_state)
