money=int(input("enter the how much money : "))

thousands=money//1000

remaining=money%1000
hundreds=remaining//100

remaining=money%100
tens=remaining//10

ones=money%10

print("thousands : ",thousands)
print("hundreds : ",hundreds)
print("tens : ",tens)
print("ones : ",ones)