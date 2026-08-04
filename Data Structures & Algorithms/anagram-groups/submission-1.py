class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = {}
        for string in strs:
            charCount = [0] * 26 #number of lowercase english characters
            for char in string:
                charCount[ord(char)-ord('a')] += 1
            charCount = tuple(charCount)
            lists[charCount] = lists.get(charCount, [])
            lists[charCount].append(string)

        return list(lists.values())