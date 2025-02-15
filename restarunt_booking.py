bookings={}

while True:
    print("********Resturant booking system*********")
    print("1.Book table")
    print("2.cancel booking")
    print("3.view bookings")
    print("4.exit")
    
    print("="*50)
    choice=int(input("enter the choice (1-4) : "))
    print("="*50)

    if choice==1:
        table_number=int(input("enter table number : "))

        if table_number not in bookings:
            name=input("enter your name : ")
            phone=input("enter your phone number : ")
            time=input("enter booking time : ")

            bookings[table_number]={
                'name':name,
                'phone':phone,
                'time':time
            }
            
            print("*"*50)
            print(f"table {table_number} booked successfully")
            print("*"*50)

        else:
            print("="*50)
            print(f"table {table_number} is already booked")
            print("="*50)
                    
    elif choice==2:

        table_number=int(input("enter a table number : "))

        if table_number in bookings:
            del bookings[table_number]

            print("*"*50)
            print(f"table {table_number} cancelled successfully") 
            print("*"*50)

        else:
            print("*"*50)
            print(f"table {table_number} not found in bookings")
            print("*"*50)

    elif choice==3:
        print("bookings:")

        for table, booking in bookings.items():
            print("*"*50)
            print(f"table {table} : {booking['name']} - {booking['phone']} - {booking['time']}")
            print("*"*50)

    elif choice==4:
        print("the program is exiting")
        break

    else:
        print("invalid choice. please try again")        