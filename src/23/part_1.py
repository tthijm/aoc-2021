import sys
from heapq import heappush, heappop

with open(sys.argv[1]) as f: lines = [l for l in f.readlines()]

ROOM = [(3, 2), (5, 2), (7, 2), (9, 2)]
ENERGY = [1, 10, 100, 1000]
FORBIDDEN = [3, 5, 7, 9]

amphipods = []

for y in range(2, 4):
  for x in range(3, 11, 2):
    amphipods.append((lines[y][x], (x, y)))

initial_state = (0,) + tuple(x[1] for x in sorted(amphipods))
seen = set([initial_state])
heap = [initial_state]

def is_done(state):
  for i in range(1, len(state), 2):
    point_a, point_b = state[i], state[i + 1]
    goal_a = ROOM[(i - 1) // 2]
    goal_b = (goal_a[0], goal_a[1] + 1)

    if not ((point_a == goal_a and point_b == goal_b) or (point_a == goal_b and point_b == goal_a)):
      return False

  return True

def get_next_states(state):
  for index in range(1, len(state)):
    point = state[index]
    goal = ROOM[(index - 1) // 2]

    above_point = (point[0], point[1] - 1)
    below_goal = (goal[0], goal[1] + 1)

    if above_point in state:
      continue

    if point == below_goal or (point == goal and ROOM[(state.index(below_goal) - 1) // 2] == goal):
      continue

    if goal not in state and (below_goal not in state or ROOM[(state.index(below_goal) - 1) // 2] == goal):
      min_x = min(point[0], goal[0])
      max_x = max(point[0], goal[0])

      if not any(j != index and state[j][1] == 1 and min_x <= state[j][0] <= max_x for j in range(1, len(state))):
        if below_goal not in state:
          goal = below_goal

        steps = (point[1] - 1) + abs(min_x - max_x) + (goal[1] - 1)
        energy = steps * ENERGY[(index - 1) // 2]

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
        energy = steps * ENERGY[(index - 1) // 2]

        yield (state[0] + energy,) + state[1:index] + (goal,) + state[index+1:]

    for new_x in range(point[0] + 1, 12):
      if new_x not in FORBIDDEN:
        goal = (new_x, 1)

        if goal in state:
          break

        steps = (point[1] - 1) + abs(point[0] - goal[0])
        energy = steps * ENERGY[(index - 1) // 2]

        yield (state[0] + energy,) + state[1:index] + (goal,) + state[index+1:]

while seen:
  state = heappop(heap)

  if is_done(state):
    print(state[0])
    break

  for next_state in get_next_states(state):
    if next_state not in seen:
      heappush(heap, next_state)
      seen.add(next_state)
