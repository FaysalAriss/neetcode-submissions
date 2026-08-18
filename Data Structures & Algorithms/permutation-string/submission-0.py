class Solution:
    def checkInclusion(self, s1: str, s2:str) -> bool:
        if len(s1) > len(s2):
            return False
        
        charCounts1 = defaultdict(int)
        charCounts2 = defaultdict(int)
        for i in range(len(s1)):
            charCounts1[s1[i]] += 1
            charCounts2[s2[i]] += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if charCounts1 == charCounts2:
                return True
            charCounts2[s2[left]] -= 1
            if charCounts2[s2[left]] == 0:
                charCounts2.pop(s2[left])
            left += 1
            charCounts2[s2[right]] += 1
            
        return charCounts1 == charCounts2