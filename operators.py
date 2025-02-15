# arithimetic operator
a=20
b=15
print("a=",a,"b=",b)
c=a+b
print("addition of two numbers are :",c)

c=a-b
print("substraction of two numbers are :",c)

c=a*b
print("multipication of two numbers are :",c)

c=a/b
print("divisioon of two numbers are :",c)

c=a%b
print("modules of two numbers are :",c)

c=a**b
print("exponent of two numbers are :",c)

c=a//b
print("floor division of two numbers are :",c)


# logical operator
# AND,OR,NOT

a=True
b=False
# AND operator
print("a and b is:",a and b)    # false
# OR operator
print("a and b is:",a or b)      # true
# NOT operator
print("a and b is:",not a)       # false



# bitwise operator
# &,|,^,~,>>,<<
a=10  # binary:1010
b=5    # binary:0011

# Bitwise AND
print("a & b=",a & b)
# Bitwise OR
print("a | b=",a | b)
# Bitwise XOR
print("a ^ b=",a ^ b)
# Bitwise AND
print(" ~ b=",~ b)
# left shift
print("a << b=",a << b)
# right shift
print("a >> b=",a >> b)


# membership operator
# in,not in 
a=10
b=5
c=15
list=[1,3,34,75,10,64,50]
print("a=",a,"b=",b,"c",c)
if a in list:
    print("a is available in list")
else:
      print("a is not available in list")


if b in list:
    print("b is available in list")
else:
      print("b is not available in list")  


if c not in list:
    print("c is not available in list")
else:
      print("c is available in list")   


# identity operator
# is,is not

a=10
b=5
c=a

print("a=",a,":",id(a),"b=",b,":",id(b),"c=",c,":",id(c))

if a is not b:
    print("a and b have not same identity")
else:
    print("a and b have same identity")           


if a is c:
    print("a and c have same identity")
else:
    print("a and c have not same identity")    


if id(a) is id(b):
    print("a and b have not same identity")
else:
    print("a and b have same identity")    



# assignment operator
# += , -= , *= , /= , %= , **= , //==

a=5
b=a

print("value of a :",a)
print("value of b :",b)
a+=10
print("value of a+=10 :",a)

a-=10
print("value of a-=10 :",a)

a*=10
print("value of a*=10 :",a)

a/=10
print("value of a/=10 :",a)

a%=10
print("value of a%=10 :",a)

a**=10
print("value of a**=10 :",a)

a//=10
print("value of a//=10 :",a)


# relational operator
# == , != , > , < , <= , >=

a=30
b=50

a==b
print("a==b is : ",a==b)

a!=b
print("a!=b is : ",a!=b)

a>b
print("a>b is : ",a>b)

a>=b
print("a>=b is : ",a>=b)

a<b
print("a<b is : ",a<b)

a<=b
print("a<=b is : ",a<=b)

