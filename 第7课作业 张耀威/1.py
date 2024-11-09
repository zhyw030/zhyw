ls=[12,0,10,9,8,-1,21,-6]
#================第1轮比较
for i in range(len(ls)-1):
    if(ls[0]<ls[i+1]):
        a=ls[0]
        ls[0]=ls[i+1]
        ls[i+1]=a
print(ls)
#=================第2轮比较
for i in range(1,len(ls)-1):
    if(ls[1]<ls[i+1]):
        ls[1],ls[i+1]=ls[i+1],ls[1]
print(ls)
#==================第3轮比较
for i in range(2,len(ls)-1):
    if(ls[2]<ls[i+1]):
        ls[2],ls[i+1]=ls[i+1],ls[2]
print(ls)
#================第4轮比较
for i in range(3,len(ls)-1):
    if(ls[3]<ls[i+1]):
        a=ls[3]
        ls[3]=ls[i+1]
        ls[i+1]=a
print(ls)
#=================第5轮比较
for i in range(4,len(ls)-1):
    if(ls[4]<ls[i+1]):
        a=ls[4]
        ls[4]=ls[i+1]
        ls[i+1]=a
print(ls)
#==================第6轮比较
for i in range(5,len(ls)-1):
    if(ls[5]<ls[i+1]):
        a=ls[5]
        ls[5]=ls[i+1]
        ls[i+1]=a
print(ls)
#================第7轮比较
for i in range(6,len(ls)-1):
    if(ls[6]<ls[i+1]):
        a=ls[6]
        ls[6]=ls[i+1]
        ls[i+1]=a
print(ls)

"""for j in range(len(ls)-1):
    for i in range(len(ls)-j-1):
        if(ls[j]>ls[j+i+1]):
            #a=ls[j]
            #ls[j]=ls[j+i+1]
            #ls[j+i+1]=a
            ls[j],ls[j+i+1]=ls[j+i+1],ls[j]
print(ls)
def sz(lb):
    for j in range(len(lb)-1):
        for i in range(len(lb)-j-1):
            if(lb[j]>ls[j+i+1]):
            #a=ls[j]
            #ls[j]=ls[j+i+1]
            #ls[j+i+1]=a
                lb[j],lb[j+i+1]=lb[j+i+1],lb[j]
    print(lb)
sz(ls)"""







    
    
