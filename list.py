'''
lists
'''

# a=[]
# print(type(a))


# b=[1,5,8,3,9,4,8,2,6,"vishnu"]
# print(b)
# print(b[5])
# print(b[-3])
# print(b[0:5])
# print(b[1:7:2])


'''
append
extend
count
insert
pop
remove
index
reverse
sort

'''


# a=[3,6,8,3,67,50,'vishnu']
# a.append('python')
# print(a)


# a=[3,6,8,3,67,50,'vishnu']
# a.extend([589,676,33,3,65])
# print(a)


# a=[3,6,8,3,67,50,'vishnu']
# print(a.count(3))


# a=[3,6,8,3,67,50,'vishnu']
# a.remove(50)
# print(a)


# a=[3,6,8,3,67,50,30,42,10,'vishnu']
# a.pop(7)
# print(a)


# a=[3,6,8,3,67,50,'vishnu']
# print(a.index(50))
# print(a.index("vishnu"))


# a=[3,6,8,3,67,50,'vishnu']
# a.insert(5,"python")
# print(a)


# a=[3,6,8,3,67,50,'vishnu']
# a.reverse()
# print("reverse list is :",a)


# a=['computer','mobile','tab','laptop']
# a.sort()
# print("sorted list is ",a)



# for i in [3,6,8,3,67,50,'vishnu']:
#    print(i)


# extend a list without append

l1=[20,40,60]
l2=[10,30,50]
l1[:0]=l2
print(l1)



# python program to access index of list using for loop

my_list=[42,55,74,94,24]
for index,val in enumerate(my_list,start=1):
    print(index,val)


'''
1 42
2 55
3 74
4 94
5 24 
 
'''

list1=['abc','tiger',205,505,'computer']
list2=[1,76,335,35,645,36,56,554]

print("list1= ",list1)
print("list2= ",list2)

print("list1[1:3]=",list1[1:3])
print("list2[2:5]=",list2[2:5])
print("list2[1:]=",list2[1:])

# update the list
print("available in list1 :",list1)
list1[3]="vishnu"
print("updating list is :",list1)


# deleting the list
print("available in list2 :",list2)
del list2[5]
print("after deleting index 5 in list2 :",list2)


# built in list functions
# len() function
list1=[1,5,8,3,9,4,8,2,6]
list2=["c","c++","java","html","python"]
print("length of list1 :",len(list1))
print("length of list2 :",len(list2))

# max() function
list1=[1,5,8,3,9,4,8,2,6]
list2=["c","c++","java","html","python"]
print("max element in list1 :",max(list1))
print("max element in list2 :",max(list2))


# min() function
list1=[1,5,8,3,9,4,8,2,6]
list2=["c","c++","java","html","python"]
print("min element in list1 :",min(list1))
print("min element in list2 :",min(list2))


# list() function
tuple=("c","c++","java","html","python")
list1=list(tuple)
print("changing tuple to list is :",list1)


str="vishnu"
list2=list(str)
print("changing string to list is :",list2)




list=["c","c++","java","html","python"]

m=[i for i in list]
print(m)


n=[i for i in range(10)]
print(n)


k=[1,2,3,4,5,6,7,8,9]

new_list=[]
for i in k:
    if i%2==0:
        new_list.append(i)
print(new_list)



m=[i for i in range(10) if i%2==0]
print(m)

nums=[0,0,0,1]
ans=all(x==0 for x in nums)
print(ans)



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


nums=[5,4,3,2,1]
for i in reversed(nums):
    print(nums)


a=[1,1,2,3]
b=[2,2,3,4]

ans=sorted(set(a+b))
print(ans)