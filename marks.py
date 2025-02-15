print("***** STUDENT MARKS *****")

print("="*50)
name=input("Enter student name : ")
roll_no=int(input("enter roll number : "))

telugu=int(input("enter student telugu marks : "))
hindi=int(input("enter student hindi marks : "))
english=int(input("enter student english marks : "))
maths=int(input("enter student maths marks : "))
science=int(input("enter student science marks : "))
social=int(input("enter student social marks : "))
total_marks=(telugu+hindi+english+maths+science+social)
average_marks=total_marks/6
print("="*50)

print("*"*50)
print("student name : ",name)
print("roll number :",roll_no)
print("student total marks : ",total_marks)
print("student average marks : ",average_marks)
print("*"*50)

print("="*30)

if average_marks >= 90:
    print("Grade A")
    print("Excellent")

elif average_marks >= 80:
    print("Grade B")
    print("very very Good")

elif average_marks >= 70:
    print("Grade C") 
    print(" very Good")  

elif average_marks >= 60:
    print("Grade D")
    print("Good")

elif average_marks >=50:
    print("Grade E")
    print("Average")

else:
    print("Grade f")
    print("Fail")

print("="*30)    

print("*"*30)
print("Thank you!")
print("*"*30)


