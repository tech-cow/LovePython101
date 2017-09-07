#!/usr/bin/python
# -*- coding: utf-8 -*-
def space():
    print '\n'

menu = ["orange chicken", "chicken mian", "spicy chicken"]



#餐馆有几道菜？
print (len(menu))

#有哪些菜？
print menu

#Index
print menu[0]
print menu[-1]

#Slicing
print menu[:2]
print menu[1:]

#店面扩张，加菜
menu.append("sweet&sour chicken")
print menu
menu.insert(0, 'choe meain')
print menu


#菜不好吃，减菜
nasty = menu.pop()
print nasty
print menu

#New space sorting,不更改原来的List
nums = [3,4,2,1,5]
new = sorted(nums)
print new
print nums

# In-place sorting
nums.sort()
print nums

print nums[::-1]

#min,max,sum
print min(nums)
print max(nums)
print sum(nums)

# 菜和index展示
count = 0
for item in menu:
    print count, item
    count += 1

for index, food in enumerate(menu):
    print index, food


# Join: list to string

menu_str = ' - '.join(menu)
print menu_str

# split: string to List
new_list = menu_str.split(' - ')
print new_list


#Mutable vs. Immutable
new_menu = menu[]
# vs.
new_menu = menu[:]
new_menu[0] = 'idk'
print menu
