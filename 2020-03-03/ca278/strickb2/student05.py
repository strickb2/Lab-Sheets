#!/usr/bin/env python


class student:
  id_counter = 0
  def __init__(self, name, exam, ca):
     student.id_counter = student.id_counter + 1
     self.id = student.id_counter
     self.name = name
     self.exam = float(exam)
     self.ca = float(ca)

  def get_average(self):
    return float((self.exam + self.ca) / 2)

  def __str__(self):
    return "Id: " + str(self.id) + ", " + "Name: " + self.name + ", " + "Average: " + str(self.get_average())

with open("students.txt", "r") as f:
  li = f.readlines()

j = 0
for i in li:
  line_li = li[j].split(",")
  print student(line_li[0],line_li[1],line_li[2])
  j = j + 1
