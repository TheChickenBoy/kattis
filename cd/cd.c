#include <stdio.h>
#include <string.h>
#define SIZE 1000000000
char nr[SIZE];

int main(void){
    //*char nr[SIZE] = malloc(SIZE);
    int n=0,m=0,eq;
    for(;;) {
        eq = 0;
        memset(nr,0x00,SIZE);
        if(fscanf(stdin,"%d %d",&n,&m)>0){
            if(n == 0 && m == 0)
                return 0;
            if(n == 0 || m == 0){
                printf("0\n");
                continue;
            }
            int temp=0;
            for(int i=0;i<n;i++){
                if(fscanf(stdin,"%d",&temp)){
                    nr[temp]++;
                }
            } for(int i=0;i<m;i++){
                if(fscanf(stdin,"%d",&temp)){
                    if(nr[temp] == 1)
                        eq++;
                }
            }
            printf("%d\n", eq);
        }
    }
    return 0;
}
