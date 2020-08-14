#!/usr/bin/env python

import sys

minage = {
  "austria": 16,
  "ecudor": 16,
  "north korea": 17,
  "sudan": 17,
  "ireland": 18,
  "portugal": 18,
  "russia": 18,
  "cameroon": 20,
  "bahrain": 20,
  "lebanon": 21
}

x = input("How old are you?")
y = raw_input("Where are you from?")

if y.lower() in minage and minage[y.lower()] > x:
  print "You cannot vote"
elif y.lower() in minage and minage[y.lower()] <= x:
  print "You can vote"
elif y.lower() not in minage:
  print "I do not know whether you can vote"
