class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        left = 0
        right = left
        maxCount = 0
        maxLength = 0

        while right < len(s):  
            currentChar = s[right]
            charCount[currentChar] += 1
            maxCount = max(maxCount, charCount[currentChar])

            #if invalid substring then increment left
            while right-left+1 - maxCount > k:
                charCount[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right-left+1)
            right += 1

        return max(maxLength,right-left)