
def display_student(students):
    print("====== students =======")
    for key, value in students.items():
        print(f"{key}. {value['name']} - {value['branch']}")


def add_student(students):
    roll_number=int(input("enter the roll number : "))
    name=input("enter the student name : ")
    branch=input("enter the name of the branch : ")
    students[roll_number]={
        'name':name,
        'branch':branch
        }
    print(f"student {name} was added successfully.")


def delete_students(students,roll_number):
    if roll_number in students:
        del students[roll_number]
        print(f"roll number {roll_number} was deleted successfully.")
    else:
        print(f"roll number {roll_number} was not found.") 


def display_faculty(faculty):
    print("====== faculty =======")
    for key, value in faculty.items():
        print(f"{key}. {value['name']} - {value['department']}")           

def add_faculty(faculty):
    faculty_id=int(input("enter the faculty id : "))
    name=input("enter the faculty name : ")
    department=input("enter the name of the department : ")
    faculty[faculty_id]={
        'name':name,
        'department':department
        }
    print(f"faculty {name} was added successfully.")        


def delete_faculty(faculty,faculty_id):
    if faculty_id in faculty:
        del faculty[faculty_id]
        print(f"faculty id {faculty_id} was deleted successfully.")
    else:
        print(f"faculty id {faculty_id} was not found.")     

def main():
    students={}
    faculty={}
    while True:
        print("****** college management *******")
        print("1.student management")
        print("2.faculty management")
        print("3.exit")

        choice=int(input("enter the choice from 1/2/3 : "))
        
        if choice==1:
            print("===== student management =====")
            print("1.display student")
            print("2.add student")
            print("3.delete student")
            print("4.back")

            student_choice=int(input("enter the student choice : "))

            if student_choice==1:
                display_student(students) 
            elif student_choice==2:
                add_student(students)
            elif student_choice==3:
                roll_number=int(input("enter the roll number for deleting : "))
                delete_students(students,roll_number)   
            elif student_choice==4:
                continue
            else:
                print("Invalid choice.Please try again.")

        elif choice==2:
            print("===== faculty management =====")
            print("1.display faculty")
            print("2.add faculty")
            print("3.delete faculty")
            print("4.back")

            faculty_choice=int(input("enter the faculty choice : "))

            if faculty_choice==1:
                display_faculty(faculty) 
            elif faculty_choice==2:
                add_faculty(faculty)
            elif faculty_choice==3:
                faculty_id=int(input("enter the faculty id for deleting : "))
                delete_faculty(faculty,faculty_id)   
            elif student_choice==4:
                continue
            else:
                print("Invalid choice.Please try again.")  

        elif choice==3:
            print("exiting the program.")
            break

        else:
            print("Invalid choice.Please try again.")  


if __name__=="__main__":
    main()



