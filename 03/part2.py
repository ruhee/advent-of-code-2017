#! /usr/bin/python

'''
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
'''

# When reaching a new square:
  # Check adjacent squares for values: combinations of x (-1, 0, -1) and y (-1, 0, -1)
  # Sum whatever values exist
  # Store that value at these coordinates
  # Check if value is greater than input
    # if yes, break and return
    # else continue

# eight squares:
#
#  x x x
#  x - x
#  x x x
#
# From origin:
# [-1, 1]   [0, 1]  [1, 1]
# [-1, 0]           [1, 0]
# [-1, -1]  [0, -1] [1, -1]

def get_value(coords, values):
  key = get_key(coords)
  if key in values:
    return values[key]
  else:
    return None

def get_key(coords):
  return '{0},{1}'.format(coords[0], coords[1])

def sum_adjacent(coords):
  x = coords[0]
  y = coords[1]

  return sum(filter(None, [
    values.get(get_key([x-1, y+1])),
    values.get(get_key([x, y+1])),
    values.get(get_key([x+1, y+1])),
    values.get(get_key([x-1, y])),
    values.get(get_key([x+1, y])),
    values.get(get_key([x-1, y-1])),
    values.get(get_key([x, y-1])),
    values.get(get_key([x+1, y-1]))
  ]))

# num = 3 # 4
num = 289326 # 295229

current_value = 1 # break when it's larger than the input
current_direction = 'right'
times_to_move = 1 # number of times to repeat the direction we're on right now
current_repeat = 0 # number of times we have already repeated this direction
coordinates = [0, 0]
values = {
  '0,0': 1
}

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

while current_value < num:
  if current_direction == 'right':
    coordinates[0] += 1
  elif current_direction == 'up':
    coordinates[1] += 1
  elif current_direction == 'left':
    coordinates[0] -= 1
  elif current_direction == 'down':
    coordinates[1] -= 1

  current_repeat += 1
  values[get_key(coordinates)] = sum_adjacent(coordinates)
  current_value = values[get_key(coordinates)]
  check_repeat()

print current_value
