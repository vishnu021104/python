from tkinter import *
from tkinter import simpledialog,messagebox

main=Tk()
main.withdraw()

questions=["what is the capital of india.?",
           "who is prime minister in india.?",
           "what is the capital of karnataka.?",
           "what is the chief minister of AP.?"  ]

answers=["delhi",
         "modi",
         "banglore",
         "cbn"]

score=0

for i in range(0,len(questions)):
    print(questions[i])
    user_answer=simpledialog.askstring(questions[i],"Answer: ")

    if user_answer==answers[i]:
        messagebox.showinfo("correct","coreect")
        score=score+1
    else:
        messagebox.showinfo("incorrect","incorrect")    
messagebox.showinfo("score",str(score))