print("********** welcome to APSRTC ticket bookings ***********")

total=0

print("="*50)

while True:
    print("*"*50)
    choice=int(input(" 1.exit \n 2.book tickets \n 3.view tickets \n enter the choices (1 to 3) : "))
    print("*"*50)

    if choice == 1:
        print("exiting the program")
        break

    elif choice == 2:
        name=input("enter the person name : ")
        bus=input("enter the bus number : ")
        seat=input("enter seat number : ")
        persons=int(input("enter no.of persons : "))
        price=800

        total_price=price * persons
        
        print("|"*50)
        print("person name : ",name)
        print("bus number is : ",bus)
        print("seat number is : ",seat)
        print("enter number of persons : ",persons)
        print("the total price is : ",total_price)
        print("|"*50)

        submit=input("enter the submit : ")
        
        print("-"*50)
        print("The bus tickets are successfully booked")
        print("-"*50)

        total+=1

        

    elif choice == 3:
        print("total booked tickets : ",total)

    else:
        print("It is the invalid choice")

    print("THANK YOU!")    

print("="*50)

