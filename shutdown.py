import os

choice=input("enter the choice shutdown your computer (y/n) : ")
choice.lower()

# /s = shutdown , /r = restart,  /l = logoff

if choice == 'y':
    os.system("shutdown /r")

else:
    print("exitin the program")    
