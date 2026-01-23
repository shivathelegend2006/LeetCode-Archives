#include <ctype.h>
#include <string.h>
bool isPalindrome(char* s) {
    int left = 0;
    int right = strlen(s);
    int cond=1;
    while (left < right ){
        if (!isalnum(s[left])){
            left++;
            continue;
        }
        if (!isalnum(s[right])){
            right--;
            continue;
        }
        if (tolower(s[left]) != tolower(s[right]))
            cond=0;
        left++;
        right--;
    }    
    if (cond == 0)
        return false;
    else 
        return true;
}