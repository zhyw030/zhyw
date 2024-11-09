"""
#9
for i in range(1,10):
    print("ix9=%d\t"%(i,i*9),end="")
print()
#8
for i in range(1,9):
    print("ix8=%d\t"%(i,i*8),end="")
print()
#7
for i in range(1,8):
    print("ix7=%d\t"%(i,i*7),end="")
print()
#6
for i in range(1,7):
    print("ix6=%d\t"%(i,i*6),end="")
print()
#5
for i in range(1,6):
    print("ix5=%d\t"%(i,i*5),end="")
print()"""
for j in range(9):
    for i in range(1,j+2):
        print("%dx%d=%d\t"%(i,j+1,i*(j+1)),end="")
    print()
print()
for x in range(9,0,-1):
    for y in range(1,x+1):
        print("%dx%d=%d\t"%(y,x,y*x),end="")
    print()
    













