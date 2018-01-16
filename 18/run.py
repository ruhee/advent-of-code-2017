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
  last_recovered_val = None

  while last_recovered_val is None:
    pass

  ##############

  for line in data:
    # could be formatted like `set i 31` or `snd a` or `jgz 1 3`
    # snd/rcv do not have a value param, the others do
    # [instruction] [register or number] [optional value]

    line = line.split()
    instruction = line[0]
    register = line[1] # TODO: This might be a number instead of a register key

    if instruction == 'snd':
      last_played_val = registers[register]
    elif instruction == 'rcv':
      if last_played_val is not 0:
        print 'Last value:', last_played_val
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
            pass
          pass
        else:
          if registers[register] is not 0:
            # go to line indicated by offset
            pass
          pass
        pass

print registers
