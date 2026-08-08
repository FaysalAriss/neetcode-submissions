class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        chars = set()
        for i, char in enumerate(s):
            #if we've seen the current character then the stretch is done
            if char in chars:
                maxLength = max(maxLength, i-left)
                #more left until it is past the the character we're currently at, but on the left
                if not s[left] == char:
                    while not s[left] == char:
                        chars.discard(s[left])
                        left += 1
                left += 1 #move past it
            #keep track of characters seen
            chars.add(char)

        #check for the final stretch where right is = len(s)
        return max(maxLength, len(s)-left)
