'''
pass
continue
break

'''


# if True:
#    pass


# a=5
# b=3
# if a>b:
#    pass


# a="computer"
# for i in a:
#    if i=='t':
#        continue
#   print(i)


# a=[1,2,3,4,5,6,7]
# for i in a:
#    if i==6:
#        continue
#    print(i)


# a="python"
# for i in a:
#    if i=='h':
#        break
#    print(i)


# a=5,6,8,3,9,8,7,2,1,4,0,8,5,6
# for i in a:
#    if i==7:
#        break
#    print(i)

# break statement

for letter in "vishnu":
    if letter=="h":
        break
    print("current letter :",letter)


a=10
while a>0:
    a=a-1
    print("current value ",a)
    if a==5:
        break
    


# continue statements

for letter in "vishnu":
    if letter=="h":
        continue
    print("current letter :",letter)


a=10
while a>0:
    a=a-1
    if a==5:
        continue
    print("current value ",a)


pswd="123"
while True:
    x=input("enter a password :")
    if x!=pswd:
        print("enter again")
        continue
    print("password entered correctly")
    break

 

# pass tatement

a=10
b=20
if a<b:
    pass
