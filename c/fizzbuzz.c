#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void){
    int x=0,y=0,n=0;
    char *fizz="",*buzz="";
    if(fscanf(stdin,"%d %d %d",&x,&y,&n)>0){
        for(int i=1;i<=n;i++){
            fizz = "";
            buzz = "";
            if(i%x==0)
                fizz="Fizz";
            if(i%y==0)
                buzz="Buzz";
            if(fizz != "" || buzz != "")
                printf("%s%s\n", fizz,buzz);
            else
                printf("%d\n", i);
        }
    }
    return 0;
}
