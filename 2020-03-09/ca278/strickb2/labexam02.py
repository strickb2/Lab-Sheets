#!/usr/bin/env python

import sys

with open(sys.argv[1], "r") as f:
  li = f.readlines()

i = 0
while i < len(li):
  first = li[i].split()
  print first[0]
  i = i + 1
