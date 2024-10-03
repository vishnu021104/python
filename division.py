# find all numbers which are divisible by7 but not a multipication of 5
l=[]
for i in range(0,1000):
    if i%7==0 and i%5!=0:
        l.append(str(i))
print(','.join(l))        
        