print("*********** CAFE MANAGEMENT ************")

menu={
    'tea':15,
    'coffee':25,
    'egg puff':20,
    'samosa':10,
    'biscuits':5,
}

print("welcome to chai cafe")
print(" tea: Rs 15 \n coffee:25 \n egg puff:20 \n samosa:10 \n biscuits:5")

order_total=0

item_1=input("enter the name of item you want to order : ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} has been added to your successfully")

else:
    print(f"ordered item {item_1} is not available yet")    


another_order=input("do you want another item (yes/no) : ")


if another_order=='yes':

    item_2=input("enter the name of item you want to order : ")
    if item_2 in menu:
        order_total+=menu[item_2]
    print(f"your item {item_2} has been added to your successfully")

elif another_order == 'no':
    exit()


else:
    print("invalid condition")    

print("your total bill is ",order_total)    



    

    
       

