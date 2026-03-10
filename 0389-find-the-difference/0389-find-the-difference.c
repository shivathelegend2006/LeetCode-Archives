#include <string.h>
char findTheDifference(char* s, char* t) {
    char e = 0;
    while(*s != '\0'){
        e ^= *s;
        s++;
    }

    while(*t != '\0'){
        e ^= *t;
        t++;
    }
    return e;
}