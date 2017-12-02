#! /usr/bin/python
with open('input.txt', 'r') as input1:
  data = input1.read().strip()

matches = []

for idx, val in enumerate(data):
  if (idx == len(data)-1):
    if (val == data[0]): # check if last item matches first item
      matches.append(int(val))
  elif val == data[idx+1]:
    matches.append(int(val))

print sum(matches)
