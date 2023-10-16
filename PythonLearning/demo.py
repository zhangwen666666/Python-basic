# age = 18
# height = 180
# message = "我今年%d岁了，身高%dcm" % (age,height)
# print(message)

# name = "张文"
# age = 23
# height = 1.80
# school_name = "天津理工大学"
# print(f"我叫{name},我今年{age}岁了,我身高{height}m,就读于{school_name}")

# name = input("请告诉我你是谁：")
# print(f"我知道了，你是{name}")
# print(10 == 20)

# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print("sum = ", sum)

# import random
# gess_num = random.randint(1,100)
# count = 0
# while True:
#     count += 1
#     num = int(input("请输入你猜的数字（1-100）："))
#     if num == gess_num:
#         print(f"恭喜你猜了{count}轮之后，猜中了")
#         break
#     elif num > gess_num:
#         print("你猜大了")
#     else:
#         print("你猜小了")


# i = 1
# while i <= 9:
#     j = 1
#
#     while j <= i:
#         print("%d*%d=%2d" % (j, i, j * i), end='  ')
#         j += 1
#     i += 1
#     print("")

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%d*%d=%-2d" % (j, i, j * i), end=' ')
#     print()

# str1 = "123jkh"
#
#
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print("{}的长度是{}".format(data, count))
#     return count
#
# len1 = my_len(str1)
# print(f"len = {len1}")


# person = {'name': 'zhangsan', 'age': 18, 'height': 100}
# for x in person:
#     print(x, '=', person[x], end='    ')

# age_list = [21, 25, 21, 23, 22, 20]
# age_list.append(31)
# print(age_list)
# age_list.extend([29, 33, 30])
# print(age_list)
# age_list.pop(0)
# print(age_list)
# age_list.pop(-1)
# print(age_list)
# print(age_list.index(31))

# age = [12, 15, 3, 45, 78, 65, 2, 11]
# i = 0
# while i < len(age):
#     print(age[i])
#     i += 1
#
# for i in age:
#     print(i, end=' ')


# str1 = "itheima itcast boxuegu"
# # 统计字符串中有多少个it字符
# count = str1.count("it")
# print(count)
# str1 = str1.replace(" ", "|")
# print(str1)
# ret = str1.split("|")
# print(ret)

# my_list = [1, 5, 3, 8, 4, 7]
# my_tuple = (1, 2, 3, 4, 5)
# my_str = "abcdef"
# my_set = {1, 2, 3, 4, 5}
# my_dict = {'key1': 5, 'key2': 4, 'key3': 3, 'key4': 2, 'key5': 1}
#
# print(f"列表 转元组\t{str(my_list)}")
# print(f"元组 转元组\t{str(my_tuple)}")
# print(f"字符串转元组\t{str(my_str)}")
# print(f"集合 转元组\t{str(my_set)}")
# print(f"字典 转元组\t{str(my_dict)}")
#
# # print(f"列表转列表\t{list(my_list)}")
# # print(f"元组转列表\t{list(my_tuple)}")
# # print(f"字符串转列表\t{list(my_str)}")
# # print(f"集合转列表\t{list(my_set)}")
# # print(f"字典转列表\t{list(my_dict)}")
#
# new_list = sorted(my_list,reverse=False)
# print(my_list)
# print(new_list)

# print(my_list)
# print(my_tuple)
# print(my_str)
# print(my_set)
# print(my_dict)


# f = open("./测试.txt", "r", encoding="UTF-8")
# # print(f.read(20))
# # print(f.read(20))
# # print(f.readlines())
# for line in f:
#     print(line)
# f.close()

# f = open("./测试.txt", 'r', encoding="UTF-8")
# count = 0
# for line in f:
#     print(line)
#     count += line.count("itheima")
# f.close()
# print("itheima出现的次数是%d" % count)

# f = open("./text.txt","w",encoding="UTF-8")
# f.write("你好世界")
# f.flush()
# f.close()

# fr = open("bill.txt", 'r', encoding="UTF-8")
# fw = open("bill.txt.bat", 'w', encoding="UTF-8")
# for line in fr:
#     # print(line)
#     new_line = line.strip()  # 去掉换行符
#     # print(new_line)
#     words = new_line.split(',')
#     if words[-1] == '测试':
#         continue
#     fw.write(line)
#     # print(words)
# fw.close()
# fr.close()

import numpy

A = [[2, 1, 3], [3, 1, 4], [5, 7, 12]]
A = numpy.array(A)
# print(A)
# print(A.shape)
x = numpy.random.random(size=(3,1))
print(x)