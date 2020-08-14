#!/usr/bin/env python

import time

def countdown(num):
  if num == 0:
    print "LIFT OFF!"
  else:
    print num
    time.sleep(0.1)
    num = num - 1
    countdown(num)
    
def search(the_str,letter):
  if the_str == "":
    return False
  elif the_str[0] == letter:
    return True
  else:
    return search(the_str[1:],letter)
    
def previous_two(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  else:
    return previous_two(n-1) + previous_two(n-2)
    