# given number is even or odd
num= int(input("enter a number:"))
if num%2==0:
    print("It is even number")
else:
    print("It is odd number")    



# print even or odd letters in string

string="python"
data=[]
for i in range(len(string)):
    if i%2==0:
        data.append(string[i])
print(data)        
