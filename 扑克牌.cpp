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
 // ��������ð������
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
	
	   // ������3
    strcpy(pkp[0].name, "���� 3");
    strcpy(pkp[1].name, "÷�� 3");
    strcpy(pkp[2].name, "���� 3");
    strcpy(pkp[3].name, "���� 3");
    // ������4
    strcpy(pkp[4].name, "���� 4");
    strcpy(pkp[5].name, "÷�� 4");
    strcpy(pkp[6].name, "���� 4");
    strcpy(pkp[7].name, "���� 4");
    // ������5
    strcpy(pkp[8].name, "���� 5");
    strcpy(pkp[9].name, "÷�� 5");
    strcpy(pkp[10].name, "���� 5");
    strcpy(pkp[11].name, "���� 5");
    // ������6
    strcpy(pkp[12].name, "���� 6");
    strcpy(pkp[13].name, "÷�� 6");
    strcpy(pkp[14].name, "���� 6");
    strcpy(pkp[15].name, "���� 6");
    // ������7
    strcpy(pkp[16].name, "���� 7");
    strcpy(pkp[17].name, "÷�� 7");
    strcpy(pkp[18].name, "���� 7");
    strcpy(pkp[19].name, "���� 7");
    // ������8
    strcpy(pkp[20].name, "���� 8");
    strcpy(pkp[21].name, "÷�� 8");
    strcpy(pkp[22].name, "���� 8");
    strcpy(pkp[23].name, "���� 8");
    // ������9
    strcpy(pkp[24].name, "���� 9");
    strcpy(pkp[25].name, "÷�� 9");
    strcpy(pkp[26].name, "���� 9");
    strcpy(pkp[27].name, "���� 9");
    // ������10
    strcpy(pkp[28].name, "���� 10");
    strcpy(pkp[29].name, "÷�� 10");
    strcpy(pkp[30].name, "���� 10");
    strcpy(pkp[31].name, "���� 10");
    // ��ĸ��J
    strcpy(pkp[32].name, "���� J");
    strcpy(pkp[33].name, "÷�� J");
    strcpy(pkp[34].name, "���� J");
    strcpy(pkp[35].name, "���� J");
    // ��ĸ��Q
    strcpy(pkp[36].name, "���� Q");
    strcpy(pkp[37].name, "÷�� Q");
    strcpy(pkp[38].name, "���� Q");
    strcpy(pkp[39].name, "���� Q");
    // ��ĸ��K
    strcpy(pkp[40].name, "���� K");
    strcpy(pkp[41].name, "÷�� K");
    strcpy(pkp[42].name, "���� K");
    strcpy(pkp[43].name, "���� K");
    // ��ĸ��A
    strcpy(pkp[44].name, "���� A");
    strcpy(pkp[45].name, "÷�� A");
    strcpy(pkp[46].name, "���� A");
    strcpy(pkp[47].name, "���� A");
    // ������2��2 > A��
    strcpy(pkp[48].name, "���� 2");
    strcpy(pkp[49].name, "÷�� 2");
    strcpy(pkp[50].name, "���� 2");
    strcpy(pkp[51].name, "���� 2");
    // ��С��
    strcpy(pkp[52].name, "С��");
    strcpy(pkp[53].name, "����");

     // �����߼�
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

   

    // �������
    sort_cards(farmer1, 17);
    printf("ũ��1���ƣ�");
    for (int i = 0; i < 17; i++) printf("%s ", farmer1[i].name);
    printf("\n");

    sort_cards(farmer2, 17);
    printf("ũ��2���ƣ�");
    for (int i = 0; i < 17; i++) printf("%s ", farmer2[i].name);
    printf("\n");

    sort_cards(landlord, 20);
    printf("�������ƣ�");
    for (int i = 0; i < 20; i++) printf("%s ", landlord[i].name);
    printf("\n");

    return 0;
	
}






