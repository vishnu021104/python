x=[[10,39,56],
   [35,77,26],
   [24,75,14]]

y=[[63,79,26],
   [65,97,23],
   [54,12,94]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

# print(len(x))

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)        

