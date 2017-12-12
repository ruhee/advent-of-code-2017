#! /usr/bin/python
import re

with open('input.txt', 'r') as txtfile:
  data = txtfile.read().strip().split('\n')

  flat_list = []

  for row in data:
    row = re.sub(r'(\(\d+\))', '', row).split('->')
    for i, v in enumerate(row):
      row[i] = v.strip().split(',')

    for item in row:
      for val in item:
        flat_list.append(val.strip())

  counts = dict((x,flat_list.count(x)) for x in set(flat_list))
  for k, v in counts.iteritems():
    if v == 1:
      print k

# This is stupid.

# The bottom program is the only one that appears only one time in the list,
# because other items appear once when they are listed themselves, and once more when
# they're listed as being directly above another item.
# So this returns the only item that is listed once.
# :|