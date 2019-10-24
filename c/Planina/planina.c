#include <stdio.h>

int main(void){
    int n=0,cur=2;
    if(fscanf(stdin,"%d",&n))
        for(int i=0;i<n;i++)
            cur = cur+(cur-1);
    printf("%d\n", cur*cur);
    return 0;
}
