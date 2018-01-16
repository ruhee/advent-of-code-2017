#! /usr/bin/python

# What is the value of the most recently played sound the first time a `rcv` instruction is executed with a non-zero value?

with open('input.txt', 'r') as txtfile:
  data = txtfile.read().strip().split('\n')

  current_instruction = 0
  last_played_val = 0
  last_recovered_val = 0

  # setup empty objects
  registers = {}
  keys = []

  for line in data:
    x = line.split()[1]
    if not x.isdigit():
      keys.append(x)

  keys = sorted(set(keys))
  for k in keys:
    registers[k] = 0

  while last_recovered_val == 0:
    current_line = data[current_instruction].split()
    instruction = current_line[0]
    x = current_line[1]
    if len(current_line) > 2:
      y = current_line[2]

    try:
      y = int(y)
    except ValueError:
      y = registers[y]

    if instruction == 'snd':
      last_played_val = registers[x]
    elif instruction == 'rcv':
      last_recovered_val = last_played_val
    elif instruction == 'set':
      registers[x] = y
    elif instruction == 'add':
      registers[x] += y
    elif instruction == 'mul':
      registers[x] = registers[x] * y
    elif instruction == 'mod':
      registers[x] = registers[x] % y
    elif instruction == 'jgz':
      try:
        x = int(x)
      except ValueError:
        x = registers[x]
      if x is not 0:
        current_instruction += y

    if instruction is not 'jgz':
      current_instruction += 1

  print last_recovered_val
