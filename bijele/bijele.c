#include <stdio.h>

int kq(int n){
    if(n==1)
        return 0;
    else if(n==0)
        return 1;
    else
        switch (n) {
            case 2:
                return -1;
            case 3:
                return -2;
            case 4:
                return -3;
            case 5:
                return -4;
            case 6:
                return -5;
            case 7:
                return -6;
            case 8:
                return -7;
            case 9:
                return -8;
            case 10:
                return -9;
        }
    return -11;
}
int rbk(int n){
    if(n==2)
        return 0;
    else if(n==1)
        return 1;
    else if(n==0)
        return 2;
    else
        switch (n) {
            case 3:
                return -1;
            case 4:
                return -2;
            case 5:
                return -3;
            case 6:
                return -4;
            case 7:
                return -5;
            case 8:
                return -6;
            case 9:
                return -7;
            case 10:
                return -8;
        }
    return -11;
}
int pawns(int n){
    switch (n) {
        case 0:
            return 8;
        case 1:
            return 7;
        case 2:
            return 6;
        case 3:
            return 5;
        case 4:
            return 4;
        case 5:
            return 3;
        case 6:
            return 2;
        case 7:
            return 1;
        case 8:
            return 0;
        case 9:
            return -1;
        case 10:
            return -2;
    }
    return -11;
}
int main(void){
    int king=0,q=0,r=0,b=0,k=0,p=0;
    if(fscanf(stdin,"%d %d %d %d %d %d",&king,&q,&r,&b,&k,&p)){
        printf("%d %d %d %d %d %d\n", kq(king),kq(q),rbk(r),rbk(b),rbk(k),pawns(p));
    }
}
