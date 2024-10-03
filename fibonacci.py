# n=int(input("enter a number:"))
# a=0
# b=1
# if n==1:
#    print(a)
# else: 
#     print(a)
#     print(b)
# for i in range(2,n):
#     c=a+b
#     a=b
#     b=c
#     print(c)



# fibonacci sequence

n=int(input("enter a number:"))
a=0
b=1
c=0
for i in range(n):
    print(c,end=" ")
    a=b
    b=c
    c=a+b
    