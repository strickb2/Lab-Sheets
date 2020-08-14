#!/usr/bin/env python

class Employee:
  def __init__(self, n, jd, s):
      self.name = n
      self.job_desc = jd
      self.salary = s

  def net_salary(self):
      return self.salary - (self.salary * .2)

if __name__ == '__main__':
    n = raw_input('Enter the employee name:\n')
    jd = raw_input('Enter the employee job description:\n')
    s = input('Enter the employee salary:\n')

    e = Employee(n,jd,s)

    print 'Net Salary:', e.net_salary()
