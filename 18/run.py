#! /usr/bin/python

# What is the value of the most recently played sound the first time a `rcv` instruction is executed with a non-zero value?

with open('input.txt', 'r') as txtfile:
  data = txtfile.read().strip().split('\n')

  registers = {}
  keys = []

  for line in data:
    register = line.split()[1]
    # instructions can be like `jgz 1 3`, don't use that as a key
    if not register.isdigit(): # TODO: This might be a negative number
      keys.append(register)

  keys = sorted(set(keys))
  for k in keys:
    registers[k] = 0

  current_instruction = 0
  last_played_val = 0
  last_recovered_val = 0

  while last_recovered_val == 0:
    line = data[current_instruction].split()
    instruction = line[0]
    register = line[1] # TODO: This might be a number instead of a register key

    if instruction == 'snd':
      last_played_val = registers[register]
    elif instruction == 'rcv':
      last_recovered_val = last_played_val
      pass
    else:
      value = line[2]

      try:
        value = int(value)
      except ValueError:
        value = registers[value]

      if instruction == 'set':
        registers[register] = value
      elif instruction == 'add':
        registers[register] += value
      elif instruction == 'mul':
        registers[register] = registers[register] * value
      elif instruction == 'mod':
        registers[register] = registers[register] % value
      elif instruction == 'jgz':
        if register.isdigit():
          if register is not 0:
            current_instruction = current_instruction + register
            pass
          pass
        else:
          if registers[register] is not 0:
            current_instruction = current_instruction + registers[register]
            pass
          pass
        pass
    pass

    if instruction is not 'jgz':
      current_instruction += 1

print last_recovered_val
