# import random
# result=random.randint(1,6)
# print("dice result : ",result)


import random

while True:
    print("1. roll dice \n 2.exit")
    choice=int(input("enter number 1 to 2: "))
    
    if choice==1:
        result=random.randint(1,6)
        print("The dice rolled to get the result: ",result)

    elif choice==2:
        print("the program has been ended")
        exit()   
    else:
        print(" you can choose invalid choice")    