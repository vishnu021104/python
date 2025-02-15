# python program to remove punctuation from a string
punctuations="'''''''!@#$%^&*()_-=+,."
mystr=input("enter the string:")

new_str=""
for i in mystr:
    if i not in punctuations:
        new_str=new_str+i
print(new_str)