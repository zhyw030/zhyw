#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
struct kp
	{
		char name[5];
		int a;
		int b;
	}pkp[54];
 // 排序函数（冒泡排序）
    void sort_cards(struct kp cards[], int len) {
        for (int i = 0; i < len ; i++) {
            for (int j = i+1; j < len ; j++) {
                if (cards[i].a < cards[j].a) {
                    struct kp temp = cards[i];
                    cards[i] = cards[j];
                    cards[j] = temp;
                }
            }
        }
    }
int main()
{
	
	   // 数字牌3
    strcpy(pkp[0].name, "方块 3");
    strcpy(pkp[1].name, "梅花 3");
    strcpy(pkp[2].name, "红心 3");
    strcpy(pkp[3].name, "黑桃 3");
    // 数字牌4
    strcpy(pkp[4].name, "方块 4");
    strcpy(pkp[5].name, "梅花 4");
    strcpy(pkp[6].name, "红心 4");
    strcpy(pkp[7].name, "黑桃 4");
    // 数字牌5
    strcpy(pkp[8].name, "方块 5");
    strcpy(pkp[9].name, "梅花 5");
    strcpy(pkp[10].name, "红心 5");
    strcpy(pkp[11].name, "黑桃 5");
    // 数字牌6
    strcpy(pkp[12].name, "方块 6");
    strcpy(pkp[13].name, "梅花 6");
    strcpy(pkp[14].name, "红心 6");
    strcpy(pkp[15].name, "黑桃 6");
    // 数字牌7
    strcpy(pkp[16].name, "方块 7");
    strcpy(pkp[17].name, "梅花 7");
    strcpy(pkp[18].name, "红心 7");
    strcpy(pkp[19].name, "黑桃 7");
    // 数字牌8
    strcpy(pkp[20].name, "方块 8");
    strcpy(pkp[21].name, "梅花 8");
    strcpy(pkp[22].name, "红心 8");
    strcpy(pkp[23].name, "黑桃 8");
    // 数字牌9
    strcpy(pkp[24].name, "方块 9");
    strcpy(pkp[25].name, "梅花 9");
    strcpy(pkp[26].name, "红心 9");
    strcpy(pkp[27].name, "黑桃 9");
    // 数字牌10
    strcpy(pkp[28].name, "方块 10");
    strcpy(pkp[29].name, "梅花 10");
    strcpy(pkp[30].name, "红心 10");
    strcpy(pkp[31].name, "黑桃 10");
    // 字母牌J
    strcpy(pkp[32].name, "方块 J");
    strcpy(pkp[33].name, "梅花 J");
    strcpy(pkp[34].name, "红心 J");
    strcpy(pkp[35].name, "黑桃 J");
    // 字母牌Q
    strcpy(pkp[36].name, "方块 Q");
    strcpy(pkp[37].name, "梅花 Q");
    strcpy(pkp[38].name, "红心 Q");
    strcpy(pkp[39].name, "黑桃 Q");
    // 字母牌K
    strcpy(pkp[40].name, "方块 K");
    strcpy(pkp[41].name, "梅花 K");
    strcpy(pkp[42].name, "红心 K");
    strcpy(pkp[43].name, "黑桃 K");
    // 字母牌A
    strcpy(pkp[44].name, "方块 A");
    strcpy(pkp[45].name, "梅花 A");
    strcpy(pkp[46].name, "红心 A");
    strcpy(pkp[47].name, "黑桃 A");
    // 数字牌2（2 > A）
    strcpy(pkp[48].name, "方块 2");
    strcpy(pkp[49].name, "梅花 2");
    strcpy(pkp[50].name, "红心 2");
    strcpy(pkp[51].name, "黑桃 2");
    // 大小王
    strcpy(pkp[52].name, "小王");
    strcpy(pkp[53].name, "大王");

     // 发牌逻辑
    struct kp farmer1[17], farmer2[17], landlord[20];
    int f1_idx = 0, f2_idx = 0, ld_idx = 0;
    srand((unsigned int)time(NULL));
	for(int i=0;i<=53;i++)
	{
		pkp[i].a=i;
		pkp[i].b=0;
	}
	//pkp[53].a=100;
    while (f1_idx < 17 || f2_idx < 17 || ld_idx < 20) {
        int num = rand() % 54;
        if (pkp[num].b == 0) {
            if (f1_idx < 17) {
                farmer1[f1_idx] = pkp[num];
                f1_idx++;
            } else if (f2_idx < 17) {
                farmer2[f2_idx] = pkp[num];
                f2_idx++;
            } else {
                landlord[ld_idx] = pkp[num];
                ld_idx++;
            }
            pkp[num].b = 1;
        }
    }

   

    // 排序并输出
    sort_cards(farmer1, 17);
    printf("农民1的牌：");
    for (int i = 0; i < 17; i++) printf("%s ", farmer1[i].name);
    printf("\n");

    sort_cards(farmer2, 17);
    printf("农民2的牌：");
    for (int i = 0; i < 17; i++) printf("%s ", farmer2[i].name);
    printf("\n");

    sort_cards(landlord, 20);
    printf("地主的牌：");
    for (int i = 0; i < 20; i++) printf("%s ", landlord[i].name);
    printf("\n");

    return 0;
	
}






