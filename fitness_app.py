users={}
def create_account():
    username=input("enter the username : ")
    password=input("enter the password : ")
    height=float(input("enter the height : "))
    weight=float(input("enter the weight : "))

    users[username]={
        "password":password,
        "height":height,
        "weight":weight,
        "workouts":[]
    }

    print("account created successfully.")

def login():
    username=input("enter the username : ")
    password=input("enter the password : ")

    if username in users and users[username]["password"]==password:
        return username
    else:
        print("invalid username or password.")
        return None
    
def calculate_bmi(username):
    height=users[username]["height"] 
    weight=users[username]["weight"]
    bmi=weight/(height**2)
    print(f"your bmi is : {bmi:.2f}")

def log_workout(username):
    workout_name=input("enter the workout name : ")
    duration=float(input("enter the duration in minutes : "))

    users[username]["workouts"].append({
        "workout_name":workout_name,
        "duration":duration
    }) 

    print("workout logged successfully.")

def view_workouts(username):
    print("your workouts : ")

    for i,workout in enumerate(users[username]["workouts"]):
        print(f"{i+1}. {workout["workout_name"]} : {workout["duration"]} minutes.") 

def main():
    while True:
        print("***** fitnes app *****")
        print("1.create account")
        print("2.login account") 
        print("3.exit") 

        choice=int(input("enter the choices from 1 to 3 : "))

        if choice==1:
            create_account()

        elif choice==2:
            username=login() 
            if username:

                while True: 
                    print("======dashboard======")
                    print("1.calculate bmi")
                    print("2.log workout")
                    print("3.view workouts")
                    print("4.exit")

                    choice=int(input("enter the choices from 1 to 4 : "))

                    if choice==1:
                        calculate_bmi(username)

                    elif choice==2:
                        log_workout(username)

                    elif choice==3:
                        view_workouts(username) 

                    elif choice==4:
                        print("exiting the program")
                        break

                    else:
                        print("invalid choice.please try again")


        elif choice==3:
            print("exiting the program.")
            break

        else:
            print("invalid choice.please try again.")

if __name__=="__main__":
    main()
