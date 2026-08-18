class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.length() > s2.length()){
            return false;
        }

        unordered_map<char, int> charCounts1;
        unordered_map<char, int> charCounts2;
        for(int i = 0; i < s1.length(); ++i){
            charCounts1[s1[i]]++;
            charCounts2[s2[i]]++;
        }

        for(int right = s1.length(); right < s2.length(); ++right){
            if(charCounts1 == charCounts2){
                return true;
            }
            int left = right-s1.length();
            charCounts2[s2[left]]--;
            if(charCounts2[s2[left]] == 0){
                charCounts2.erase(s2[left]);
            }
            charCounts2[s2[right]]++;
        }

        return charCounts1 == charCounts2;
    }
};
