str=input("enter a string: ")
str=str.lower()

vowel=['a','e','i','o','u']
vcount=0
ccount=0

for i in str:
    if i in vowel:
        vcount=vcount+1
    else:
        ccount=ccount+1

print("number of vowels in {} is {}".format(str,vcount))
print("number of consonants in {} is {}".format(str,ccount))



# find the letter vowel or consonant

chr="v"
vowels=['a','e','i','o','u']
if chr in vowels:
    print("vowel")
else:
    print("consonant")    