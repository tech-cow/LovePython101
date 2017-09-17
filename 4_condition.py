#!/usr/bin/python
# -*- coding: utf-8 -*-

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

#上帝视角
player = ['wolf','wolf','wolf','seer','witch','hunter','fart villager','fart villager','fart villager']

#狼人请睁眼
temp = input("狼人请睁眼，请选择猎杀目标")

#女巫请睁眼
isSave = input('女巫请睁眼，救人请输入1，不救人请输入0')

#上帝发言1
def annocement1():
    if isSave == True:
        print '昨晚平安夜'
    else:
        identity = player.pop(temp)
        print '昨晚' + str(temp) + '玩家死亡, 他的身份是: ' + identity
    print player

#上帝发言2
def annocement2():
    if isSave is True:
        print '昨晚平安夜'
    else:
        identity = player.pop(temp)
        print '昨晚' + str(temp) + '玩家死亡, 他的身份是: ' + identity
    print player

#上帝发言3
def annocement3():
    if isSave:
        print '昨晚平安夜'
    else:
        identity = player.pop(temp)
        print '昨晚' + str(temp) + '玩家死亡, 他的身份是: ' + identity
    print player

annocement3()
