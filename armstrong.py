# check if the number is armstrong or not
n=int(input("enter the number:"))
s=n
sum=0
while n>0:    # 153
    r=n%10    # 153%10=3  
    sum+=r**3 # 3**3=27  5**3=125  1**3=1   27+125+1=153
    n=n//10   

if s==sum:
    print("armstron number")
else:
    print("not a armstrong number")    