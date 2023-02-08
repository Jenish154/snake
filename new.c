#include <stdio.h>

int main() {
    int num;
    printf("Enter the length of the word: ");
    scanf("%d", &num);
    printf("\n");
    char word[num];
    printf("Enter the word: ");
    scanf("%s", &word);
    printf("\n");
    char new[num];
    char prev;
    for (int i=0; i<num; i++) {
        if (prev == word[i]){
            continue;
        }
        new[i] = word[i];
        prev = word[i];
    }
    num = sizeof(new)/sizeof(new[0]);
    for (int i=0; i<num; i++) {
        if (new[i] == 0){
            continue;
        }
        printf("%dth position of the word is: %c\n", i+1, new[i]);
    }
    return 0;
}