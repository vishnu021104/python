'''
collection of charchter
'''

# a='vishnu'
# b="vishnu"
# c='''vishnu'''
# print(type(a),type(b),type(c))


'''
lower
upper
endswith
replace
find
index
count
remove prefix
remove suffix
split
strip
rstrip
lstrip
'''


# a="python language"
# print(a.upper())

# a="PYTHON LANGUAGE"
# print(a.lower())

# vishnu="python language"
# print(vishnu.startswith("p"))


# vishnu="python language"
# print(vishnu.endswith("language"))


# vishnu="python programming"
# print(vishnu.replace("programming","language"))


# a="python programming"
# print(a.index("g"))

# a="python programming"
# print(a.find("programming"))

# a="python language"
# print(a.count("g"))

# a="python language"
# print(a.removeprefix("p"))

# a="python language"
# print(a.removesuffix("language"))


# a="      python programming     "
# print(a)
# print(len(a))
# print(a.strip())
# v=a.strip()
# print(len(v))
# p=a.rstrip()
# print(len(p))
# r=a.lstrip()
# print(len(r))




s='vishnu'
print(s)

s="vishnu"
print(s)

s='''vishnu'''
print(s)

# accessing characters in a string
mystr="country"

print("mystr=",mystr)
print("mystr[0]=",mystr[0])
print("mystr[1:5]=",mystr[1:5])
print("mystr[-1]=",mystr[-1])
print("mystr[3:-1]=",mystr[3:-1])

#strings are immutable
# but different Isstrings can be assigned
mystr="python"
print(mystr)

mystr="programming"
print(mystr)

#concatenation of string

mystr1="python"
mystr2="programming"
# using +
print("mystr1+mystr2=",mystr1+mystr2)

print("mystr1*5=",mystr1*5)

# iterating through a string
letter_count=0
for letter in "hello world":
    if(letter=="o"):
        letter_count=letter_count+1
print(letter_count,"times o letter repeated")        



# string membership
print('l' in 'hello')
print('l' not in 'hello')
print('a' in 'hello')
print('a' not in 'hello')


# built in function
mystr="vishnu"

#using enumerate()
my_list_enumerate=list(enumerate(mystr))
print("list(enumerate(mystr)=",my_list_enumerate)

print("len(mystr)=",len(mystr))


# escape triple quotes
print('''tell me "what's your name?"''')

# escape double quotes
print("tell me 'what\'s your name?'")

# escape single quotes
print('tell me "what\'s your name?"')

# escape double quotes
print("tell me \"what's your name?\"")


print("this is a private \n school")

print("this is a private \t school")


# format method
# default (implict) order

default_order="{} {} and {}".format('I','have','choclate')
print(default_order)

#order using positional argument
optional_order="{2} {0} and {1}".format('have','choclate','I')
print(optional_order)

# order using keyword argument
keyword_order="{i} {h} and {c}".format(i='I',h='have',c='choclate')
print(keyword_order)

# formatting numbers

print("required binary reprentation of {0} is {0:b}".format(30))

print("required exponent reprentation of {0} is {0:e}".format(18))

print("required float reprentation of {0} is {0:f}".format(1/7))



# string formatting operator

name="ABC"
print("hello %s" %name)

age=30
print("age=%d" %age)
print("age is %s" %age)

marks=60
print("marks=%f" %marks)
print("marks in octal %o" %marks)
print("marks in hexadecimal %x" %marks)
print("age with exp %e" %age)