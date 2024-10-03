'''
wrapping of variables methods in a single unit is called encapsulation.
public
private  __
protected _

'''

class vishnu():
    def __init__(self,a,b):
        self.__a=a   # private
        self._b=b    # protected
class vishnu1(vishnu):
    def output(self):
        print(self._b)
s=vishnu1(5,7)
s.output() 



def add(a,b):
    print(a+b)

add(3,8)
add('a','b')
add([45,67],[23,89])
add((45,65),(74,99))    