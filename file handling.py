'''
open
read/write
close

'''

a=open('demo.txt',mode='r')
print(a.read())
a.close()


a=open('demo.txt',mode='w')
a.write("what is your name:")
a.close()

# a=open('demo.txt',mode='a')
# a.write("who are you?")
# a.close()

# a=open('demo.txt',mode='r+')
# print(a.read())
# a.write("what are you doing")
# a.close()

# a=open('demo.txt',mode='w+')
# a.write("what is your name:")
# a.seek(0)
# print(a.read())
# a.close()