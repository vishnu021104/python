print("***** PIZZA ORDERED *****")

print("="*50)

size=input("enter size of the pizza S,M,L or (q to quit) : ")

number=int(input("enter number of pizzas : "))

print('='*50)

if size=='S':
    price=120
           

elif size=='M':
    price=150
            

elif size=='L':
    price=200
           

else:

    print("It is invalid choice")
         

total=price*number

print("the total bill is : ",total,'/-')

submit=input("enter the submit : ")

print("*"*30)
print("you are ordered pizzas successfully ")
print("*"*30)
   


     
   
 


