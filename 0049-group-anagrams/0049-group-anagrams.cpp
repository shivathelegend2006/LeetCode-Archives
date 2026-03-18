#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm> // This gives us the sort() function

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> mailroom;
        for (string word : strs) {
            string signature = word; // Make a copy of the word
            
            sort(signature.begin(), signature.end()); 
            
            mailroom[signature].push_back(word);
        }
        
        vector<vector<string>> result;
        
        for (auto pair : mailroom) {
            result.push_back(pair.second); 
        }
        
        return result;
    }
};