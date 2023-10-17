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

import time


class Student(object):
    def __init__(self, x, y):
        # 对象创建的时候会自动调用
        # print("__init__方法被调用了")
        self.name = x
        self.age = y

    # def __del__(self):
    # 对象销毁的时候会自动调用
    # print("__del__方法调用了")

    def __repr__(self):
        return "__repr__"

    def __str__(self):
        return "__str__"

    def __call__(self, *args, **kwargs):
        print("__call__")

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        return False

s1 = Student("张三", 18)
s2 = Student("张三", 18)
print(s1 == s2)  # True
print(s1 is s2)  # False
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)  # False

print(l1 == l2)  # True
# s1()
# print(s1)
# print(repr(s1))
# print(s1.__repr__())
