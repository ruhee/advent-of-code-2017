#! /usr/bin/python
with open('input.txt', 'r') as input1:
  data = input1.read().strip()

matches = []
half = len(data)/2

for idx, val in enumerate(data):
  if idx < half:
    if val == data[idx+half]:
      matches.append(int(val))
  else:
    if val == data[idx-half]:
      matches.append(int(val))

print sum(matches)
