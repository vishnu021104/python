'''
blue print of a object

syntax:
class className
    #body


 object syntax:
   obj name=class name
   obj name.method name       

'''

# class python():
#     a=5
#     print(a)


class python():    #class name
    a=7
    def output(self):   #method name
        print(self.a)
b=python()
b.output() 


class vishnu():
    pass

###########################################
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person('gopal',26)

print(p1.name)
print(p1.age)


class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} ({self.age})"
        

p1=person('gopal',26)

print(p1)



##################################

class Item:
    def total_price(self,x,y):
        return x*y


item1=Item()
item1.name="phone"
item1.price=10000
item1.quantity=5
print(item1.total_price(item1.price,item1.quantity))


item2=Item()
item2.name="laptop"
item2.price=50000
item2.quantity=3
print(item2.total_price(item2.price,item2.quantity))