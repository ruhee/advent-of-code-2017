#! /usr/bin/python
import csv

differences = []
results = []

def get_difference(row):
  return row[(len(row)-1)] - row[0]

with open('input.tsv', 'r') as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')

  for row in reader:
    int_row = [int(item) for item in row]

    # part 1
    int_row.sort()
    differences.append(get_difference(int_row))

    # part 2
    for idx, val in enumerate(int_row):
      for i, v in enumerate(int_row):
        if (val % v == 0 and idx != i):
          results.append(val/v)

  print sum(differences)
  print sum(results)

