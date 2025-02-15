# addition matrix

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


# multipication matrix
x=[[1,3,5],
   [3,7,6],
   [2,7,1]]

y=[[6,7,2],
   [6,5,3],
   [4,1,9]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

# print(len(x))

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j]+=x[i][k]*y[k][j]
for r in result:
    print(r)        

                

