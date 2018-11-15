#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void bubble(int arr[],int n){
    int i, j;
    for (i = 0; i < n-1; i++)
        for (j = 0; j < n-i-1; j++)
            if (arr[j] < arr[j+1])
               swap(&arr[j], &arr[j+1]);
}

void sum(int arr[],int n){
    int s1=0,s2=0;
    for(int i=0;i<n;i++){
        if(i%2==0)
            s1 = s1+arr[i];
        else
            s2 = s2+arr[i];
    }

    printf("%d %d\n", s1, s2);
}
int main(void){
    int n=0,t=0;
    if(fscanf(stdin,"%d",&n)){
        int nr[n]={0};
        for(int i=0;i<n;i++)
            if(fscanf(stdin,"%d",&t))
                nr[i]=t;

        bubble(nr,n);
        sum(nr, n);
    }
    return 0;
}
