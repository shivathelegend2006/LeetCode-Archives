#include <string.h>
#include <stdlib.h>
char* reverseWords(char* s) {
    int len = strlen(s)-1;
    char* words = (char*)malloc((len+2)*sizeof(char));

    int i=len,j=0;
    while (i>=0 && s[i]==' ')
        i--;

    int start,end=len;
    while (i >= 0){
        
        while (i>=0 && s[i]==' ')
            i--;
        end = i;
        while (i>=0&&s[i] != ' ' ){
            start = i;
            i--;
        }
        for(int k=start;k<=end;k++){
            words[j] = s[k];
            j++;
        }
        words[j] = ' ';
        j++;

    }
    words[j-1] = '\0';
    j = strlen(words)-1;
    while(j>=0 && words[j] == ' ')
        j--;
    words[j+1] = '\0';
    return words;
}