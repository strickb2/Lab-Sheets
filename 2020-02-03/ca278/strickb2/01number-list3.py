#!/usr/bin/env python

l = []
m = {}
n = 0

while n != -1:
  n = input("Please enter a number (-1 to stop):")
  if n not in l:
    l.append(n)
  if n != -1:
    if n not in m:
      m[n] = 0
    if n in m:
      m[n] += 1

print l[0:len(l)-1]
for key in m:
  print key, "occurred", m[key], "times"
