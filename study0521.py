#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 2.9

if a >= 0:
    print("yes")
else:
    print("no")

# \n 表示换行
# \t 表示一个制表符
# \\ 表示 \ 字符本身
a = 'hello \n刘德华'
print(a)

# 布尔值True False
# 布尔值可以用 : and、or 和 not
a = True
print(a)

# a = b = c = 1
# a, b, c = 1, 2, "liangdianshui"
# print(a,b,c)

list1 = ['hello', 123, 'thehsy']
# 访问 List（列表）中的值
print(list1[2])
print(list1[0:2])
# 更新list
list1[2] = 'rookie'
print(list1[2])
list1.append("jackylove")
print(list1)
# 删除list
del list1[1]
print(list1)
# list1的长度
print(len(list1))

# tuple（元组）
# uple 不可变是指当你创建了 tuple 时候，它就不能改变了，也就是说它也没有 append()，insert() 这样的方法，但它也有获取某个索引值的方法，但是不能赋值。
# 那么为什么要有 tuple 呢？那是因为 tuple 是不可变的，所以代码更安全
tuple1 = ('letme', 'mlxg', 'xiaohu', 'ming', 'uzi')
print(tuple1)
del tuple1


print('---------------------------------')


# 字典
# dict 全称dictionary，相当于 JAVA 中的 map，使用键-值（key-value）存储，具有极快的查找速度
userInfo = {'theshy': '0001', 'rookie': '0002'}
print(userInfo)
# 添加值
userInfo['baolan'] = '0003'
print(userInfo)
# 修改键值对
userInfo['baolan'] = '0004'
print(userInfo)
# 删除 dict （字典）
del userInfo['baolan']
print(userInfo)
# del userInfo
userInfo.clear()
print(userInfo)

print('---------------------------------')

# set 是无序不重复元素集, 基本功能包括关系测试和消除重复元素。set 和 dict 类似，但是 set 不存储 value 值的。
set1 = set([123, 456, 789])
print('set1 : ' + str(set1))
# 添加元素
set1.add(246)
print(set1)
# 删除元素
set1.remove(246)
print(set1)

print('---------------------------------')

# 条件语句
result = 89
if result > 60:
    print("及格")
elif result > 90:
    print('优秀')
else:
    print('不及格')

print('---------------------------------')

# for循环语句
for hello in range(1, 10):
    print(hello)

print('---------------------------------')

# 函数
def sum(num1, num2):
    "两数之和"
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        return "数据类型不正确"
    return num1 + num2


print(sum(3, 21))
print(sum("", 21))

print('---------------------------------')

# 函数也可以返回多个值
def division(num1, num2):
    # 求商与余数
    a = num1 % num2
    b = (num1 - a) / num2
    return b, a


num1, num2 = division(9, 4)
tuple1 = division(9, 4)
print(num1, num2)
print(tuple1)



# 默认值参数 sex有默认值
def print_user_info(name, age, sex='男'):
    # 打印用户信息
    print('昵称：{}'.format(name))
    print('年龄：{}'.format(age))
    print('性别：{}'.format(sex))
    return;


print('---------------------------------')
# list生成器
lsit1=[x * x for x in range(1, 11)]
print(lsit1)
lsit2=[x * x for x in range(1,11) if x % 2 == 0]
print(lsit2)