ls1=[12,0,8,9,6,1,21,46]
ls2=[3,88,-2,90,100]
ls3=[6,-3,9,12,44,0,50,70,-23,8]

def sz(ls):
    for j in range(len(ls)-1):
        for i in range(len(ls)-j-1):
            if(ls[j]>ls[j+i+1]):
            #a=ls[j]
            #ls[j]=ls[j+i+1]
            #ls[j+i+1]=a
                ls[j],ls[j+i+1]=ls[j+i+1],ls[j]
    print(ls)
sz(ls1)
sz(ls2)
sz(ls3)

