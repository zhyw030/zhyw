//������һ���ַ���������������Ӣ���ַ�����
//���г��򲻵øĶ����������Ҫ�����������һ��
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
    printf("�������ַ���(������15���ַ�)��");
    scanf("%s",str);
    printf("�ַ����й���%d��Ӣ���ַ�",count(str));
    return 0;
}
