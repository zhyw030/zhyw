#include <stdio.h>
int fun1(int n)
{
	if(n==1)
		return 1;
	else return n*fun1(n-1);
}
//=========================================//
int fun2(int n)
{
	if(n==1)
		return fun1(1);
	else return fun1(n)+fun2(n-2);
	
}
//=========================================//
int main()
{
	printf("1!+3!+5!+...+11!=%d",fun2(11));
	return 0;
}
