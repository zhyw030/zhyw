//�ж�һ����(С��1000000)��λ������3467Ϊһ��4λ��
//���г��򲻵øĶ����������Ҫ�����������һ��
int fun(int n) //��n��λ���Ӻ���
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
        printf("������һ��������");
        scanf("%d",&a);
        printf("%d��һ��%dλ��\n\n",a,fun(a));
    }
    return 0;
}
