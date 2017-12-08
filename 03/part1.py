#! /usr/bin/python

next_directions = {
  'right': 'up',
  'up': 'left',
  'left': 'down',
  'down': 'right'
}

def check_repeat():
  global current_repeat
  global current_direction
  global times_to_move
  if current_repeat == times_to_move:
    if current_direction == 'up' or current_direction == 'down':
      times_to_move += 1
    current_direction = next_directions[current_direction]
    current_repeat = 0

# num = 12 # 3
num = 289326 # 419
current_step = 1 # only needed to check if we've made it to the square provided
current_direction = 'right'
times_to_move = 1 # number of times to repeat the direction we're on right now
current_repeat = 0 # number of times we have already repeated this direction
coordinates = [0, 0]

while current_step < num:
  if current_direction == 'right':
    coordinates[0] += 1
  elif current_direction == 'up':
    coordinates[1] += 1
  elif current_direction == 'left':
    coordinates[0] -= 1
  elif current_direction == 'down':
    coordinates[1] -= 1

  current_repeat += 1
  current_step += 1
  check_repeat()

# manhattan distance: distance from 0 on both axes
print abs(coordinates[0]) + abs(coordinates[1])
