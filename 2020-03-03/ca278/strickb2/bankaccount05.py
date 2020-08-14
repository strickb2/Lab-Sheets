#!/usr/bin/env python

class BankAccount:
  id_counter = 0
  balance = 0

  def __init__(self, balance):
     BankAccount.balance = balance
     self.balance = BankAccount.balance
     BankAccount.id_counter += 1
     self.id = BankAccount.id_counter

  def __str__(self):
     return "Account number: " + str(self.id) + "\nBalance: " + str(self.balance)

  def lodge(self, amount):
     self.l_amount = amount
     BankAccount.balance = BankAccount.balance + self.l_amount
     self.balance = BankAccount.balance

  def withdraw(self, amount):
     self.w_amount = amount
     BankAccount.balance = BankAccount.balance - self.w_amount
     self.balance = BankAccount.balance

acc1 = BankAccount(1000)
acc2 = BankAccount(1500)

print acc1.__str__()
print acc2.__str__()

acc2.withdraw(500)
acc1.lodge(500)

print acc1.__str__()
print acc2.__str__()
