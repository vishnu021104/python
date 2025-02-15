# a=()
# print(type(a))

# b=(1,53,43,57,2,643,45)
# print(min(b))
# print(max(b))
# print(sum(b))
# print(len(b))

# t1=(54,66,95)
# t2=(12,75,46)
# print(t1+t2)

# c=(5,8,4,9,2,3,7,6)
# print(c*5)
# for i in c:
#     print(i)

# print(20 in c)    

# t1=(1,2,3)
# t2=(4,5,6)
# print(t1 is not t2)

# tuple is ordered,immmutable,unchanged.
# indexing, slicing
tuple1=('html','css','js','java','python')
tuple2=(24,64,75,87,12,66,95)
print("tuple1 :",tuple1)
print("tuple2 :",tuple2)
print("tuple1[3] :",tuple1[3])
print("tuple2[1:3] :",tuple2[1:3])
print("tuple1[3:] :",tuple1[3:])
print("tuple2[-1] :",tuple2[-1])

tuple3=tuple1+tuple2
print("new tuple :",tuple3)

# tuple basic operators 
tuple1=('html','css','js','java','python')
tuple2=(24,64,75,87,12,66,95)

# length function()
print("length of tuple1 :",len(tuple1))
print("length of tuple2 :",len(tuple2))

# concatenation function()
tuple3=tuple1+tuple2
print("new tuple :",tuple3)

# repetation function()
print("repetation function :",tuple2*3)

a="html" in tuple1
print("html in tuple1 :",a)

# iteration function
for x in (1,2,3):
    print(x)



# tuple built in function
tuple1=('html','css','js','java','python')
tuple2=(24,64,75,87,12,66,95)

# length function()
print("length of tuple1 :",len(tuple1))
print("length of tuple2 :",len(tuple2))

# maximum function()
print("maximum of tuple1 :",max(tuple1))
print("maximum of tuple2 :",max(tuple2))


# minimum function()
print("minimum of tuple1 :",min(tuple1))
print("minimum of tuple2 :",min(tuple2))


# tuple function()
list=[24,64,75,87,12,66,95]
str="vishnu"
print("tuple of list :",tuple(list))
print("tuple of string :",tuple(str))