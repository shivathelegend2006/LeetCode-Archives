#include <string.h>

bool isValid(char* s) {
    int n = strlen(s);
    char a[n];
    int i=0,j=-1;
    while(i<n){
        char x = s[i];
        if (x=='(' || x=='{' || x=='[') a[++j] = x;
        else if (j >=0 &&x==')' && a[j] == '(') a[j--] = '\0';
        else if (j >=0 && x=='}' && a[j] == '{') a[j--] = '\0';
        else if (j >=0 && x==']' && a[j] == '[') a[j--] = '\0';
        else return false;
        i++;
    }
    return (j==-1) ? true : false;
}