class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.length() > s2.length()){
            return false;
        }

        int charCounts1[26] = {0};
        int charCounts2[26] = {0};
        for(int i = 0; i < s1.length(); ++i){
            charCounts1[s1[i] - 'a']++;
            charCounts2[s2[i] - 'a']++;
        }

        int matches = 0;
        for(int i = 0; i < 26; ++i){
            if(charCounts1[i] == charCounts2[i]){
                matches++;
            }
        }

        for(auto rightChar = s2.begin()+s1.length(); rightChar < s2.end(); ++rightChar){
            if(matches == 26){
                return true;
            }
            int leftIndex = *(rightChar-s1.length()) - 'a';
            charCounts2[leftIndex]--;
            if(charCounts1[leftIndex] == charCounts2[leftIndex]){ //prev not matching and now matching
                matches++;
            }else if(charCounts1[leftIndex] == charCounts2[leftIndex]+1){ //prev matching and now not matching
                matches--;
            }
            int rightIndex = *rightChar - 'a';
            charCounts2[rightIndex]++;
            if(charCounts1[rightIndex] == charCounts2[rightIndex]){
                matches++;
            }else if(charCounts1[rightIndex] == charCounts2[rightIndex]-1){
                matches--;
            }
        }

        return matches == 26;
    }
};
