# find all numbers which are divisible by7 but not a multipication of 5
l=[]
for i in range(0,1000):
    if i%7==0 and i%5!=0:
        l.append(str(i))
print(','.join(l))        
        


# another division 
print("The numbers are divisible by 16 are: ")
for i in range(1,100) :
    if i % 16 == 0:
        print(i)   


# using lambda function
l=[10,13,49,53,50,64] 

result=list(filter(lambda x:x%5==0,l))

print("the 5 divisible numbers are: ",result)