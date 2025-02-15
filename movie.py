print("*****BOOK MY SHOW*****")


while True:
    print("==" * 30)

    print("1.view available movies \n 2.book the movie ticket \n 3.view bookings \n 4.exit")

    print("==" * 30)
    choice=input("enter the choice 1 to 4 : ")

    if choice=='1':
        print("1.Pushpa2 \n 2.Amaran \n 3.Devara \n 4.Game Changer")

    elif choice=='2':
        print("1.Pushpa2 \n 2.Amaran \n 3.Devara \n 4.Game Changer")

        movie=input("enter movie name : ")
        persons=int(input("enter number of persons : "))
        seats=int(input("enter number of seats : "))
        price=150
        total_price=price*persons
        print("toal amount is : ",total_price)
        submit=input("enter submit  : ")
        print("successfully booked the movie tickets")

    elif choice=='3':
        print("booking tickets are : ",persons, " tickets are booked")

    elif choice=='4':
        exit()

    else:
        print("It is the invalid choice")  

    print("***THANK YOU! HAve a nice day***")




