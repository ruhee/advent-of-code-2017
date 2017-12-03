#! /usr/bin/python
import csv

differences = []

def get_difference(row):
  return row[(len(row)-1)] - row[0]

with open('input.tsv', 'r') as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')

  for row in reader:
    int_row = [int(item) for item in row]
    int_row.sort()
    differences.append(get_difference(int_row))

  print sum(differences)


