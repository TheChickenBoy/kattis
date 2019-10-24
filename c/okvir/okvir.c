#include <stdio.h>

int main(void){
    int m=0,n=0,u=0,l=0,r=0,d=0,wi=0,pr=0;
    char words[110]={"\0"};
    if(fscanf(stdin,"%d %d",&m,&n))
        if(fscanf(stdin,"%d %d %d %d",&u,&l,&r,&d)){
            for(int i=0;i<m;i++)
                if(fscanf(stdin,"%s",&words[i*n]));

            for(int j=0;j<u;j++){
                for(int x=0;x<n+r+l;x++){
                    if(pr%2==0 && x%2==0)
                        printf("#");
                    else if((pr%2!=0 && x%2==0)|| (pr%2==0 && x%2!=0))
                        printf(".");
                    else
                        printf("#");
                }
                pr++;
                printf("\n");
            }

            for(int j=0;j<m;j++){
                for(int x=0;x<l;x++){
                    if((pr%2==0 && x%2==0)){
                        printf("#");
                    }
                    else if((pr%2!=0 && x%2==0)|| (pr%2==0 && x%2!=0)){
                        printf(".");
                    }
                    else{
                        printf("#");
                    }
                }
                for(int ti=0;ti<n;ti++){
                    if(words[wi]=='\0')
                        break;
                    printf("%c", words[wi]);
                    wi++;
                }
                for(int x=0;x<r;x++){
                    if((pr%2==0 && x%2==0 && x%2==0)){
                        printf((n+l) % 2 == 0  ? "#" : ".");
                    }
                    else if(((pr%2!=0 && x%2==0)|| (pr%2==0 && x%2!=0))){
                        printf((n+l) % 2 == 0  ? "." : "#");
                    }
                    else{
                        printf((n+l) % 2 == 0  ? "#" : ".");
                    }
                }
                pr++;
                printf("\n");
            }


            for(int j=0;j<d;j++){
                for(int x=0;x<n+r+l;x++){
                    if(pr%2==0 && x%2==0)
                        printf("#");
                    else if((pr%2!=0 && x%2==0)|| (pr%2==0 && x%2!=0))
                        printf(".");
                    else
                        printf("#");
                }
                pr++;
                printf("\n");
            }
        }


    printf("\n");
    return 0;
}
