#!/usr/bin/python
# -*- coding: utf-8 -*-


cards = ['预言家', '女巫', '猎人', '白痴','平民']
actions = ['闭眼',"睁眼","发动技能","死亡"]

# Step 1:
for card in cards:
    break
    print card

# vs

for i in xrange(0,len(cards)):
    print i

for i , card in enumerate(cards):
    print str(i) + card

# Step 2:
for card in cards:
    break
    if card == '女巫':
        print card + '，今晚干掉你'
        break
    print card

# Step 3:
for card in cards:
    break
    if card == '猎人':
        print card + ', 怕了你，不敢动你'
        continue
    print card

# Step 4
for card in cards:
    for action in actions:
        # if card == '平民' and action == '发动技能':
        #     continue
        print card + '请' + action


# While
i = 0
while cards[i] is not '猎人':
    i += 1
    print i
