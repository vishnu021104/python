# program to check if a string is palindrome or not
# input=madam,radar
# output=madam,radar


def ispalindrome(s):
    return s==s[::-1]
s="madam"
ans=ispalindrome(s)
if ans:
    print("this is palindrome")
else:
    print("this is not palindrome")  



# problem-2

forw=input("enter a word: ") 
rev=forw[::-1]

if forw==rev:
    print("It is the polindrome")
else:
    print("It is not polindrome")    