# write a python  function to sum all the numbers in the list.
numbers=[30,63,35,86,95]
total_sum=sum(numbers)
print("sum of all numbers in the list is:",total_sum)

# using function

def sum(numbers):         # function definition
    total=0               # local variable
    for i in numbers:
        total+=i          # total=total+i
    return total
print(sum([10,54,6,33,264,43,35])) # function call  


s=[1,2,3,4,5]
print(sum(s))