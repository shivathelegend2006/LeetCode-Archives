bool isAnagram(char* s, char* t) {
    int s_alpha[26] = {0};
    int t_alpha[26] = {0};
    for(int i=0;s[i] != '\0';i++){
        int i_s = s[i] - 'a';
        s_alpha[i_s]++;
    }

    for(int i=0;t[i] != '\0';i++){
        int i_t = t[i] - 'a';
        t_alpha[i_t]++;
    }
    for(int i=0;i<26;i++){
        if(s_alpha[i] != t_alpha[i]) return false;
    }
    return true;

}