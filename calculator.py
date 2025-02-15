print("****** SIMPLE CALCULATOR ******")

num1=int(input("enter a first number: "))
num2=int(input("enter a second number: "))

print("press 1 for addition \n press 2 for substraction \n press 3 for multiplication \n press 4 for division")

choice=int(input("enter a choice 1-4: "))

if choice==1:
    print("addition of two numbers ",num1+num2)

elif choice==2:
    print("substraction of two numbers ",num1-num2)

elif choice==3:
    print("multiplication of two numbers ",num1*num2)  

elif choice==4:
    print("division of two numbers ",num1/num2)          