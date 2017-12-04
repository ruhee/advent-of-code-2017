#! /usr/bin/python
with open('input.txt', 'r') as txtfile:
  data = txtfile.read().strip().split('\n')

valid_phrases = 0

for line in data:
  pieces = line.split(' ')
  unique_pieces = set(pieces)
  if len(pieces) == len(unique_pieces):
    valid_phrases += 1

print valid_phrases
