#include <stdio.h>

int main(void){
    int n=0;
    char bapc[100000]={'\0'};
    if(fscanf(stdin,"%d",&n)){
        for(int i=0;i<n;i++){
            int t=0;
            char list[1000]={'\0'};
            if(fgets(bapc, sizeof bapc, stdin)!=NULL)
                if(fscanf(stdin,"%d",&t))
                    if(fgets(list, sizeof list, stdin)!=NULL);

            for(int j=0;j<1000;j++){
                if(list[i]=='\0')
                    break;
                printf("%c",list[i]);
            }
            printf("\n");
        }
    }
}
