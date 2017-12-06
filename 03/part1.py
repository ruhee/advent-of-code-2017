#! /usr/bin/python

def walk_spiral(num):
  current_step = 1 # only needed to check if we've made it to the square provided
  current_direction = 'right'
  times_to_move = 1 # number of times to repeat the direction we're on right now
  current_repeat = 0 # number of times we have already repeated this direction
  coordinates = [0, 0]

  while current_step < num:
    if current_direction == 'right':
      coordinates[0] += 1
      current_repeat += 1
      current_step += 1
      if current_repeat == times_to_move:
        current_direction = 'up'
        current_repeat = 0
    elif current_direction == 'up':
      coordinates[1] += 1
      current_repeat += 1
      current_step += 1
      if current_repeat == times_to_move:
        times_to_move += 1
        current_direction = 'left'
        current_repeat = 0
    elif current_direction == 'left':
      coordinates[0] -= 1
      current_repeat += 1
      current_step += 1
      if current_repeat == times_to_move:
        current_direction = 'down'
        current_repeat = 0
    elif current_direction == 'down':
      coordinates[1] -= 1
      current_repeat += 1
      current_step += 1
      if current_repeat == times_to_move:
        current_direction = 'right'
        current_repeat = 0
        times_to_move += 1

  # manhattan distance: distance from 0 on both axes
  print abs(coordinates[0]) + abs(coordinates[1])

walk_spiral(1) # 0
walk_spiral(12) # 3
walk_spiral(289326) # 419