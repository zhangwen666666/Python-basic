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

# import numpy
#
# A = [[2, 1, 3], [3, 1, 4], [5, 7, 12]]
# A = numpy.array(A)
# # print(A)
# # print(A.shape)
# x = numpy.random.random(size=(3,1))
# print(x)

# try:
#     f = open("homework.txt", 'r')
# except:
#     f = open("homework.txt", 'w')

# try:
#     print(name)
#     # print("hello")
# except NameError:
#     print("出现了变量未定义异常")
# else:
#     print("没有异常")
# finally:
#     print("我都要执行")


# import numpy as np
# import matplotlib.pyplot as plt
#
# A = [[2, 1, 3], [3, 1, 4], [5, 7, 12]]
# A = np.array(A)
# # print(A)
# # print(A.shape)
# x = np.random.uniform(low=-1.0, high=1.0, size=(3, 1000))
#
# LA = np.dot(A, x)
# # print(A)
# # print(x)
# # print(LA)
#
# # plt.plot(x,LA)
# # plt.show()
#
#
# from mpl_toolkits.mplot3d import Axes3D  # 绘制3D图案
# print(A.shape)
# print(x.shape)
# A_, x_, = np.meshgrid(A, x, indexing='ij')
# print(A_.shape)
# print(x_.shape)
# # LA_ = np.dot(A_, x_)  # 画图所要表现出来的主函数
# fig = plt.figure(figsize=(10, 10), facecolor='white')  # 创建图片
# sub = fig.add_subplot(111, projection='3d')  # 添加子图，
# surf = sub.plot_surface(A, x, LA, cmap=plt.cm.brg)  # 绘制曲面,cmap=plt.cm.brg并设置颜色cmap
# cb = fig.colorbar(surf, shrink=0.8, aspect=15)  # 设置颜色棒

# import numpy as np
# import matplotlib.pyplot as plt
#
# # 随机生成一个2维向量x
# x = np.random.rand(2)
# print("随机向量x:", x)
#
# # 定义一个2x2矩阵A
# A = np.array([[1, 2], [3, 4]])
# print("矩阵A:\n", A)
#
# # 计算L=Ax
# L = np.dot(A, x)
# print("计算出的L:", L)
#
# # 在平面直角坐标系上标出两个点
# x1, y1 = L[0], L[1]
# x2, y2 = x[0], x[1]
# plt.scatter([x1, x2], [y1, y2], color='red')
#
# # 用直线连接两个点
# plt.plot([x1, x2], [y1, y2], color='blue')
# plt.text(x1, y1, str((x1, y1)), fontsize=10)
# plt.text(x2, y2, str((x2, y2)), fontsize=10)
# plt.title("L=Ax")
# plt.xlabel("x1")
# plt.ylabel("y1")
# plt.grid(True)
# plt.show()
# A = A.T
# # 随机生成一个2维向量x
# x = np.random.rand(2)
# print("随机向量x:", x)
#
# # 定义一个2x2矩阵A
# A = np.array([[1, 2], [3, 4]])
# print("矩阵A:\n", A)
#
# # 计算L=Ax
# L = np.dot(A, x)
# print("计算出的L:", L)
#
# # 在平面直角坐标系上标出两个点
# x1, y1 = L[0], L[1]
# x2, y2 = x[0], x[1]
# plt.scatter([x1, x2], [y1, y2], color='red')
#
# # 用直线连接两个点
# plt.plot([x1, x2], [y1, y2], color='blue')
# plt.text(x1, y1, str((x1, y1)), fontsize=10)
# plt.text(x2, y2, str((x2, y2)), fontsize=10)
# plt.title("L=Ax")
# plt.xlabel("x1")
# plt.ylabel("y1")
# plt.grid(True)
# plt.show()

# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
#
# # 随机生成一个3维向量x
# x = np.random.rand(3)
# print("随机向量x:", x)
#
# # 定义一个3x3矩阵A
# A = np.array([[2, 1, 3], [3, 1, 4], [5, 7, 12]])
# # print("矩阵A:\n", A)
#
# # 计算L=Ax
# L1 = np.dot(A, x)
# L2 = np.dot(A.T, x)
# print("计算出的L1:", L1)
# print("计算出的L2:", L2)
#
# # 在三维空间直角坐标系上标出两个点
# x11, y11, z11 = L1[0], L1[1], L1[2]
# x22, y22, z22 = L2[0], L2[1], L2[2]
# x2, y2, z2 = x[0], x[1], x[2]
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter([x11, x2], [y11, y2], [z11, z2], color='red')
# ax.scatter([x22, x2], [y22, y2], [z22, z2], color='yellow')
#
# # 用直线连接两个点
# ax.plot([x11, x2], [y11, y2], [z11, z2], color='blue',label="L=Ax")
# ax.plot([x22, x2], [y22, y2], [z22, z2], color='green',label="L=ATx")
# ax.text(x11, y11, z11, str((x11, y11, z11)), fontsize=10)
# ax.text(x22, y22, z22, str((x22, y22, z22)), fontsize=10)
# ax.text(x2, y2, z2, str((x2, y2, z2)), fontsize=10)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # 生成数据
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)
# X, Y = np.meshgrid(x, y)
# Z1 = np.sin(np.sqrt(X ** 2 + Y ** 2))
# Z2 = np.cos(np.sqrt(X ** 2 + Y ** 2))
#
# # 创建一个3D图形
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # 在这个图形中画第一个曲面
# ax.plot_surface(X, Y, Z1, cmap='viridis')
# # 在这个图形中画第二个曲面
# ax.plot_surface(X, Y, Z2, cmap='viridis')
#
# ax.set_title('Two surfaces in 3D plot')
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
#
# A = np.array([[0, 1, -1], [-1, 0, 1]])
#
# # 列空间和行空间的基
# column = np.linalg.qr(A)[0]
# row = np.linalg.qr(A.T)[0]
#
# # 创建一个二维图形
# fig, ax = plt.subplots()
#
# # 绘制列空间中的向量
# for vector in column.T:
#     ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='green')
#
# # 绘制行空间中的向量
# for vector in row.T:
#     ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='red')
#
# # 设置坐标轴范围
# ax.set_xlim([-1, 1])
# ax.set_ylim([-1, 1])
#
# # 设置坐标轴标签
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
#
# # 显示图形
# plt.show()
#
#
# # 奇异值分解
# U, s, Vt = np.linalg.svd(A)
#
# # 零空间和左零空间的基向量
# null = Vt[-1]
# left_null = U[:, -1]
#
# # 创建一个三维图形
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # 绘制零空间中的向量
# ax.quiver(0, 0, 0, null[0], null[1], null[2], color='green')
#
# # 绘制左零空间中的向量
# ax.quiver(0, 0, 0, left_null[0], left_null[1], 0, color='red')
#
# # 设置坐标轴范围
# ax.set_xlim([-1, 1])
# ax.set_ylim([-1, 1])
# ax.set_zlim([-1, 1])
#
# # 设置坐标轴标签
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# # 显示图形
# plt.show()