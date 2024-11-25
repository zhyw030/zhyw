for i in range(1,100):
    sum=0.0001*2**i
    if(sum>=8848.18):
        print("对折%d次后厚度将超过珠穆朗玛峰的高度"%i)
        break
