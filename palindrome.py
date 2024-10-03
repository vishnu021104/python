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