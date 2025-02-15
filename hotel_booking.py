rooms={
    '201':{'type':'single','price':200,'booked':False},
    '202':{'type':'double','price':350,'booked':False},
    '203':{'type':'suite','price':500,'booked':False}
}

def display_rooms(rooms):
    print("======== available rooms =======")
    for key,value in rooms.items():
        if not value["booked"]:
            print(f"{key}. {value["type"]} - {value["price"]} per night")


def book_room(rooms,room_number):
    if room_number in rooms:
        if not rooms[room_number]["booked"]:
            name=input("enter the customer name : ")
            night=int(input("enter the number of nights : "))
            rooms[room_number]["booked"]=True

            print(f"room {room_number} successfully booked for {name}")
        
        else:
            print(f"room {room_number} was already booked")

    else:
        print("Invlaid room number.Please try again.")      

def view_books(rooms):
    print("Booking rooms : ")
    for key,value in rooms.items():
        if value["booked"]:
            print(f"room {key} is booked")              


def cancel_books(rooms,room_number):
    if room_number in rooms:
        if rooms[room_number]["booked"]:
            rooms[room_number]["booked"]=False

            print(f"room {room_number} was cancelled successfully.")
        else:
            print(f"room {room_number} is not booked.") 

    else:
        print("Invalid room number.Please try again.")


def main():
    while True:
        print("********* HOTEL BOOKINGS **********")
        print("1.display rooms")
        print("2.room bookings") 
        print("3.view bookings")
        print("4.cancel bookings")
        print("5.exit")

        choice=int(input("enter the choice : "))

        if choice==1:
            display_rooms(rooms) 

        elif choice==2:
            room_number=input("enter the room number for booking : ")
            book_room(rooms,room_number)       

        elif choice==3:
            view_books(rooms)

        elif choice==4:
            room_number=input("enter the number for cancel booking : ")
            cancel_books(rooms,room_number)

        elif choice==5:
            print("existing the program")
            exit()

        else:
            print("Invalid choice.Please try again")            

if __name__=="__main__":
    main()

