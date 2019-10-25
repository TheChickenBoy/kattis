#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(){
    int n, k, index=0;
    int fo = 0;
    char ans[100] = {'\0'};
    scanf("%d", &n);

    for (int c = 31; c >= 0; c--){
        k = n >> c;
        if (k & 1){
            ans[index++] = '1';
            fo = 1;
        }
        else{
            if(fo)
                ans[index++] = '0';
        }
    }

    index--;
    char str[index+1];
    for(int i=-1; i<=index;i++)
        str[i] = ans[index-i];
    str[index+1] = '\0';
    unsigned long num = strtoul(str,NULL,10);
    int rest = 0, a = 0;
    for(int i = 0; num != 0; i++){
        rest = num%10;
        num /= 10;
        a += rest*pow(2,i);
    }
    printf("%d\n",a);
    return 0;
}
