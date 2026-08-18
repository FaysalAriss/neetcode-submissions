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

        for(auto rightChar = s2.begin()+s1.length(); rightChar < s2.end(); ++rightChar){
            if(charCounts1 == charCounts2){
                return true;
            }
            char leftChar = *(rightChar-s1.length());
            charCounts2[leftChar]--;
            if(charCounts2[leftChar] == 0){
                charCounts2.erase(leftChar);
            }
            charCounts2[*rightChar]++;
        }

        return charCounts1 == charCounts2;
    }
};
