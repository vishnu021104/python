# variable=value
# a=5
# print(a)

# a=1,2,3
# print(a)

# a,b,c=1,2,3
# print(a,b,c)

'''
1.start with alphabets.
2.start with _underscore.
3.cannot start with numbers.
4.case sensitive.
5.cannot start with symbols.


'''

# abc5958=10
# print(id(abc5958))

# python=50
# PYTHON=30
# print(python)   #case sensitive

# local variable inside func
# global variable outside func

a=57  # global
def func():
    x=20  #local
    y=10
    s="vishnu"
print(func.__code__.co_nlocals)


