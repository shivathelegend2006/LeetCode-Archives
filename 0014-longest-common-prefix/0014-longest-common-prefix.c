#include <string.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    for(int i=0;strs[0][i] != '\0';i++){
        char curr = strs[0][i];
        for(int j=1;j<strsSize;j++){
            if(strs[j][i] == '\0' || strs[j][i] != curr){
                strs[0][i] = '\0';
                return strs[0];
            }
        }
    }
    return strs[0];
}