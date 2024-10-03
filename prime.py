for num in range(2,101):
    for i in range(2,num):
        if num%i==0:
           break
    else:
        print(num)


n=int(input("enter a number: "))
for i in range(2,n):
    if n%i==0:
        print(n,"is not prime number")
        break
else:
    print(n,"is a prime number")


