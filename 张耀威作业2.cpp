#include <stdio.h>
#define N 10
float min(float s[],int n)
{
	int i;
	float x;
	for(i=1;i<n;i++)
	{
		if(s[0]>s[i]&&s[i]!=0)
		{
			s[0]=s[i];
		}
	}
	return s[0];
}
//======================================
float max(float s[],int n)
{int i;
	float q;
	for(i=1;i<n;i++)
	{
		if(s[0]<s[i])
		{
			s[0]=s[i];
		}
	}
	return s[0];
}
//======================================
float ave(float s[],int n)
{
	float sum=0.0;
	float x;
	float q;
	int i;
	for(i=0;i<n;i++)
	{
		sum=sum+s[i];
	}
	sum=sum-min(s,n)-max(s,n);
	return sum/8.0;
}
//======================================
int main()
{
	float score[N]={9.8, 8.5, 7.8, 8.5, 9.3, 9.8, 8.9, 7.8, 8.6, 8.4};
	printf("��ͷ�Ϊ%.1f,��߷�Ϊ%.1f,ƽ����Ϊ%.3f",min(score,N),max(score,N),ave(score,N));
	return 0;
}
