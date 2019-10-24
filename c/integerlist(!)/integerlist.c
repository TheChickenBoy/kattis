#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define SIZE 7

/* Function:    splitString
 * Description: Reads the information in a string and splits it at ':'
 * Input:       The string, the size to allocate memory for
 * 				and a delim character that is ':' in this case
 * Output:      An array full of pointers to arrays with the strings
 */
char **splitString(char *str, int *size, const char *delim){
	*size = 1;
	for(int i=0; str[i] != '\0' ;i++){
		if(str[i]==*delim)
			*size=*size+1;
	}

	char **string = malloc(*size*sizeof(char*));
	char *pch;
	int positionToColon=0;
	int positionInArray=0;
	int positionToAdd=0;
	for(int i=0; str[i] != '\0';i++){
		if(str[i]==*delim || str[i+1]=='\0'){
			pch=calloc(sizeof(char), SIZE);
			positionToAdd=0;
			for(int j=positionToColon; j<i; j++, positionToAdd++){
				if(str[j]=='[' || str[j]==']'){
					positionToAdd--;
				}else
					pch[positionToAdd]=str[j];
			}
			string[positionInArray]=pch;
			positionInArray++;
			positionToColon=i+1;
		}
	}
	return string;
}

int main(void){
    int n=0,s=0;
    char **numbers;
    char bapc[100001]={'\0'};
    if(fscanf(stdin,"%d",&n)){
        for(int i=0;i<n;i++){
            int t=0,delf=0,delb=0;;
			bool rev = false;
            char list[100000]={'\0'};
            if(fscanf(stdin,"%s",bapc))
                if(fscanf(stdin,"%d ",&t))
                    if(fgets(list, SIZE, stdin)!=NULL);


            //numbers = splitString(list,&s,",");

            //Each letter in BAPC
            for (int j=0;j<100001;j++){
                if(bapc[j]=='\n' || bapc[j]=='\0')
                    break;
                if(bapc[j]=='R')
					rev = !rev;
				else if(bapc[j]=='D'){
					if(!rev)
						delf++;
					else
						delb++;
				}
            }
			if(t<delf+delb){
				printf("error\n");
			}
			else{
				printf("[");
				if(rev)
					for(int j=t-delb*2-1;j>=delf;j-=2){
						if(j!=t-delb-1)
						printf(",");
						printf("%s",&list[j]);
					}
				else
					for(int j=delf*2+1;j<t-delb;j+=2){
						if(j!=delf)
							printf(",");
						printf("%s",&list[j]);
					}
				printf("]\n");
			}
			/*if(s>0){
				for (int x = 0; x < s; x++) {
					free(numbers[x]);
				}
			} free(numbers);*/
		}
    }
	return 0;
}
