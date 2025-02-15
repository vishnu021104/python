# shopping cart

foods=[]
prices=[]
total=0

while True:
    food=input("enter the item or (q to quit) : ")
    food.lower()

    if food=='q':
        exit()

    else:
        price=float(input(f"enter price of {food}: $"))
        foods.append(food)
        prices.append(price)



    print("===== YOUR CART =====")

    for food in foods:
        print(food)

    for price in prices:
       total+=price    

    print("your total is ",total) 
