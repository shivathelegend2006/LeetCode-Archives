#include <string.h>

int strStr(char* haystack, char* needle) {
    char *p = strstr(haystack,needle);
    if(p != NULL)
        return (int)(p - haystack);
    return -1;
}