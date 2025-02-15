restaurants={
    "adiratha":{
        "menu":{
            "chicken biryani":200,
            "spl biryani":220,
            "dhum biryani":250 
        },
        "rating":4.6    
    },

    "king's restuarant":{
        "menu":{
            "veg biryani":180,
            "panner biryani":200,
            "mogalai biryani":230
        },
        "rating":4.3
    }
}

users={}

def create_account():
    username=input("enter the name of the custmor : ")
    password=(input("enter the password : "))

    users[username]={
        "password":password,
        "orders":[]
    }
    print("account create successfully.")

def login():
    username=input("enter the custmor name : ")
    password=input("enter the password : ")

    if username in users and users[username]["password"]==password:
        return username
    else:
        print("invalid username or password")
        return None

def view_restaurants():
    print("===== restaurants =====")

    for i,restaurant in enumerate (restaurants):

        print(f"{i+1}. {restaurant} - rating : {restaurants[restaurant]["rating"]}")


def view_menu(restaurant):
    print(f"===== {restaurant} menu =====")

    for i,item in enumerate (restaurants[restaurant]["menu"]):
        print(f"{i+1}. {item} - {restaurants[restaurant]["menu"][item]:.2f}")


def place_order(username, restaurant, item):
    users[username]["orders"].append({
        "restaurant":restaurant,
        "item":item
    })

    print(f"order place succesfully. - {restaurant} - {item}")

def view_order(username):
    print("===== orders =====")

    for i,order in enumerate (users[username]["orders"]):
        print(f"{i+1}. {order["restaurant"]} - {order["item"]}")


def main():
    while True:
        print("******** food delivery app ********")        
        print("1. create account")
        print("2.login")
        print("3.exit")

        choice=int(input("enter the choice : "))

        if choice==1:
            create_account()

        elif choice==2:
            username=login()
            if username:

                while True:
                    print("***** dashboard *****")
                    print("1.view restaurants")
                    print("2.view menu")
                    print("3.place order")
                    print("4.view orders")
                    print("5.exit") 

                    choice=int(input("enter the choices (1-5) : "))

                    if choice==1:
                        view_restaurants()

                    elif choice==2:
                        view_restaurants()

                        restaurant_choice=int(input("enter the restaurant choice : "))
                        restaurant=list(restaurants.keys())[restaurant_choice-1] 
                        view_menu(restaurant)     

                    elif choice==3:
                        view_restaurants()

                        restaurant_choice=int(input("enter the restaurant choice : "))
                        restaurant=list(restaurants.keys())[restaurant_choice-1] 
                        view_menu(restaurant)

                        item_choice=int(input("enter the item : "))
                        item=list(restaurants[restaurant]["menu"].keys())[item_choice-1]
                        place_order(username, restaurant,item)


                    elif choice==4:
                        view_order(username)

                    elif choice==5:
                        print("logged out sucessfully.")
                        break

                    else:
                        print("invalid choice.please try again")


        elif choice==3:
            print("exiting the app")
            break


        else:
            print("invalid choice. please try again")


if __name__=="__main__":
    main()




