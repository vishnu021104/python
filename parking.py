vehicle1=None
vehicle2=None
vehicle3=None

while True:
    print("***** online parking sysytem *****")
    print("1.vehicle1 parking")
    print("2.vehicle2 parking")
    print("3.vehicle3 parking")
    print("4.remove vehicle1")
    print("5.remove vehicle2")
    print("6.remove vehicle3")
    print("7.exit")

    choice=int(input("enter the choices from 1 to7 : "))

    if choice==1 and vehicle1 is None:
        vehicle1=input("enter the vehicle1 number : ")
        print(f"vehicle {vehicle1} is parked successfully.")
    elif choice==1 and vehicle1 is not None:
        print("slot 1 is already occupied") 


    if choice==2 and vehicle2 is None:
        vehicle2=input("enter the vehicle2 number : ")
        print(f"vehicle {vehicle2} is parked successfully.")
    elif choice==2 and vehicle2 is not None:
        print("slot 2 is already occupied")  

    if choice==3 and vehicle3 is None:
        vehicle3=input("enter the vehicle3 number : ")
        print(f"vehicle {vehicle3} is parked successfully.")
    elif choice==3 and vehicle3 is not None:
        print("slot 3 is already occupied") 

    if choice==4 and vehicle1 is not None:
        vehicle1=None
        print(f"vehicle1 removed successfully")  
    elif choice==4 and vehicle1 is None:
        print("slot 1 is empty")   

    if choice==5 and vehicle2 is not None:
        vehicle2=None
        print(f"vehicle2 removed successfully")  
    elif choice==5 and vehicle2 is None:
        print("slot 2 is empty") 

    if choice==6 and vehicle3 is not None:
        vehicle3=None
        print(f"vehicle1 removed successfully")  
    elif choice==3 and vehicle3 is None:
        print("slot 3 is empty")  

    if choice==7:
        print("exiting the program") 
        break

    if vehicle1 is not None or vehicle2 is not None or vehicle3 is not None:

        print("="*50)
        print("parking status : ")

        if vehicle1 is not None:
            print("slot 1 : ",vehicle1)   
        else:
            print("slot 1 : Empty")        

        if vehicle2 is not None:
            print("slot 2 : ",vehicle2)   
        else:
            print("slot 2 : Empty")     

        if vehicle3 is not None:
            print("slot 3 : ",vehicle3)   
        else:
            print("slot 3 : Empty")   

        print("="*50)                   



           
