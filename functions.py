'''
block of code

'''


# def add(a,b):
#     return a+b
# print(add(5,7))


# def func(name):
#     print(f"i am{name}")
# func(" vishnu")   

# def func(name,age,dish):
#     print(f"my name is {name} ")
#     print(f"i am years old {age}")
#     print(f"my favourite food is {dish}")     
    
# func("raj",30,"egg rice")
# func("ram",25,"gobi rice")
# func("gopi",27,"curd rice")


# def func(a,b,c):
#     print("this is function",a,b,c)
# func(1,2,3)  
  

# def func(*a):
#    print("this is function",a)
# func(1,2,3)     

# def func(**a):
#    print("this is function",a)
# func(a=1,b=2)   

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)
def divide(a,b):
    print(a/b)

add(1,2)    
sub(5,3)
multiply(3,2)
divide(5,2)    


# calling function

def my_functon():
    print("vishnu")
my_functon()    



# passing arguments in function

def my_function(name):
    print("my name is ",name)
my_function("vishnu")    
my_function("raju")    
my_function("rani")    


# arbitary arguments, *args

def my_function(*kids):
    print("the youngest kid is ",kids[2])
my_function("chinna","ammu","sweety")   


# arbitary keyword arguments,**kwargs

def my_function(**kids):
    print("the youngest kid is "+kids["child1"])
my_function(child1="chinna",child2="ammu",child3="sweety")   


# keyword arguments
def my_function(name,age):
    print("name :",name)
    print("age :",age)
my_function("rohit",27)    
my_function("niraj",32)



# default parameter arguments

def my_function(name,age=45):
    print("name :",name)
    print("age :",age)
my_function("rohit")    
my_function("niraj",32)


def my_function(country="india"):
    print("i am from :",country)
my_function("england")    
my_function("america")
my_function()    
my_function("austrelia")



# return values

def my_function(x):
    return 3 * x
print(my_function(3))
print(my_function(7))
print(my_function(5))
print(my_function(2))
print(my_function(8))


# passing a list as an argument

def my_function(food):
    for x in food:
        print(x)

fruits=["apple","banana","orange"]
my_function(fruits)


# pass statement

def my_function():
    pass



def display_student(name,age):
    print(name,age)

# call using original name
display_student('suraj',30)

# assign new name
new_student=display_student

# call using new name
new_student('kumar',27)


