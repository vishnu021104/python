# a={}
# print(type(a))

# s={5:"abc",70:"python","html":20}
# print(s["html"])


'''
get
update
key
values
items

'''
s={5:"abc",70:"python","html":20}
# print(s.get(70))
# print(s.keys())
# print(s.values())
# print(s.items())
# s.update({50434:9435})
# print(s)


# for i,j in {5:"abc",70:"python","html":20}.items():
#     print(i,j)


my_dict={1:'a',2:'b',3:'c'}
if 30 in my_dict:
    print("present")
else:
    print("not present")    

# create a list  of empty dictionaries
#[{},{},{},{},{}]

print([{} for _ in range(10)])