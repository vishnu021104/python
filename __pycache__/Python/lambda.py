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