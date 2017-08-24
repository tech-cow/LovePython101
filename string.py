#!/usr/bin/python
# -*- coding: utf-8 -*-

#Strings

#第一步
print 'yu zhou'


#第二步, Variable的运用
# 知识点：
# 1. 讲一下python是不需要 ; 结尾的
# 2. 命名的重要性，为什么不取名 x
# 3. 什么是一个variable
# 4. Single Quote vs. Double Quote  message = 'yu's phone' ,假如single quote不得劲，就用double， double不得劲，就用single


last_word = 'Iloveyou'
print last_word

#第三步， 字符串长度

print len(last_word)


#第4步， 字符串里面的access一个数
#解释3为什么不是o，而是v，因为字符串是从0开始算起
print last_word[3]

#第5步，index out of range讲解
# print last_word[10]


#第6步，字符串里面的access多个数
# 这里叫学员，自己去尝试slice的规律，inclusive or exclusive

print last_word[:5]  # Ilove
print last_word[5:] # you

#Method vs function
#第7步，string method， lowercase

print last_word.lower()
print last_word.upper()


#第8步，Count Method/ Find
print "8.-------"
print last_word.count('l')
print last_word.find('y')
print last_word.find('z') #解释-1

#第9步， replace   in place/ not in place
last_word.replace('I', 'Yu')
print last_word
print last_word.replace('I', 'Yu')



# 第10步： combine, placeholder

first = 'yu'
last = 'zhou'
name = first + ' ' + last
name2 = '{} {}'.format(first, last)

print name
print name2


#第11步： dir
print dir(name)






#作业： 把 name: yu zhou变成   Yu Zhou
