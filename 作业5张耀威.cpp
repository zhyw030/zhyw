//���Ƴ����⣺����N�����������ֲ�����4���������������������
//���г��򲻵øĶ����������Ҫ�����������һ��
#include <stdio.h>
#include <string.h>
#define N 5
// ���뺯��
void input(char name[][10], int n) {
    printf("������%d��������\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%s", name[i]);
    }
    printf("\n"); 
}
// ������������ð������
void sort(char name[][10], int n) {
    char temp[10];
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (strcmp(name[j], name[j + 1]) > 0) {
                strcpy(temp, name[j]);
                strcpy(name[j], name[j + 1]);
                strcpy(name[j + 1], temp);
            }
        }
    }
}
// �������
void output(char name[][10], int n) {
    for (int i = 0; i < n; i++) {
        printf("%s\n", name[i]);
    }
}

int main()
{
    char name[5][10];
    input(name,N);  //����N������
    sort(name,N);   //��N��������������
    output(name,N); //���N������
    return 0;
}
