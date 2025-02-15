# python compound intrest calculator

principle=0
rate=0
time=0

while True:
    principle=float(input("enter the principle amount: "))
    if principle < 0:
        print("principle less than to zero")
    else:
        break

while True:
    rate=float(input("enter the rate amount: "))
    if rate < 0:
        print("rate less than to zero")
    else:
        break


while True:
    time=float(input("enter the time amount: "))
    if time < 0:
        print("time less than to zero")
    else:
        break        


total=principle*((1+rate/100)**time)    
print("balance after",time,"year/s is",total)