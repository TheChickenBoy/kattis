#include <stdio.h>

int rev(int a){
    int ret = 0.0;
    while(a != 0){
        ret = ret *10;
        ret = ret +a%10;
        a = a/10;
    }
    return ret;
}

int main(void){
    int a=0,b=0;
    if(fscanf(stdin,"%d %d",&a,&b) >0){
        a = rev(a);
        b = rev(b);
        if(a<b){
            printf("%d\n", b);
        }else
            printf("%d\n", a);
    }

    return 0;
}
