#! /usr/bin/python
import csv
from itertools import cycle, islice

with open('input.tsv', 'r') as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
    row = [int(item) for item in row]

    results = []
    current_item = 0
    current_list = row
    num_of_cycles = 0

    while results.count(current_list) < 2:
      max_value = max(current_list)
      current_item = current_list.index(max_value) # this will return the first occurrence if there's duplicates
      current_value = current_list[current_item]
      current_list[current_item] = 0

      for i, v in islice(cycle(enumerate(current_list, current_item+1)), current_value):
        index_to_modify = i
        if i > (len(current_list) - 1):
          index_to_modify = i - len(current_list)

        current_list[index_to_modify] += 1

      results.append(list(current_list))
      num_of_cycles += 1

    # part 1
    print num_of_cycles

    # part 2
    indices = [i for i,x in enumerate(results) if x == current_list]
    print indices[1] - indices[0]
