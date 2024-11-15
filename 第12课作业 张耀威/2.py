import random as r
公鸡=5
母鸡=3
小鸡=1
n=0
for x in range(21):             #公鸡数
    for y in range(34):
        z=100-x-y
        if(公鸡*x+母鸡*y+小鸡*z/3==100):
            print("可以买公鸡",x,"可以买母鸡",y,"可以买小鸡",z)
            n+=1
print("共有%d种方法"%n)


