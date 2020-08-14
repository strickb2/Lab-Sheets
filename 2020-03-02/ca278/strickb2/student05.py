#!/usr/bin/env python

import students

class Student:
  def __init__(self, name, exam, ca):
      self.name = name
      self.exam = exam
      self.ca = ca

  def get_average(self):
      return (self.exam + self.ca) / 2

  def __str__(self):
      id = input("Id:")
      return id, n("Name:"), s.get_average("Average:")

  if __name__ == '__main__':
      f = open("students.txt", "r")
      s = Student(name, exam, ca)
      exam = students.txt.split(",")[1]
      ca = students.txt.split(",")[2]

