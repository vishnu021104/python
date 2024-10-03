# largest in given three numbers
a= int(input("enter a number:"))
b= int(input("enter a number:"))
c= int(input("enter a number:"))
 
if a>b and b>c:
    print("a is largest")
elif b>c and b>a:
    print("b is largest")
else:
    print("c is largest")    


