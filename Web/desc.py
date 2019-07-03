# 代码 1

class Desc(object):

    def __get__(self, instance, owner):
        print("__get__...")
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("owner : \t", owner)
        print('=' * 40, "\n")

    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('=' * 40, "\n")


class TestDesc(object):
    x = Desc()


# 以下为测试代码
t = TestDesc()
t.x
print(t)
t.x=3

# # 代码 3
#
# class Desc(object):
#     def __init__(self, name):
#         self.name = name
#         print("__init__(): name = ", self.name)
#
#     def __get__(self, instance, owner):
#         print("__get__() ...")
#         return self.name
#
#     def __set__(self, instance, value):
#         self.value = value
#
#
# class TestDesc(object):
#     _x = Desc('x')
#
#     def __init__(self, x):
#         self._x = x
#
#
# # 以下为测试代码
# t = TestDesc(10)
# t._x
#
# print(t.__dict__)
# print(TestDesc.__dict__)

