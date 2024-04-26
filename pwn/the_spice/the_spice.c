#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct spice_buyer {
    unsigned int spice_amount;
    char name[12];
};

void prompt(void) {
    printf("Choose an option:\n");
    printf("(1) View a buyer\n");
    printf("(2) Add a buyer\n");
    printf("(3) Update a buyer's spice allocation\n");
    printf("(4) Remove a buyer\n");
    printf("(5) Sell the spice\n");
}

int main() {
    struct spice_buyer buyers[8];
    char buf[16];
    int i, num, len, spice;

    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    memset(buyers, 0, sizeof(buyers));

    srand(time(NULL));
    spice = rand() % 100;

    printf("House Harkonnen has finally taken control of Arrakis, and with it control of the crucial spice.\n");
    printf("However, the Baron poured all of his funds into exterminating House Atreides.\n");
    printf("Luckily, we sent some guys to drop the last of them into the desert, so that's all taken care of.\n");
    printf("\n");
    printf("For some reason our spice harvesters keep getting raided though?\n");
    printf("As a result, spice production is lower than expected.\n");
    printf("\n");
    printf("Can you help the Baron distribute the %d tons of spice among his prospective buyers?\n", spice);
    printf("\n");

    while (727) {
        prompt();
        printf("> ");

        fgets(buf, sizeof(buf), stdin);
        num = atoi(buf);

        switch (num) {
        case 1:
            printf("Enter the buyer index: ");
            fgets(buf, sizeof(buf), stdin);
            num = atoi(buf);

            struct spice_buyer *buyer = &buyers[num];
            printf("Buyer %d: %s, allocated %u tons of spice\n", num, buyer->name, buyer->spice_amount);

            break;
        case 2:
            printf("Enter the buyer index: ");
            fgets(buf, sizeof(buf), stdin);
            num = atoi(buf);

            if (num < 0 || num >= 8) {
                printf("Invalid index!\n");
                continue;
            }

            printf("How long is the buyer's name? ");
            fgets(buf, sizeof(buf), stdin);
            len = atoi(buf);
            
            printf("Enter the buyer's name: ");
            fgets(buyers[num].name, len, stdin);
            buyers[num].name[strcspn(buyers[num].name, "\n")] = '\0';

            printf("Enter the spice allocation (in tons) to this buyer: ");
            fgets(buf, sizeof(buf), stdin);
            buyers[num].spice_amount = atoi(buf);

            break;
        case 3:
            printf("Enter the buyer index: ");
            fgets(buf, sizeof(buf), stdin);
            num = atoi(buf);

            if (num < 0 || num >= 8) {
                printf("Invalid index!\n");
                continue;
            }

            printf("Enter the spice allocation (in tons) to this buyer: ");
            fgets(buf, sizeof(buf), stdin);
            buyers[num].spice_amount = atoi(buf);

            break;
        case 4:
            printf("Enter the buyer index: ");
            fgets(buf, sizeof(buf), stdin);
            num = atoi(buf);

            if (num < 0 || num >= 8) {
                printf("Invalid index!\n");
                continue;
            }

            strcpy(buyers[num].name, "");
            buyers[num].spice_amount = 0;

            break;
        default:
            for (i = 0; i < 8; i++) {
                spice -= buyers[i].spice_amount;
            }

            if (spice < 0) {
                printf("You oversold your spice resources. The Spacing Guild is extremely angry, and has revoked your shipping privileges.\n");
                exit(1);
            } else if (spice == 0) {
                printf("You sold all of the spice! The Baron wanted you to sell it slowly to inflate the price! He is extremely angry with you.\n");
                exit(1);
            } else {
                printf("You sold the spice, and have %d tons remaining. You live to see another day.\n", spice);
                exit(0);
            }
        }
    }
}

