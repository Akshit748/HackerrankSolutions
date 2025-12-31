#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch;
    char str[100];
    char sentence[200];

    scanf("%c", &ch);

    scanf("%s", str);

    getchar();

    fgets(sentence, sizeof(sentence), stdin);

    // Print all
    printf("%c\n", ch);
    printf("%s\n", str);
    printf("%s", sentence);

    return 0;
}
