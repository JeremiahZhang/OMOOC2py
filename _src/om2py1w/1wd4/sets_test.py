# -*- coding: utf-8 -*-
import math
# sets have no duplicate elements, USE in
# - membership testing
# - eliminating duplicate entries.
# set()
# set(list)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket) # no duplicate
print fruit
print 'orange' in fruit
print 'berry' in fruit

apple = set('appleappleappleapple')
bear = set('bearbearbear')
print apple
print bear

print apple - bear

print apple|bear
print apple&bear
print apple^bear

a = {x for x in 'apple' if x not in "bear"}
print a