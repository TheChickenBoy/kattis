#include <stdio.h>

int main(void){
    int cont[5]={0},t1,t2,t3,t4,curHI=0;
    for(int i=0;i<5;i++)
        if(fscanf(stdin,"%d %d %d %d",&t1,&t2,&t3,&t4)){
            cont[i] = t1+t2+t3+t4;
            if(cont[i]>cont[curHI])
                curHI=i;
        }

    printf("%d %d\n",curHI+1,cont[curHI]);
    return 0;
}
