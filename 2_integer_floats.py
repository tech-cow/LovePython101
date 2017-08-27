#!/usr/bin/python
# -*- coding: utf-8 -*-

#第二课， 加减乘除，Integer/Floats


# String
# num1 = "20"
# num2 = "30"
# print num1 + num2


#加
print 3 + 2
#减
print 3 - 4
#乘
print 3 * 4

#除
# 讲明白这里面的 3/2 和 3/2.0 的区别
# 2.0英语的梗
print 3 / 2
print 3 / 2.0
print 3 / float(2)


# Exponential
print 3 ** 3

# Modulus
# 确认一个数是基数还是偶数 ， 是否能被整除
# 举例： fizzbuzz
print 3 % 2



#大杂烩
print 3 * (2+1)


# Count增加
num = 1
num = num + 1
num += 1
print num
num *= 10
print num
num //= 5
print num


#绝对值
print abs(-100)

#round
print round(3.99, 1)


# String casting
num1 = int("20")
num2 = int("30")
print num1 + num2




#草船借箭
# 好了，诸葛亮要牛逼逼的去干一票大的，奈何他的数学智商为0，他需要10万之箭
# 目前市场上只能通过江湖奸商购买稻草人来装箭， 诸葛亮不知道自己最少需要多少钱
# 才能买到足够的稻草人。
# 他只能求助聪明的周瑜（也就是你），来帮忙计算最终的价格
#
# 价格如下，聪明的周瑜，请问诸葛亮一共需要多少钱(四舍五入哟)才能去借箭呢？

# 计算机给出了江湖奸商的价格表格：

# 品种               载重           数量           价格
# 普通稻草人          500           x无限          100
# VIP稻草人          1532           x5            150
# Maggie专用稻草人   2000           x1             1

p_maggie = 1
p_vip = 150*5
quan_reg = (100000 - 2000 - (1532*5)) / 500.0   #记得提醒float操作
p_reg = round(quan_reg) * 100  #数量需要整数
total = p_vip + p_maggie + p_reg
print total
