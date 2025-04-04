//判断一个数(小于1000000)的位数，如3467为一个4位数
//已有程序不得改动，输入输出要求与测试样例一致
int fun(int n) //求n的位数子函数
{
	int count=0;
	if(n==0)
	{
		return 1;
	} 
	while(n>0)
	{
		n/=10;
		count++;
	}
	return count ;
}

#include <stdio.h>
int main()
{
    int i,a;
    for(i=0;i<6;i++)
    {
        printf("请输入一个整数：");
        scanf("%d",&a);
        printf("%d是一个%d位数\n\n",a,fun(a));
    }
    return 0;
}
