#!/usr/bin/env python

import math
class Circle:
  def __init__(self, rad):
      self.radius = rad

  def get_area(self):
      return math.pi * (self.radius ** 2)

  def get_circumference(self):
      return 2 * math.pi * self.radius
