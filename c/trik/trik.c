#include <stdio.h>
#define SIZE 51

int main(void){
    char str[SIZE] = {0};
    int c , i=0, curr,temp;
    while((c = getchar()) != '\n' && c != EOF)
        str[i++] = c;

    curr = 'A';
    for(int j=0;j<SIZE;j++){
        temp=str[j];
        if(temp == '\0')
            break;

        else if(temp == 'A'){
            if(curr == 'A')
                curr = 'B';
            else if (curr == 'B')
                curr = 'A';
        } else if(temp == 'B'){
            if(curr == 'B')
                curr = 'C';
            else if (curr == 'C')
                curr = 'B';
        } else if(temp == 'C'){
            if(curr == 'C')
                curr = 'A';
            else if (curr == 'A')
                curr = 'C';
        }
    }
    printf("%d\n", curr-'A'+1);
    return 0;
}
