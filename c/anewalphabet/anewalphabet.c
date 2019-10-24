#include <stdio.h>
#include <ctype.h>

char *alpha[127] = {
    ['a'] = "@",
    ['b'] = "8",
    ['c'] = "(",
    ['d'] = "|)",
    ['e'] = "3",
    ['f'] = "#",
    ['g'] = "6",
    ['h'] = "[-]",
    ['i'] = "|",
    ['j'] = "_|",
    ['k'] = "|<",
    ['l'] = "1",
    ['m'] = "[]\\//[]",
    ['n'] = "[]\\[]",
    ['o'] = "0",
    ['p'] = "|D",
    ['q'] = "(,)",
    ['r'] = "|Z",
    ['s'] = "$",
    ['t'] = "']['",
    ['u'] = "|_|",
    ['v'] = "\\//",
    ['w'] = "\\//\\//",
    ['x'] = "}{",
    ['y'] = "`/",
    ['z'] = "2"
};

int main(void){
    unsigned char c;
    while ((c=getchar())!=EOF) {
        if(isalnum(c))
            fputs(alpha[c],stdout);
        else
            putc(c,stdout);
    }
    return 0;
}
