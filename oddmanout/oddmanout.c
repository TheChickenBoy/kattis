#include <stdio.h>
#include <string.h>

void pr(int n, int pair[], int guest[]){
    for(int x=0;x<1000;x++)
        if(pair[x]==0){
            printf("Case #%d: %d\n", n+1, guest[x]);
            return;
        }
}

int check(int n, int guest[1000]){
    for(int i=0;i<1000;i++){
        if(guest[i] == n)
            return i;
    }
    return -1;
}

int main(void){
    int guest[1000]={-1};
    int pair[1000]={0};
    int n=0,g=0,c=0,q=0;

    if(fscanf(stdin,"%d",&n))
        for(int i=0;i<n;i++){
            memset(guest,-1,1000);
            memset(pair,0x00,1000);
            g=0;c=0;q=0;
            if(fscanf(stdin,"%d",&g))
                for (int j=0;j<g;j++) {
                    if(fscanf(stdin,"%d",&c)){
                        int t = check(c,guest);
                        if(t!=-1)
                            pair[t]++;
                        else
                            guest[q++] = c;
                    }
                }
            pr(i,pair,guest);
        }
    return 0;
}
