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
    user_answer=input("enter a answer: ")

    if user_answer==answers[i]:
        print("correct")
        score=score+1
    else:
        print("incorrect")    
print(f"score {score}")



