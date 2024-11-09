ls=[12,0,10,9,8,-1,21,-6]
print(ls)
for j in range(6):
    for i in range(0,len(ls)-1 ):
        if(ls[i]<ls[i+1]):
            ls[i],ls[i+1]=ls[i+1],ls[i]
    print(j,ls)

























