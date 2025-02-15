students={}

def display_menu():
    print("====== Attendence management system ======")
    print("1.add student")
    print("2.mark attendence")
    print("3.view attendence")
    print("4.exit")

def add_student(students):
    name=input("enter the student name : ")
    students[name]={"attendence":[],"total_classes":0}
    print(f"student {name} added successfully")


def mark_attendence(students):
    name=input("enter the student name : ")
    if name in students:
        attendence=input("enter attendence (P/A) : ")
        students[name]["attendence"].append(attendence)
        students[name]["total_classes"]+=1

        print(f"attendence marked for {name}")
    else:
        print(f"student {name} is not found.")


def view_attendence(students):
    name=input("enter the student name : ")
    if name in students:
        attendence=students[name]["attendence"]
        total_classes=students[name]["total_classes"]

        present=attendence.count("P")   
        absent=attendence.count("A")
        percentage=(present/total_classes)*100

        print("***** attendence report *****")
        print("total_classes : ",total_classes)
        print("present : ",present)
        print("absent : ",absent)
        print("percentage : ",percentage, "%")

    else:
        print(f"student {name} not found.")


def main():
    while True:
        display_menu()
        choice=int(input("enter the choice (1-4) : "))

        if choice==1:
            add_student(students)

        elif choice==2:
            mark_attendence(students)

        elif choice==3:
            view_attendence(students)

        elif choice==4:
            print("exiting the program")
            break
        else:
            print("invalid choice.please try again.")

if __name__=="__main__":
    main()


    


    


