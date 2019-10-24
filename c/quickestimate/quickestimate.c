#include <stdio.h>

int main(void){
    char str[200]={'\0'};
    int n=0,nr=0;
    if(fscanf(stdin,"%d ",&n))
        for(int i=0;i<n;i++){
            if(fgets(str,200,stdin) != NULL){
                int j=0;
                do {
                    nr++;
                } while(str[++j]!='\n');
            }
            printf("%d\n",nr);
            nr=0;
        }
    return 0;
}
