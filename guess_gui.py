from random import randint
from tkinter import *
from tkinter import simpledialog,messagebox

main=Tk()
main.withdraw()


random_number=randint(0,10)
# print(random_number)


random_number=7
x=-1

while x!=random_number:
    if x!=-1:
        messagebox.showinfo("wrong","wrong guess") 
    x=int(simpledialog.askstring("guess","enter a number: "))
    
    if x==random_number:
        messagebox.showinfo("right"," you guessed correctly")
        exit()

main.mainloop()        
        