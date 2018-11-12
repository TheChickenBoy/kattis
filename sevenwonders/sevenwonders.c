#include <stdio.h>
#include <math.h>

int main(void){
    int t[3]={0},s=0,sm=0;
    char in[52]={0};

    if(fgets(in,52,stdin)){
        for(int i=0;i<52;i++){
            if(in[i]=='T' || in[i]=='C' || in[i]=='G'){
                if(in[i]=='T')
                    t[0]++;
                else if(in[i]=='C')
                    t[1]++;
                else
                    t[2]++;
            }else
                break;
        }
        if(t[0]<=t[1] && t[0]<=t[2])
            sm = t[0];
        else if (t[1]<=t[0] && t[1]<=t[2])
            sm = t[1];
        else
            sm = t[2];

        s = pow(t[0],2) + pow(t[1],2) + pow(t[2],2) + 7*sm;
    }
    printf("%d\n", s);
    return 0;
}
