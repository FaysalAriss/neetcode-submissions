class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        left = 0
        right = left
        maxCount = 0
        maxLength = 0

        #for each character move the window right, update the char count of the current substring appropriately
        #keep track of the largest char count ever as we can keep the window that size + k as any smaller would not be the largest
        for right in range(len(s)):  
            currentChar = s[right]
            charCount[currentChar] += 1
            maxCount = max(maxCount, charCount[currentChar])

            #if substring invalid it keeps the window the same length, but moves it right
            #it doesn't matter if the new window is invalid, because it is no longer than the maximum, so will not make the result false
            if right-left+1 - maxCount > k:
                charCount[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right-left+1)

        return max(maxLength,right-left)