class Solution {
public:
    bool isPalindrome(int x) {
        int n = 0, y = x;
        if (x < 0) return false;
        if (x == 0) return true;
        while(y > 0){
            y /= 10;
            n++;
        }
        int digits[10], i =0;
        y = x;
        while(y > 0){
            digits[i] = y%10;
            y /= 10;
            i++;
        }
        for(int i=0;i<n;i++){
            if(digits[i] != digits[n-i-1]) return false;
        }
        return true;
    }
};