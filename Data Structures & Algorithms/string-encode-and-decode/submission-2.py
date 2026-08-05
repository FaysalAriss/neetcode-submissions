class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = []
        for string in strs:
            encodedString.append(f"{len(string)+1:3.0f}") #always 3 wide, as max length is 200
            encodedString.append(string)
        
        return "".join(encodedString)

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        i = 0
        while i < len(s):
            jump = int(s[i:i+3])
            decodedStrings.append(s[i+3:i+2+jump])
            i += jump+2

        return decodedStrings
