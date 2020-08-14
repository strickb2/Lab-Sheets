#!/usr/bin/env python

import sys

vote = {}

with open('countries.txt') as f:
  s = f.readlines()
  i = 0
  while i < len(s):
    token = s[i].strip().split(':')
    age = int(token[1])
    if ',' in token[0]:
      countries = token[0].split(',')
      status = True 
    else:
      countries = token[0]
      status = False

    if status == True:
      w = 0
      while w < len(countries):
        vote[countries[w].lower().strip()] = age
        w = w + 1
    elif status == False:
      vote[countries[w].lower().strip()] = age
    i = i + 1

s = raw_input("Enter name,age,country:")

token = s.split(",")

print "Hello", token[0]

if token[2].lower() in vote:
  if int(token[1]) >= int(vote[token[2].lower()]):
    print "You can vote"
  else:
    print "You cannot vote"
else:
  print "I do not know whether you can vote"
