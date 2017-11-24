from functools import singledispatch
from collections import abc
import numbers

@singledispatch
def handle(obj):
    return repr(obj)

@handle.register(str)
def _(text):
    print(text)
    return "this is str"

@handle.register(numbers.Integral)
def _(num):
    print(num+100)
    return "this is number"

@handle.register(tuple)
@handle.register(abc.MutableSequence)
def _(seq):
    for item in seq:
        print(item)
    return 'this is seq'

def register(active=True):
    def decorate(func,*args):
        print(active)
        if active:
            print('active')
        else:
            print('noactive')
        return func
    return decorate

@register
def func(a):
    print('a is %s' %a)


if __name__ == '__main__':
    (5)
