#!/usr/bin/env python

x = raw_input("Please enter a list of scores:").split()

i = 0
draws = 0
losses = 0
wins = 0
while i < len(x):
  if x[i] == "3":
    wins = wins + 1
  if x[i] == "1":
    draws = draws + 1
  if x[i] == "0":
    losses = losses + 1
  i = i + 1

print "Draws:", draws
print "Losses:", losses
print "Wins:", wins
