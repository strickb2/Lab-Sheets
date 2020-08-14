#!/usr/bin/env python

import sys

class ShopItem:
    def __init__(self, description, price, is_discounted=False):
        self.description = description
        self.price = float(price)
        self.is_discounted = is_discounted
        
    def get_price(self):
        if self.is_discounted == True:
            return self.price * 0.8
        else:
            return self.price
            
    def __str__(self):
        return self.description + " (" + str(self.get_price())+ " euro)"
        
with open(sys.argv[1], "r") as f:
    contents = f.readlines()
    for content in contents:
        if "discount" in content:
            description, price, is_discounted = content.strip().split(",")
            is_discounted = True
            item = ShopItem(description, price, is_discounted)
            print item.__str__()
        else:
            description, price = content.strip().split(",")
            item = ShopItem(description, price)
            print item.__str__()