#! /usr/bin/python
with open('input.txt', 'r') as txtfile:
  data = txtfile.read().strip().split('\n')

data = [int(item) for item in data]

current_instruction_index = 0
current_instruction_value = 0
next_instruction_index = 0
number_of_steps = 0

while next_instruction_index < len(data):
  next_instruction_index = current_instruction_index + data[current_instruction_index]
  data[current_instruction_index] += 1
  current_instruction_index = next_instruction_index
  number_of_steps += 1

print number_of_steps

######## planning notes left here for fun

# Read instruction, jump, increment, repeat

# Start at the first instruction, index 0.
# Each line tells you, in relative terms, what the next instruction is.
# When you follow an instruction, it gets incremented by 1.
  # - next_instruction: list[current_instruction_value]
  # - increment current_instruction_value IN THE LIST, number_of_steps
  # goto next_instruction
  # if next_instruction is out of list index range, print number_of_steps
