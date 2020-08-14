#!/usr/bin/env python

import sys

with open(sys.argv[1], "r") as f:
  li = f.readlines()

last = raw_input("Please enter a surname:")

i = 0
first = []
while i < len(li):
  name = li[i].split()
  if last.lower() == name[1].lower():
    first.append(name[0])
  i = i + 1

if len(first) == 0:
  print "No-one has that surname"
else:
  print first
