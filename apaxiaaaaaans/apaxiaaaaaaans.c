#include <stdio.h>

int main(void){
    char str[251] = {'\0'};
    char ret[251] = {'\0'};
    char c = '\0';
    if(fgets(str,sizeof(str),stdin) != NULL){
        for(int i=0,j=0;i<251;i++){
            char temp = str[i];
            if(c == temp)
                continue;
            else {
                c = temp;
                ret[j++] = temp;
            }
        }
        printf("%s", ret);
    }
    return 0;
}
