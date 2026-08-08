class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        chars = set()
        for i, char in enumerate(s):
            if char in chars:
                maxLength = max(maxLength, i-left)
                if s[left] == char:
                    left += 1
                else:
                    while not s[left] == char:
                        chars.discard(s[left])
                        left += 1
                    left += 1
                
            chars.add(char)

        return max(maxLength, len(s)-left)
