'''
for
while
nested loop

'''


# for i in range(0,20,2):
#    print(i)


# a=[1,5,8,6,9,3,5,2,7,4,6]
# for i in a:
#    print(i)


# a="vishnu"
# for i in a:
#    print(i)


# while True:
#    print("vishnu")


# a=10
# while a<20:
#    print("python",a)
#    a+=1



# for i in range(0,10):
#    for j in range(0,20):
#        print(i*j)



# while loop

# count=0
# while count<10:
#    count=count+1
#    print("count=",count)
# print("good bye") 


# infinite while loop
# a=1
# while a==1: # this consructs an infinite loop
#    num=int(input("enter a number : "))
#    print("you entered : ",num)
# print("thank you")


# while loop else statememt
# a=20
# while a<30:
#   a=a+1
#    print(a, "is less than 30")
# else:
#    print(a, "is not less than 30") 
# print("thank you!")  



# while loop single statement
# flag=1
# while (flag): print("given flag is really true") # infinite loop


# for loop 
for letter in "vishnu":
    print("current letter :",letter)

fruits=['apple','orange','banana']
for i in fruits:
    print("fruits :",i)     


# range function in for loop

for i in range(7):
    print(i)

print("range(start,stop)")  

for i in range(1,5):
    print(i)

print("range(start,stop,step)")

for i in range(1,7,2):
    print(i)


# for loop iterating by sequence index
# dict={key:value}

dict={'html':50,'css':70,'js':30,'python':60}
for i in dict:
    print(dict[i])                      # print i only o/p comes keys otherwise print(dict[i]) then o/p comes values only

for key,value in dict.items():
    print(key,value)    

for key in dict.keys():
    print(key)    

for val in dict.values():
    print(val)  



# nested for loop

for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print(k,end="  ")
    print()    




# using else with for loop

for i in range(10):
    print("hello", i)

else:
    print("end of the for loop")