//对输入一个字符串，输出这个串的英文字符个数
//已有程序不得改动，输入输出要求与测试样例一致
#include <stdio.h>
int count(char s[])
{
	int num=0;
	int i=0;
	while(s[i]!='\0')
	{
		if((s[i]>='a'&&s[i]<='z')||(s[i]>='A'&&s[i]<='Z'))
		{
			num++;
		}
		i++;
	}
	return num;
}

int main()
{
    char str[20];
    printf("请输入字符串(不超过15个字符)：");
    scanf("%s",str);
    printf("字符串中共有%d个英文字符",count(str));
    return 0;
}
