# import Module1
import time

# import time
#
# time.sleep(10)

# import my_util.str_util
# from my_util import file_util
#
# str1 = "HelloWord"
# str2 = my_util.str_util.str_reverse(str1)
# print(str2)
# str2 = my_util.str_util.substr(str1, 1, 5)
# print(str2)
#
# file_util.print_file_info("./text.txt")
# file_util.append_to_file("./text.txt", 'hrojojsfod')

# import json
#
# data = [{"name": "zhangsan", "age": 12}, {"name": "lisi", "age": 18}, {"name": "王五", "age": 23}]
# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))

# class Student:
#
#     def say_hi(self):
#         print(f"大家好，我叫{self.name}")
#
#
# s1 = Student();
# s1.name = "zhoujielun"
# s1.say_hi()

# class Student(object):
#     __slots__ = ('name', 'age')
#
#     def __init__(self, x, y):
#         self.name = x
#         self.age = y
#
#
# s1 = Student("张三", 18)
# s1.city = "上海"  # 报错

# import time
#
#
# class Student(object):
#     def __init__(self, x, y):
#         # 对象创建的时候会自动调用
#         # print("__init__方法被调用了")
#         self.name = x
#         self.age = y
#
#     # def __del__(self):
#     # 对象销毁的时候会自动调用
#     # print("__del__方法调用了")
#
#     def __repr__(self):
#         return "__repr__"
#
#     def __str__(self):
#         return "__str__"
#
#     def __call__(self, *args, **kwargs):
#         print("__call__")
#
#     def __eq__(self, other):
#         if self.name == other.name and self.age == other.age:
#             return True
#         return False
#
# s1 = Student("张三", 18)
# s2 = Student("张三", 18)
# print(s1 == s2)  # True
# print(s1 is s2)  # False
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# print(l1 is l2)  # False
#
# print(l1 == l2)  # True
# s1()
# print(s1)
# print(repr(s1))
# print(s1.__repr__())


import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0, 1, -1], [-1, 0, 1]])

# 奇异值分解
U, s, V = np.linalg.svd(A)

# 零空间和左零空间的基向量
null_space = V[-1]
left_null_space = U[:, -1]

# 创建一个三维图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制零空间中的向量
ax.quiver(0, 0, 0, null_space[0], null_space[1], null_space[2], color='blue')

# 绘制左零空间中的向量
ax.quiver(0, 0, 0, left_null_space[0], left_null_space[1], 0, color='red')

# 列空间和行空间的基向量
column_space = np.linalg.qr(A)[0]
row_space = np.linalg.qr(A.T)[0]

# 绘制列空间中的向量
for vector in column_space.T:
    ax.quiver(0, 0, 0, vector[0], vector[1], 0, color='green')

# 绘制行空间中的向量
for vector in row_space.T:
    ax.quiver(0, 0, 0, vector[0], vector[1], 0, color='black')

# 设置坐标轴范围
ax.set_xlim([-0.5, 1])
ax.set_ylim([-0.5, 1])
ax.set_zlim([-0.5, 1])

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()