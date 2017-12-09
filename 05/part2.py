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
  if data[current_instruction_index] > 2:
    data[current_instruction_index] -= 1
  else:
    data[current_instruction_index] += 1
  current_instruction_index = next_instruction_index
  number_of_steps += 1

print number_of_steps
