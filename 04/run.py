#! /usr/bin/python
with open('test2.txt', 'r') as txtfile:
  data = txtfile.read().strip().split('\n')

  valid_phrases = 0
  valid_anagrams = 0

  for line in data:
    pieces = line.split(' ')

    # part 1
    unique_pieces = set(pieces)
    if len(pieces) == len(unique_pieces):
      valid_phrases += 1

    # part 2
    for index, item in enumerate(pieces):
      pieces[index] = ''.join(sorted(item))

    unique_sorted = set(pieces)
    if len(pieces) == len(unique_sorted):
      valid_anagrams += 1

  print valid_phrases
  print valid_anagrams

