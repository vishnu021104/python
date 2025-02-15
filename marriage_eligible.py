sex=input("enter the gender (male/female) : ")
sex.lower()

age=int(input("enter age of the gender : "))

if sex == 'male':

    if age >= 21:
        print("eligible for maariage")
    else:
        print("not eligible for marriage")


elif sex == 'female':

    if age >= 18:
        print("eligible for maariage")
    else:
        print("not eligible for maariage")    



