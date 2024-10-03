from random import randint
random_number=randint(0,10)
# print(random_number)


random_number=7
x=-1

while x!=random_number:
    if x!=-1:
        print("wrong guess") 
    x=int(input("enter a number: "))

print("yes! you guessed correctly")