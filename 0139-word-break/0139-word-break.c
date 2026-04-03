#include <string.h>

bool wordBreak(char* s, char** wordDict, int wordDictSize) {
    int n = strlen(s);
    int dp[n+1] ;
    for(int i=0;i<n+1;i++){
        dp[i] = 0;
    }
    dp[0] = 1;
    for(int i=0;i<n;i++){
        if(dp[i]== 0) continue;
        for(int j=0;j<wordDictSize ;j++){
            int len = strlen(wordDict[j]);
            if(i + len <= n && strncmp(s+i, wordDict[j],len)==0) dp[len+i] = 1;
        }
    }
    return (dp[n] == 1) ? true : false;
}