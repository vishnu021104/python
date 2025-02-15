# s={1,2,44,856,5}
# print(type(s))

'''
add
update
pop
remove

'''

s={1,4,55,78,5,66,5,78,42,5}
# print(s)
#s.add(555)
# s.update({1,2,3,4,5})
# s.pop()
# s.remove(55)
# print(s)


'''
union
intersection
difference
issubset
issuperset

'''

# a={1,2,3,4,5}
# b={3,5,7,8,2}
# print(a.union(b))

# a={1,2,3,4,5}
# b={3,5,7,8,2}
# print(a.intersection(b))


# a={1,2,3,4,5}
# b={3,5,7,8,2}
# print(a.difference(b))


# a={1,2,3,4,5}
# b={3,4,5}
# print(a.issuperset(b))

# a={1,2,3,4,5}
# b={3,5,7,8,2}
# print(a.issubset(b))


s1={0,1,2,3,4}
s2={5,6,7,8,9}

zipped=zip(s1,s2)
# print(list(zipped))

for a,b in zip(s1,s2):
    print(a,b)