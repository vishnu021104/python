n=int(input("enter a number :"))
for i in range(n):                 # n=0,1,2,3,4,5
    for j in range(i+1):           # n=1,2,3,4,5,6
        print("*",end=" ")
    print()     
   

n=int(input("enter a number :"))
for i in range(n,0,-1):                # n=5,4,3,2,1
    for j in range(i,0,-1):            # n=5,4,3,2,1
        print("*",end=" ")
    print()    



for i in range(1,6):                 # 1,2,3,4,5
    for j in range(i):               # 1,2,3,4,5
        print(i,end=" ")
    print()    



for i in range(5,0,-1):                 # 5,4,3,2,1
    for j in range(i):                  # 5,4,3,2,1
        print(i,end=" ")
    print()    




for i in range(1,6):                  # 1,2,3,4,5
    for j in range(1,i+1):            # 1,2,3,4,5
        print(j,end=" ")
    print() 
   


for i in range(5,0,-1):                     # 5,4,3,2,1
    for j in range(1,i+1):                  # 5,4,3,2,1
       print(j,end=" ")
    print()   


for i in range(1,6):               # 1,2,3,4,5
    for j in range(5,i,-1):        # 5,4,3,2
       print(" ",end=" ")
    for k in range(1,i+1):         # i=1,2,3,4,5
        print("*",end=" ")
    print()    




for i in range(5,0,-1):               # 5,4,3,2,1
    for j in range(5,i,-1):           # 5,4,3,2,1
       print(" ",end=" ")
    for k in range(1,i+1):         # i=5,4,3,2,1
        print("*",end=" ")
    print() 



for i in range(1,6):               # 1,2,3,4,5
    for j in range(5,i,-1):        # 5,4,3,2
        print(" ",end=" ")
    for k in range(i):         # i=1,2,3,4,5
        print(i,end=" ")
    print() 




for i in range(5,0,-1):               
    for j in range(5,i,-1):        
        print(" ",end=" ")
    for k in range(i):         
        print(i,end=" ")
    print() 



for i in range(5,0,-1):               
    for j in range(5,i,-1):        
        print(" ",end=" ")
    for k in range(1,i+1):         
        print(k,end=" ")
    print() 



for i in range(1,6):               
    for j in range(5,i,-1):        
        print(" ",end=" ")
    for k in range(1,i+1):         
        print(k,end=" ")
    print()   