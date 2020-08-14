#!/usr/bin/env python

l = []

n = input("Please enter a number (-1 to stop):")

while n != -1:
  if n not in l:
    l.append(n)
  n = input("Please enter a number (-1 to stop):")

print l
