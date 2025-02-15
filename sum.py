# sum of numbers from user input

sum=0
ncount=0

while True:
    choice=input("enter the choice (y/n) : ").lower()

    if choice == 'n':
        break

    elif choice == 'y':
        number=int(input("enter a number : "))
        sum+=number
        ncount+=1
        
        average=sum/ncount

        print("sum is : ",sum)

        print("average is : ",average)


    else:
        print("it is invalid choice")    



# sum of numbers from 1 to n


num=int(input("emter the numbers : "))

sum=0

for i in range(1,num+1):
    sum=sum+i
print("sum of natural numbers : ",sum)