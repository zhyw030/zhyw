


c=1
while(c!=0):
    a=input("请选择是加密还是解密1.加密 2.解密")
    #---------加密-----------
    if(a=="1"):
        b=input("请输入要加密的内容")
        for i in b:
            if(ord(i)>87 and ord(i)<97):
                print(chr(ord(i)-87+65),end="")
            elif(ord(i)>119):
                print(chr(ord(i)-119+97),end="")
            else:
                print(chr(ord(i)+3),end="")
        print()
    #-----------解密----------
    if(a=="2"):
        b=input("请输入要解密的内容")
        for i in b:
            if(ord(i)>96 and ord(i)<100):
                print(chr(ord(i)-99+122),end="")
            elif(ord(i)>64 and ord(i)<68):
                print(chr(ord(i)-67+90),end="")
            else:
                print(chr(ord(i)-3),end="")
        print()
    c=input("是否要再来一次？1.是 2.否")
    if(c=="1"):
        c=1
    else:
        c=0





