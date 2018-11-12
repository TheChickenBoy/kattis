#include <stdio.h>
#include <string.h>

int main(void){
    int d = 0;
    char s[4] = {0};

    if(fscanf(stdin,"%s %d",s,&d)){
        if((strcmp(s,"OCT")==0 && d==31) || (strcmp(s,"DEC")==0 && d==25)){
            printf("yup\n");
        }else
            printf("nope\n");
    }
    return 0;
}
