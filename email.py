email=input("enter a email: ")
index=email.index("@")

username=email[:index]
domain=email[index+1:]

print("your username is ",username,"and domain is ",domain)