def findHCF(x,y):
    if x > y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if ((x%i==0)and(y%i==0)):
            hcf=i
    return hcf
print("the hcf of given number is ",findHCF(12,30))                