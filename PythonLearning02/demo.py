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


# import numpy as np
# import matplotlib.pyplot as plt
#
# A = np.array([[0, 1, -1], [-1, 0, 1]])
#
# # 奇异值分解
# U, s, V = np.linalg.svd(A)
#
# # 零空间和左零空间的基向量
# null_space = V[-1]
# left_null_space = U[:, -1]
#
# # 创建一个三维图形
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # 绘制零空间中的向量
# ax.quiver(0, 0, 0, null_space[0], null_space[1], null_space[2], color='blue')
#
# # 绘制左零空间中的向量
# ax.quiver(0, 0, 0, left_null_space[0], left_null_space[1], 0, color='red')
#
# # 列空间和行空间的基向量
# column_space = np.linalg.qr(A)[0]
# row_space = np.linalg.qr(A.T)[0]
#
# # 绘制列空间中的向量
# for vector in column_space.T:
#     ax.quiver(0, 0, 0, vector[0], vector[1], 0, color='green')
#
# # 绘制行空间中的向量
# for vector in row_space.T:
#     ax.quiver(0, 0, 0, vector[0], vector[1], 0, color='black')
#
# # 设置坐标轴范围
# ax.set_xlim([-0.5, 1])
# ax.set_ylim([-0.5, 1])
# ax.set_zlim([-0.5, 1])
#
# # 设置坐标轴标签
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# # 显示图形
# plt.show()


# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __gt__(self, other):
#         return self.age > other.age
#
#     def __ge__(self, other):
#         return self.age >= other.age
#
#     def __int__(self):
#         return 20
#
#
# s1 = Student("张三", 18)
# print(int(s1))  # 20
#
# s2 = Student("李四", 18)
# print(s1 >= s2)  # True
# print(s1 < s2)


# class Person(object):
#     """
#     这是一个人类
#     """
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(self.name + '正在吃饭')
#
#
# p = Person('张三', 18)
# print(dir(p))
# print(p.__dir__())
# print(p.__doc__)  # 这是一个人类
# print(p.__dict__)  # {'name': '张三', 'age': 18}
# print(p.__class__)  # <class '__main__.Person'>
# print(p.__module__)  # __main__


# class Student(object):
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#
#     def __setitem__(self, key, value):
#         # self.key = value  不会将原属性修改，而是会多一个self.key属性并且值为value
#         self.__dict__[key] = value
#
#     def __getitem__(self, item):
#         return self.__dict__[item]
#
# s1 = Student("张三", 25, "上海")  # {'name': '张三', 'age': 25, 'city': '上海'}
# print(s1['age'])    #25
#
# print(s1.__dict__)  # 把对象转换成为字典
# s1['name'] = "李四"
# print(s1.__dict__)  # {'name': '李四', 'age': 25, 'city': '上海'}


# class Student(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__money = 1000
#
#     def __demo(self):
#         print("私有函数__demo")
#
#     def test(self):
#         self.__money += 1000
#         self.__demo()
#
# s1 = Student("张三", 18)
# s1._Student__demo() #私有函数__demo
# s1.test()   #私有函数__demo
#
# print(s1.name, s1.age)
# print(s1._Student__money)   #1000

# print(Student.type)  # 'person'
# print(s1.type)  # 'person'
# print(s2.type)  # 'person'
# s1.type = 'human'  # 不会修改类属性type，而是s1对象多了一个对象属性type，值为'human'
# print(Student.type)  # 'person'
# print(s1.type)  # 'human'
# print(s2.type)  # 'person'
# print(s1.__dict__)  # {'name': '张三', 'age': 18, 'type': 'human'}
# print(s2.__dict__)  # {'name': '李四', 'age': 29}
# # 对象s1和s2都是由Student类创建出来的对象
# # name和age是对象属性，是每一个实例对象都会单独保存一份的属性
# # 每个实例对象之间的属性没有关联，互不影响
#
# x = s1
# print(x.name)  # 张三
# # print(Student.name)


# class Singleton:
#     __instance = None  # 私有的类属性
#     __is_first = True
#
#     @classmethod
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance == None:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#     def __init__(self, a, b):
#         if self.__is_first:
#             self.a = a
#             self.b = b
#             self.__is_first = False
#
# s1 = Singleton("heheh", "hahah")
# s2 = Singleton("哈哈哈", "嘿嘿嘿")
# print(s1 is s2)  # True
# print(s1.a)  # heheh
# print(s1.b)  # hahah
# print(s2.a)  # heheh
# print(s2.b)  # hahah

# class Tuple:
#     __count = 0
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         Tuple.__count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.__count
#
#
# print(Tuple.get_count())
# t1 = Tuple(1, 2);
# print(Tuple.get_count())
# t2 = Tuple(1, 2);
# print(Tuple.get_count())
# t3 = Tuple(1, 2);
# print(Tuple.get_count())
# t4 = Tuple(1, 2);
# print(Tuple.get_count())


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         print(f"{self.name}正在睡觉")
#
#
# class Dog(Animal):
#     def bark(self):
#         print(self.name + "正在狗叫")
#
#
# class Student(Animal):
#     def study(self):
#         print(self.name + "正在学习")
#
#
# d1 = Dog("大黄", 3)
# print(d1.name)

# class A:
#     pass
#
# class B:
#     def foo(self):
#         print("我是B类里的foo方法")
#
# class C(A):
#     def foo(self):
#         print("我是C类里的foo方法")
#
# class D(B):
#     pass
#
# class X(D,C):
#     pass
#
# x1 = X()
# x1.foo() #我是B类里的foo方法
# print(X.__mro__)
# #(<class '__main__.X'>, <class '__main__.D'>,
# # <class '__main__.B'>, <class '__main__.C'>,
# # <class '__main__.A'>, <class 'object'>)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class C:
#     pass
#
# class Student(Person):
#     pass
#
# p1 = Person("张三", 18)
# s1 = Student("李四", 30)
# print(isinstance(s1, Person))  # True
# print(isinstance(s1, Student))  # True
# print(isinstance(s1, (Person, Student, C)))  # True
# print(issubclass(Person, Student))  # False
# print(issubclass(Student, Person))  # True
# print(issubclass(Student, (Person, C)))  # True


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("我是Person类，我叫" + self.name + "我正在睡觉")


class Student(Person):
    def __init__(self, name, age, school):
        # 方法一
        # self.name = name
        # self.age = age

        # 方法二
        # Person.__init__(self,name,age) #手动调用父类的__init__方法

        # 方法三  使用super直接调用父类的方法
        super(Student, self).__init__(name, age)
        self.school = school

    def sleep(self):
        print("我是tudent类，我叫" + self.name + "我正在睡觉")

    def study(self):
        print(self.name + "正在学习")


p = Person("李四", 30)
s = Student("张三", 20, "清华大学")






# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         print("我是Person类，我叫" + self.name + "我正在睡觉")
#
#
# class Student(Person):
#     def sleep(self):
#         print("我是tudent类，我叫" + self.name + "我正在睡觉")
#
#     def study(self):
#         print(self.name + "正在学习")
#
#
# p = Person("张三", 20)
# s = Student("李四", 30)
# p.sleep()  # 我是Person类，我叫张三我正在睡觉
# s.sleep()  # 我是tudent类，我叫李四我正在睡觉
