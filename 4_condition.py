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
#player = ['wolf','wolf','wolf','seer','witch','dumb','fart villager','fart villager','fart villager']
#把白痴牌换成了守卫牌：
player = ['wolf','wolf','wolf','seer','witch','sheild','fart villager','fart villager','fart villager']


#狼人请睁眼
temp = input("狼人请睁眼，请选择猎杀目标:  ")

#女巫请睁眼
isSave = input('女巫请睁眼，救人请输入1，不救人请输入0:  ')

#当白痴牌被换成了守卫牌，守卫请睁眼
sheild = input('守卫请睁眼，选择守护的人是:  ')

#白痴版上帝发言1
def annocement1():
    if isSave == True:
        print '昨晚平安夜'
    else:
        identity = player.pop(temp)
        print '昨晚' + str(temp) + '玩家死亡, 他的身份是: ' + identity
    print player

#白痴版上帝发言2
def annocement2():
    if isSave is True:
        print '昨晚平安夜'
    else:
        identity = player.pop(temp)
        print '昨晚' + str(temp) + '玩家死亡, 他的身份是: ' + identity
    print player

#白痴版上帝发言3
def annocement3():
    if isSave:
        print '昨晚平安夜'
    else:
        identity = player.pop(temp)
        print '昨晚' + str(temp) + '玩家死亡, 他的身份是: ' + identity
    print player

#守卫版上帝发言:
def annocement4():
    if isSave and sheild is temp:
        identity = player.pop(temp)
        print '昨晚' + str(temp) + '玩家死亡, 他的身份是: ' + identity
    elif isSave or sheild is temp:
        print '昨晚平安夜'
    else:
        identity = player.pop(temp)
        print '昨晚' + str(temp) + '玩家死亡, 他的身份是: ' + identity
    print player

annocement4()





#高端大气上档次的狼人识别器
wolfMentra = ['我就不说我的身份了，我是民，还是狼，你们去猜?',
              '我是一头村民','我是一只……呸，一个狼……不对不对……我是一只民……',
              '昨天晚上是平安夜，可能女巫救人了，也可能昨天守卫正好守中1号了吧。',
              '好人都退水，让那个真预言家跟我对跳!',
              '我是村民，你们好人为什么不相信我?',
              '我从头到尾跟着好人玩，为什么怀疑我',
              '我悍跳预言家',
              '我是预言家，昨晚验的是6号，他是一个猎人。',
              '我是一头真的预言家，不信你晚上来验我(手动滑稽)',
              '这个女巫肯定是假的!我们昨晚明明杀的就不是五号!']

speech = "我悍跳预言"
isBuy = input("该玩家请客吃饭了么？")
face = input("该玩家是否颜值爆棚，请从1-10进行打分:  ")
nice = input("该玩家是否和蔼可亲，请从1-10进行打分:  ")

#Edge Cases:
if speech not in wolfMentra:
    print "...机器故障"
    quit()

if isBuy:
    print '恭喜你，你成功的活到了最后'
    quit()

if face > 8 or nice > 8:
    print "恭喜你，你成功的活到了最后"
else:
    print "恭喜你滚动出局"
