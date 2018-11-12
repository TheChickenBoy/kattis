#include <stdio.h>

int main(void){
    int n=0,s=0,tt=0,t=0,d=0;
    for(;;) {
        n=0;s=0;tt=0;t=0;d=0;
        if(fscanf(stdin,"%d",&n)){
            if(n!=-1){
                for(int i=0;i<n;i++){
                    if(fscanf(stdin,"%d %d",&s,&t)){
                        t=t-tt;
                        d=d+(s*t);
                        tt = t+tt;
                    }
                }
            } else
                return 0;
        }
        printf("%d miles\n", d);
    }

}
