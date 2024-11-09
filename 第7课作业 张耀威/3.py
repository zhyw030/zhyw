ls=[12,0,10,9,8,-1,21,-6]
for i in range(1,len(ls)):
    j=i-1
    a=ls[i]
    while j>=0 and ls[j]<a:
            ls[j+1]=ls[j]
            j-=1
    ls[j+1]=a
print(ls)










