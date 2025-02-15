# add two lists using map and lambda
#its have only one expression and it is anonymous function
l1=[10,20,30]
l2=[40,50,60]
print("original list")
print(l1)
print(l2)
result=map(lambda x,y:x+y,l1,l2)    # two paramters x,y and one expression x+y
print("result")
print(list(result))



sub=lambda a,b:a-b
print("value of subtraction :",sub(30,20))
print("value of subtraction :",sub(50,20))



num=int(input("enter a number: "))

result=list(map(lambda x:2**x, range(num+1)))

print(result)

for i in range(num+1):
    print("the value of 2 raised to power ",i ," is ",result[i])



a=lambda x:x+10
print(a(5))    


m=lambda x,y:x*y
print(m(5,6))

# map function

a=[1,2,3,4,5]
b=map(lambda x:x*2,a)
print(list(b))

c=[x*2 for x in a]
print(c)

# filter function

a=[1,2,3,4,5]
b=filter(lambda x:x%2==0,a)
print(list(b))

c=[x for x in a if x%2==0]
print(c)
