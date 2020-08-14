#!/usr/bin/env python

minage = {
  "austria": 16,
  "ecudor": 16,
  "north korea": 17,
  "sudan": 17,
  "ireland": 18,
  "portugal": 18,
  "russia": 18,
  "cameroon": 20,
  "bahrain": 20,
  "lebanon": 21
}

m = raw_input("Enter name,age,country:")
infolist = m.split(",")

name=infolist[0]
age=int(infolist[1])
country=infolist[2]

print "Hello " + infolist[0]

if country.lower() in minage and age >= minage[country]:
  print "You can vote"
elif country.lower() in minage and age < minage[country]:
  print "You cannot vote"
elif country.lower() not in minage:
  print "I do not know whether you can vote"
