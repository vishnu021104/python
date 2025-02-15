from collections import Counter
s="technologies"
my_counter=Counter(s)
# print(my_counter)


from collections import OrderedDict
ordered_dict=OrderedDict()
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=4
ordered_dict['d']=5
ordered_dict['e']=6
ordered_dict['e']=3
# print(ordered_dict)


from collections import defaultdict
default_dict=defaultdict(int)
default_dict['a']=1
default_dict['b']=2
# print(default_dict['c'])


from collections import deque
d=deque()

d.append(1)
d.append(2)
d.appendleft(5)
print(d)

d.popleft()
print(d)

d.extend([7,6,8])
print(d)

d.rotate(1)
print(d)