from itertools import chain

# def f1(x):
#     return x + 1
#
# func1_list = [f1,lambda x:x-1]
#
# def f2(x):
#     return x + 10
#
#
# new_fun_list = chain([f2],func1_list)
# for func in new_fun_list:
#     print(func)


v1 = [11,22,33]
v2 = [44,55,66]

new = chain(v1,v2)
for item in new:
    print(item)