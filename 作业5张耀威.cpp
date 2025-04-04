//完善程序题：输入N个人名（汉字不超过4个），升序输出人名排序
//已有程序不得改动，输入输出要求与测试样例一致
#include <stdio.h>
#include <string.h>
#define N 5
// 输入函数
void input(char name[][10], int n) {
    printf("请输入%d个人名：\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%s", name[i]);
    }
    printf("\n"); 
}
// 排序函数，采用冒泡排序
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
// 输出函数
void output(char name[][10], int n) {
    for (int i = 0; i < n; i++) {
        printf("%s\n", name[i]);
    }
}

int main()
{
    char name[5][10];
    input(name,N);  //输入N个人名
    sort(name,N);   //对N个人名进行排序
    output(name,N); //输出N个人名
    return 0;
}
