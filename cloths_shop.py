print("***** fashion shopping cart *****")

products={
    "1":{"name":"T-Shirt","price":200},
    "2":{"name":"Shirt","price":500},
    "3":{"name":"jeans","price":1000},
    "4":{"name":"cotton pant","price":750}
}

carts={}

while True:
    print("===== products =====")
    for key,value in products.items():
        print(f"{key}.{value["name"]} - {value["price"]}")

    
    choice=input("enter the product number to add to cart (or 'v' to view cart ,'c' to checkout) : ")

    if choice in products:
        quantity=int(input("enter the quantity : "))

        if choice in carts:
            carts[choice]["quantity"]+=quantity
        else:
            carts[choice]={
                "name":products[choice]["name"],
                "price":products[choice]["price"],
                "quantity":quantity
            }   

        print(f"added {quantity} {products[choice]["name"]} s to cart.")


    elif choice.lower()=="v":
        print("cart : ") 

        for key,value in carts.items():
            print(f"{value["name"]} X {value["quantity"]} = {value["price"]*value["quantity"]}")

    elif choice.lower()=="c":
        total=sum(value["price"]*value["quantity"] for value in carts.values())

        print("total : ",total)
        print("Thank you for shopping.")
        break

    else:
        print("invalid choice.please try again.")               