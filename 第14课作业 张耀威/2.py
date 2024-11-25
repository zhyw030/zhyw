a=1               #羊
b=-1              #狼
c=-1              #草
qd=[a,b,c]
zd=[]
def move(sz,dh,lb1,lb2,j,k):
    print(f"把{dh}从{j}运到{k}")
    i=lb1.index(sz)
    lb1.pop(i)
    lb2.append(sz)
for p in range(4):
    m=sum(qd)
    if(m==-1 or m==1 ):
        move(a,"羊",qd,zd,"起点","终点")

    elif(m==-2):
        move(b,"狼",qd,zd,"起点","终点")
    else:
        move(c,"菜",qd,zd,"起点","终点")
    n=sum(zd)
    if(n==0):
        move(a,"羊",zd,qd,"终点","起点")
print(qd,zd)




