n=0
for x in range(6):
    for y in range(11):
        for z in range(51):
            if(x*10+y*5+z==50):
                #print(x,y,z)
                n+=1
print("共有%d种方法"%n)




