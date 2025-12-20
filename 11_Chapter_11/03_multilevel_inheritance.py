# class employee:
#     a = 1
# class programmer:
#     b = 2
# class manager:
#     c = 3
# o = employee
# print(o.a)
# here if i enter o.b then there will be error because till now i haven't used the inheritance method so there is no object (b) but now that i will do so then there will be no problem...
class employee:
    a = 1
class programmer(employee):
    b = 2
class manager(programmer):
    c = 3
o = manager
print(o.a) #valid
print(o.b) #valid
print(o.c) #valid