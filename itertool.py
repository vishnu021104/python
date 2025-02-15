from itertools import product
a=[7,3]
b=[1,6]
prod=product(a,b)
# print(list(prod))

from itertools import permutations
a=[1,2,3]
perm=permutations(a)
# print(list(perm))

from itertools import combinations
a=[1,2,3]
comb=combinations(a,2)
# print(list(comb))

from itertools import accumulate
a=[1,2,3,4,5]
acc=accumulate(a)
# print(a)
# print(list(acc))

from itertools import count

for i in count(10):
    print(i)
    if i==20:
        break

from itertools import cycle
a=[1,2,3,4,5]
for i in cycle(a):
    print(i)


from itertools import repeat
a=[1,2,3,4,5]
for i in repeat(1,7):
    print(i)