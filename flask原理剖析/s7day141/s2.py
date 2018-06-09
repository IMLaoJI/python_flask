import functools

def func(a1):
    print(a1)


new_func = functools.partial(func,666)

new_func()

